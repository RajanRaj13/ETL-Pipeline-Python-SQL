import pandas as pd
import mysql.connector

# ---------- CONFIGURATION ----------
MYSQL_HOST = "localhost"
MYSQL_USER = "etl_user"        
MYSQL_PASSWORD = "Asha@#061" 
MYSQL_DB = "etl_db"
CSV_FILE = "data/processed/sales_clean.csv"
# -----------------------------------

def main():
    # 1. Connect to MySQL
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        print("✅ Connected to MySQL")
    except mysql.connector.Error as err:
        print("❌ Connection error:", err)
        return

    cursor = conn.cursor()

    # 2. Load cleaned CSV
    try:
        df = pd.read_csv(CSV_FILE)
        print(f"✅ Loaded CSV with {len(df)} rows")
    except Exception as e:
        print("❌ Error reading CSV:", e)
        return

    # 3. Insert into MySQL
    try:
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO sales 
                (order_id, order_date, customer, region, product, quantity, price, total_amount)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """, tuple(row))
        conn.commit()
        print("✅ Data loaded into MySQL successfully")
    except mysql.connector.Error as e:
        print("❌ Error inserting data:", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()

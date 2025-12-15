import pandas as pd

def transform_data(df):
    # 1. Handle missing values
    df['quantity'].fillna(1, inplace=True)
    df['price'].fillna(df['price'].mean(), inplace=True)

    # 2. Convert date column
    df['order_date'] = pd.to_datetime(df['order_date'])

    # 3. Create new column
    df['total_amount'] = df['quantity'] * df['price']

    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw/sales_raw.csv")
    df_clean = transform_data(df)

    df_clean.to_csv("data/processed/sales_clean.csv", index=False)
    print("✅ Data transformation completed")

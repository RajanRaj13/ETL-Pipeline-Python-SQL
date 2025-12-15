import pandas as pd

def extract_data():
    df = pd.read_csv("data/raw/sales_raw.csv")
    print("✅ Data extracted successfully")
    return df

if __name__ == "__main__":
    df = extract_data()
    print(df.head())

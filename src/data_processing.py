import os
import json
import pandas as pd

def load_raw_data(filename='data/raw/financial_data.json'):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def process_data(data):
    # Convert to DataFrame and perform basic cleaning
    df = pd.DataFrame(data)
    # Convert 'value' to numeric and drop rows with conversion issues
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df.dropna(inplace=True)
    return df

def save_processed_data(df, filename='data/processed/processed_data.csv'):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Processed data saved to {filename}")

def main():
    raw_data = load_raw_data()
    df = process_data(raw_data)
    save_processed_data(df)

if __name__ == '__main__':
    main()

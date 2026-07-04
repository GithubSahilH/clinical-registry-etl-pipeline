import glob
import os
import pandas as pd

# Find all CSV files in your current folder
csv_files = glob.glob("*.csv")

print("--- Data Inspection ---")
for file in csv_files:
    try:
        # Load just the first 2 rows to peek at the columns and data types
        df_peek = pd.read_csv(file, nrows=2)
        print(f"\nFile: {file}")
        print(f"Columns: {list(df_peek.columns)}")
        print(f"Sample Row: {df_peek.iloc[0].to_dict()}")
    except Exception as e:
        print(f"Could not read {file}: {e}")
# ====================================================
# src/ingestion/bronze_loader.py
# Loads raw CSV data into the PostgreSQL Bronze Layer
# ====================================================

import pandas as pd 
from sqlalchemy import create_engine
import os

# Database connection details (matching our docker-compose.yml)
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5433" # Changed to 5433 because 5432 was already in use!
DB_NAME = "dataforge"

# Create the database engine
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def load_csv_to_db(csv_path: str, table_name: str):
    """Reads a CSV file and loads it into a PostgreSQL table."""
    print(f"Extracting data from {csv_path}...")

    # EXTRACT: Read the CSV
    df = pd.read_csv(csv_path)

    # Add metadata column to track when we loaded this data
    df['_loaded_at'] = pd.Timestamp.now()

    #LOAD: Write to PostgreSQL
    print(f"Loading {len(df)} records into table '{table_name}'...")
    df.to_sql(
        table_name,
        engine,
        if_exists='replace', # If the table exists, drop it and recreate
        index=False,        # Don't write the pandas index as a column
        chunksize=10000     # Load in chunks to save memory
    )
    print(f" Successfully loaded {table_name}!\n")

if __name__ == '__main__':
    print(" Starting Bronze Layer Ingestion Pipeline...\n")

    # Define the files we want to load
    raw_data_dir = 'data/raw'
    tables_to_load = {
        'customers.csv': 'bronze_customers',
        'products.csv': 'bronze_products',
        'orders.csv': 'bronze_orders',
        'order_items.csv': 'bronze_order_items'
    }

    # Loop through and load each file
    for csv_file, table_name in tables_to_load.items():
        csv_path = os.path.join(raw_data_dir, csv_file)
        if os.path.exists(csv_path):
            load_csv_to_db(csv_path, table_name)
        else:
            print(f" File not found: {csv_path}")

    print(" Bronze Ingestion Pipeline Complete!")
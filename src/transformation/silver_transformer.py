# ===========================================================
# src/transformation/silver_transformer.py
# Cleans Bronze data and loads it into Silver Layer
# ============================================================

import pandas as pd 
from sqlalchemy import create_engine

# Database connection
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "dataforge"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def transform_customers():
    """Clean and standardize customer data."""
    print(" Reading bronze_customers...")
    df = pd.read_sql("SELECT * FROM bronze_customers", engine)

    print(" Cleaning customer data...")
    # Remove leading/trailing spaces and standardize formatting
    df['first_name'] = df['first_name'].str.strip().str.title()
    df['last_name'] = df['last_name'].str.strip().str.title()
    df['email'] = df['email'].str.strip().str.lower()
    df['city'] = df['city'].str.strip().str.title()
    df['state'] = df['state'].str.strip().str.upper()

    # Fill missing cities with 'Unknown'
    df['city'] = df['city'].fillna('Unknown')

    print(" Loading silver_customers...")
    df.to_sql('silver_customers', engine, if_exists='replace', index=False)
    print(f" silver_customers loaded: {len(df)} records\n")

def transform_products():
    """Clean and standardize product data."""
    print(" Reading bronze_products...")
    df = pd.read_sql("SELECT * FROM bronze_products", engine)

    print(" Cleaning product data...")
    df['products_name'] = df['products_name'].str.strip().str.title()
    df['category'] = df['category'].str.strip().str.title()

    print(" Loading silver_products...")
    df.to_sql('silver_products', engine, if_exists='replace', index=False)
    print(f" silver_products loaded: {len(df)} records\n")

def transform_orders():
    """Clean and standardize order data."""
    print(" Reading bronze orders... ")
    df = pd.read_sql("SELECT * FROM bronze_orders", engine)

    print(" Cleaning order data...")
    df['status'] = df['status'].str.strip().str.lower()
    df['payment_method'] = df['payment_method'].str.strip().str.title()

    print(" Loading silver_orders...")
    df.to_sql('silver_orders', engine, if_exists='replace', index=False)
    print(f" silver_orders loaded: {len(df)} records\n")
    
if __name__ == '__main__':
    print(" Starting Silver Layer Transformation Pipeline...\n")
    transform_customers()
    transform_products()
    transform_orders()
    print("Silver Transformation Complete!")
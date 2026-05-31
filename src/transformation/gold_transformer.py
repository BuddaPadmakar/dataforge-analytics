# ==============================================================
# src/transformation/gold_transformer.py
# Creates the Star Schema (Gold Layer) for Analytics
# ==============================================================

import pandas as pd 
from sqlalchemy import create_engine

# Database connection
DB_USER = "admin" 
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "dataforge"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def create_dim_customers():
    """Create customer dimension with surrogate key."""
    print(" Building dim_customers...")
    df = pd.read_sql("SELECT * FROM silver_customers", engine)

    # Generate a surrogate key (unique sequential ID)
    df['customer_key'] = range(1, len(df) +1) 

    # Reorder columns so the key is first
    cols = ['customer_key'] + [col for col in df.columns if col != 'customer_key']
    df = df[cols]

    df.to_sql('dim_customers', engine, if_exists='replace', index=False)
    print(f" dim_customers loaded: {len(df)} records\n")

def create_dim_products():
    """Create product dimension with surrogate key."""
    print(" Building dim_products...")
    df = pd.read_sql("SELECT * FROM silver_products", engine)

    # Generate a surrogate key
    df['product_key'] = range(1, len(df) + 1)

    cols = ['product_key'] + [col for col in df.columns if col != 'product_key']
    df = df[cols]   

    df.to_sql('dim_products', engine, if_exists='replace', index=False)
    print(f" dim_products loaded: {len(df)} records\n")

def create_dim_date():
    """Create date dimension from order dates."""
    print(" Building dim_date...")
    orders = pd.read_sql("SELECT order_date FROM silver_orders", engine)

    # Get the min and max dates from our orders
    min_date = pd.to_datetime(orders['order_date'].min())
    max_date = pd.to_datetime(orders['order_date'].max())

    # Create a continuous range of dates
    date_range = pd.date_range(start=min_date, end=max_date, freq='D')
    df = pd.DataFrame({'full_date': date_range})

    # Extract date attributes (vital for dashboards!)
    df['date_key'] = df['full_date'].dt.strftime('%Y%m%d').astype(int)
    df['year'] = df['full_date'].dt.year
    df['month'] = df['full_date'].dt.month
    df['day'] = df['full_date'].dt.day
    df['day_of_week'] = df['full_date'].dt.day_name()
    df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])

    df.to_sql('dim_date', engine, if_exists='replace', index=False)
    print(f" dim_date loaded: {len(df)} records\n")

def create_fact_sales():
    """Create the sales fact table by joining items, orders, and dimensions."""
    print(" Building fact_sales...")

    # 1. Read the tables we need
    order_items = pd.read_sql("SELECT * FROM bronze_order_items", engine)
    orders = pd.read_sql("SELECT order_id, customer_id, order_date FROM silver_orders", engine)
    dim_cust = pd.read_sql("SELECT customer_key, customer_id FROM dim_customers", engine)
    dim_prod = pd.read_sql("SELECT product_key, product_id FROM dim_products", engine)
    dim_date = pd.read_sql("SELECT date_key, full_date FROM dim_date", engine)

    # 2. Join order items with orders to get customer_id and order_date
    fact = order_items.merge(orders, on='order_id', how='left')

    # 3. Join with dimensions to get the SURROGATE KEYS
    fact = fact.merge(dim_cust, on='customer_id', how='left')
    fact = fact.merge(dim_prod, on='product_id', how='left')

    # 4. Join with date dimension (match order_date to full_date)
    fact['order_date'] = pd.to_datetime(fact['order_date']).dt.date
    dim_date['full_date'] = pd.to_datetime(dim_date['full_date']).dt.date
    fact = fact.merge(dim_date, left_on='order_date', right_on='full_date', how='left')

    # 5. Select only the columns we need for the final fact table
    fact_final = fact[[
        'customer_key',
        'product_key',
        'date_key',
        'order_id',
        'quantity',
        'unit_price',
        'discount_pct',
        'net_amount',
        'tax_amount'
    ]].copy()

    # 6. Generate a surrogate key for the fact table
    fact_final['sales_key'] = range(1, len(fact_final) + 1)

    # Reorder columns
    cols = ['sales_key'] + [col for col in fact_final.columns if col != 'sales_key']
    fact_final = fact_final[cols]

    fact_final.to_sql('fact_sales', engine, if_exists='replace', index=False)
    print(f" fact_sales loaded: {len(fact_final)} record\n")

if __name__ == '__main__':
    print(" Starting Gold Layer (Star Schema) Creation...\n")

    # Dimensions must be created BEFORE the Fact table!
    create_dim_customers()
    create_dim_products()
    create_dim_date()

    # Fact table relies on the dimensions
    create_fact_sales()

    print(" Gold Layer (Star Schema) Complete!")

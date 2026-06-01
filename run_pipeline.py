# ========================================
# run_pipeline.py
# Master Orchestrator with Data Quality Checks
# ========================================

import sys
import os
import pandas as pd
from sqlalchemy import create_engine

# Add the src folder to Python's path so we can import our other scripts
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import our pipeline functions
from ingestion.bronze_loader import load_csv_to_db
from transformation.silver_transformer import transform_customers, transform_products, transform_orders
from transformation.gold_transformer import create_dim_customers, create_dim_products, create_dim_date, create_fact_sales

# Database connection
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "dataforge"
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def data_quality_check(table_name, min_rows=1):
    """Checks if a table exists and has enough rows."""
    print(f"🛡️ Running Data Quality Check on {table_name}...")
    try:
        df = pd.read_sql(f"SELECT * FROM {table_name}", engine)
        row_count = len(df)
        
        if row_count < min_rows:
            raise ValueError(f"❌ DQ CHECK FAILED: {table_name} only has {row_count} rows (Minimum: {min_rows})")
        
        print(f"✅ DQ CHECK PASSED: {table_name} has {row_count} records.")
        return True
    except Exception as e:
        print(f"❌ DQ CHECK FAILED: Could not read {table_name}. Error: {e}")
        return False

def run_full_pipeline():
    """Executes the entire Medallion Architecture pipeline."""
    print("="*50)
    print("🚀 STARTING DATAFORGE MASTER PIPELINE 🚀")
    print("="*50)
    
    raw_data_dir = 'data/raw'
    tables_to_load = {
        'customers.csv': 'bronze_customers',
        'products.csv': 'bronze_products',
        'orders.csv': 'bronze_orders',
        'order_items.csv': 'bronze_order_items'
    }

    # --- BRONZE LAYER ---
    print("\n🥉 INGESTING BRONZE LAYER...")
    for csv_file, table_name in tables_to_load.items():
        csv_path = os.path.join(raw_data_dir, csv_file)
        if os.path.exists(csv_path):
            load_csv_to_db(csv_path, table_name)
        else:
            print(f"❌ File not found: {csv_path}. Aborting pipeline!")
            return # Stop the pipeline if source data is missing

    # --- SILVER LAYER ---
    print("\n🥈 TRANSFORMING SILVER LAYER...")
    transform_customers()
    transform_products()
    transform_orders()
    
    # --- DATA QUALITY GATE ---
    print("\n🛡️ RUNNING SILVER QUALITY GATE...")
    if not data_quality_check('silver_orders', min_rows=1000):
        print("🚨 Pipeline aborted! Silver layer data quality failed.")
        return

    # --- GOLD LAYER ---
    print("\n🥇 BUILDING GOLD LAYER (STAR SCHEMA)...")
    create_dim_customers()
    create_dim_products()
    create_dim_date()
    create_fact_sales()
    
    # --- FINAL VALIDATION ---
    print("\n🛡️ RUNNING FINAL GOLD QUALITY GATE...")
    if not data_quality_check('fact_sales', min_rows=1000):
        print("🚨 Pipeline aborted! Gold layer data quality failed.")
        return

    print("\n" + "="*50)
    print("🎉 DATAFORGE PIPELINE COMPLETED SUCCESSFULLY! 🎉")
    print("="*50) 

if __name__ == '__main__':
    run_full_pipeline()
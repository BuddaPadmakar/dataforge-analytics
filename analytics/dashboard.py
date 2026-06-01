# ========================================
# analytics/dashboard.py
# Interactive Analytics Dashboard
# ========================================

import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# Database connection
DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "dataforge"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Set up the page layout
st.set_page_config(page_title="DataForge Analytics", page_icon="📊", layout="wide")
st.title("📊 DataForge E-Commerce Analytics")

# Load data from Gold Layer (with caching so it doesn't reload every second)
@st.cache_data
def load_data():
    fact = pd.read_sql("SELECT * FROM fact_sales", engine)
    products = pd.read_sql("SELECT * FROM dim_products", engine)
    customers = pd.read_sql("SELECT * FROM dim_customers", engine)
    return fact, products, customers

with st.spinner("Loading data from Data Warehouse..."):
    fact, products, customers = load_data()

# Join data for visualizations
sales_data = fact.merge(products, on='product_key', how='left')

# --- KPI METRICS ---
st.markdown("---")
col1, col2, col3 = st.columns(3)

total_revenue = sales_data['net_amount'].sum()
total_orders = sales_data['order_id'].nunique()
avg_order_value = sales_data['net_amount'].mean()

with col1:
    st.metric("💰 Total Revenue", f"${total_revenue:,.0f}")
with col2:
    st.metric("📦 Total Orders", f"{total_orders:,}")
with col3:
    st.metric("💵 Avg Order Value", f"${avg_order_value:,.2f}")

st.markdown("---")

# --- CHARTS ---  
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Revenue by Category")
    cat_revenue = sales_data.groupby('category')['net_amount'].sum().reset_index()
    fig_cat = px.bar(
        cat_revenue, x='category', y='net_amount', 
        color='category', title='Revenue by Product Category',
        labels={'net_amount': 'Revenue ($)', 'category': 'Category'}
    )
    st.plotly_chart(fig_cat, use_container_width=True)

with col_right:
    st.subheader("Top 5 Products by Revenue")
    prod_revenue = sales_data.groupby('products_name')['net_amount'].sum().reset_index()
    prod_revenue = prod_revenue.sort_values(by='net_amount', ascending=False).head(5)
    fig_prod = px.bar(
        prod_revenue, x='net_amount', y='products_name', orientation='h',
        color='products_name', title='Top 5 Products',
        labels={'net_amount': 'Revenue ($)', 'products_name': 'Product'}
    )
    st.plotly_chart(fig_prod, use_container_width=True) 
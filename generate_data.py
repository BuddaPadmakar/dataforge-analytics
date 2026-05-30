# ====================================================
# generate_data.py
# Generates realistic e-commerce data
# ====================================================

import pandas as pd 
import numpy as np
import os
import random 
from datetime import datetime, timedelta 

class ECommerceDataGenerator:
    def __init__(self):
        np.random.seed(42)
        random.seed(42)
        self.output_dir = 'data/raw'
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_customers(self, num_customers=5000):
        print("Generating customers...")
        cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Seattle', 'Denver', 'Boston', 'Nashville', 'Portland']
        states = ['NY', 'CA', 'IL', 'TX', 'AZ', 'WA', 'CO', 'MA', 'TN', 'OR']
        segments = ['Consumer', 'Corporate', 'Home Office']

        customers = pd.DataFrame({
            'customer_id': range(1, num_customers+1),
            'first_name': [f'First_{i}' for i in range(1, num_customers +1)],
            'last_name': [f'Last_{i}' for i in range(1, num_customers+1)],
            'email': [f'user_{i}@email.com' for i in range(1, num_customers + 1)],
            'city': random.choices(cities, k=num_customers),
            'state': random.choices(states, k=num_customers),
            'country': 'USA',
            'segment': random.choices(segments, weights=[50, 30, 20], k=num_customers),
            'registration_date': pd.date_range(start='2022-01-01', periods=num_customers, freq='2H'),
            'is_active': random.choices([True, False], weights=[85, 15], k=num_customers)
        })
        customers.to_csv(f'{self.output_dir}/customers.csv', index=False)
        print(f" Customers saved: {len(customers)} records")
        return customers 
    
    def generate_products(self, num_products=1000):
        print("Generating products...")
        categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books']

        products = pd.DataFrame({
            'product_id': range(1, num_products+1),
            'products_name': [f'Product_{i}' for i in range(1, num_products+1)],
            'category': random.choices(categories, k=num_products),
            'unit_price': np.round(np.random.uniform(10, 500, num_products), 2),
            'cost_price': np.round(np.random.uniform(5, 250, num_products), 2),
            'is_available': random.choices([True, False], weights=[90, 10], k=num_products)
        })
        products.to_csv(f'{self.output_dir}/products.csv', index=False)
        print(f"Products saved: {len(products)} records")
        return products 
    
    def generate_orders(self, customers, products, num_orders=50000):
        print("Generating orders and order items...")
        statuses = ['completed', 'pending', 'shipped', 'cancelled', 'returned']
        payment_methods = ['Credit Card', 'Debit Card', 'Paypal', 'Bank Transfer']

        order_dates = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')

        orders = []
        order_items = []
        order_id = 1
        item_id = 1

        for _ in range(num_orders):
            cust = customers.sample(1).iloc[0]
            prod = products.sample(1).iloc[0]
            qty = random.randint(1, 5)
            order_date = random.choice(order_dates)

            discount_pct = random.choices([0, 5, 10, 15, 20], weights=[50, 20, 15, 10, 5]) [0]
            unit_price = prod['unit_price']
            net_amount = round(unit_price * qty * (1 - discount_pct/100), 2)
            tax_amount = round(net_amount * 0.08, 2)

            orders.append({
                'order_id': order_id,
                'customer_id': cust['customer_id'],
                'order_date': order_date,
                'status': random.choices(statuses, weights=[70, 10, 10, 5, 5]) [0],
                'payment_method': random.choice(payment_methods),
                'total_amount': round(net_amount + tax_amount, 2)
            })

            order_items.append({
                'order_item_id': item_id,
                'order_id' : order_id,
                'product_id' : prod['product_id'],
                'quantity': qty,
                'unit_price' : unit_price,
                'discount_pct' : discount_pct,
                'net_amount' : net_amount,
                'tax_amount' : tax_amount 
            })

            order_id += 1
            item_id += 1

        df_orders = pd.DataFrame(orders)
        df_order_items = pd.DataFrame(order_items)

        df_orders.to_csv(f'{self.output_dir}/orders.csv', index=False)
        df_order_items.to_csv(f'{self.output_dir}/order_items.csv' , index=False)

        print(f" Orders saved: {len(df_orders)} records")
        print(f" Order Items saved: {len(df_order_items)} records")

if __name__ == '__main__':
    print(" Starting Data Generation...")
    gen = ECommerceDataGenerator()
    cust = gen.generate_customers()
    prod = gen.generate_products()
    gen.generate_orders(cust, prod)
    print(" Data generation complete! Check the data/raw/ folder.")
            
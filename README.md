#  DataForge Analytics Platform
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org) [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com) [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
---


End-to-End Data Engineering & Analytics Pipeline. An industry-grade, production-ready e-commerce data platform.


# Table of Contents

● (Overview)

● Architecture

● Tech Stack

● Data Architecture

● Data Model (Star Schema)

● Data Quality & Orchestration

● Project Structure

● Reproducibility




💡 Business Value

A production-ready e-commerce data platform that processes raw transactional data and transforms it into actionable business insights. This project demonstrates the complete data lifecycle, focusing on data quality, scalable architecture, and analytical accessibility

## 🏗️ Architecture

The data pipeline follows the Medallion Architecture pattern, ensuring data quality and scalability at each layer


📄 Source Systems: Raw CSVs --> Python Ingestion

🥉 Bronze Layer   --> Cleaning & Standardization 

🥈 Siver Layer  --> Star Schema Modeling 

🥇 Gold Layer   --> BI Analytics

📊 Streamlit Dashboard



### Fix 2: The Database ERD Diagram
1. In the same editing screen, find `## 📊 Data Model (Star Schema)`.
2. **Delete** everything from that heading down to the `---` below it.
3. Replace it with **exactly** this:

```markdown
# 📊 Data Model (Star Schema)

The Gold layer utilizes a Star Schema designed for fast analytical queries.

```mermaid
erDiagram
    DIM_CUSTOMERS ||--o{ FACT_SALES : "has"
    DIM_PRODUCTS ||--o{ FACT_SALES : "includes"
    DIM_DATE ||--o{ FACT_SALES : "occurs on"

    DIM_CUSTOMERS {
        int customer_key PK
        int customer_id
        string first_name
        string email
        string segment
    }
    DIM_PRODUCTS {
        int product_key PK
        int product_id
        string products_name
        string category
        float unit_price
    }
    DIM_DATE {
        int date_key PK
        date full_date
        int year
        string month_name
        boolean is_weekend
    }
    FACT_SALES {
        int sales_key PK
        int customer_key FK
        int product_key FK
        int date_key FK
        int quantity
        float net_amount
        float tax_amount
    }

<div align="center">

![Data Engineering](https://img.shields.io/badge/Data-Engineering-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

# 🏆 DataForge Analytics Platform
### End-to-End Data Engineering & Analytics Pipeline

An industry-grade, production-ready e-commerce data platform demonstrating expertise in data ingestion, transformation, warehousing, orchestration, and business intelligence.

[View Project Architecture](#-architecture) · [Quick Start](#-quick-start) · [Dashboard Preview](#-dashboard-preview)

</div> 

---

## 📐 Architecture

This project implements the **Medallion Architecture** (Bronze → Silver → Gold), the industry standard for scalable data platforms built at companies like Netflix, Airbnb, and Uber.

```mermaid
graph TD
    A[📄 Raw CSV Data] -->|Python Ingestion| B(🥉 Bronze Layer)
    B -->|Cleaning & Standardization| C(🥈 Silver Layer)
    C -->|Star Schema Modeling| D(🥇 Gold Layer)
    D -->|BI Analytics| E(📊 Streamlit Dashboard)
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#cd7f32,stroke:#333,stroke-width:2px
    style C fill:#C0C0C0,stroke:#333,stroke-width:2px
    style D fill:#FFD700,stroke:#333,stroke-width:2px
    style E fill:#4B0082,stroke:#fff,stroke-width:2px,color:#fff



---

### Chunk 2: Tech Stack and Data Model
Copy this next box, and paste it directly below the first chunk in your `README.md`.

```text
## 🛠️ Tech Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | Pipeline development, orchestration, and data manipulation |
| **Storage** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white) | Relational Data Warehouse |
| **Infrastructure** | ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) | Containerized database environment |
| **Transformation** | **Pandas** | Data cleaning, joins, and Star Schema construction |
| **Analytics** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white) | Interactive Business Intelligence Dashboards |
| **Version Control**| ![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white) | Source code management and CI/CD |

---

## 🏗️ Data Architecture Deep Dive

### 🥉 Bronze Layer (Raw)
- **Objective:** Ingest data exactly as it arrives from the source, maintaining a full audit trail.
- **Process:** Python script reads raw CSVs, appends a `_loaded_at` audit timestamp, and performs a full load into PostgreSQL.
- **Tables:** `bronze_customers`, `bronze_products`, `bronze_orders`, `bronze_order_items`

### 🥈 Silver Layer (Cleaned)
- **Objective:** Clean, standardize, and deduplicate data to create a single source of truth.
- **Process:** Trimming whitespaces, title-casing names, lowercasing emails, and handling null values.
- **Tables:** `silver_customers`, `silver_products`, `silver_orders`

### 🥇 Gold Layer (Modeled)
- **Objective:** Construct a **Star Schema** optimized for fast analytical queries and BI dashboards.
- **Process:** Generate surrogate keys, join cleaned tables, and extract date attributes.
- **Tables:** `fact_sales`, `dim_customers`, `dim_products`, `dim_date`

#### Star Schema Entity Relationship Diagram (ERD)


## 🛡️ Data Quality & Engineering Best Practices

This project isn't just about moving data; it's about **trust and reliability**.

- **Automated Quality Gates:** The master pipeline runs row-count checks between layers. If a load fails or yields 0 rows, the pipeline aborts immediately (Fail-Fast methodology).
- **Audit Lineage:** `_loaded_at` timestamps track exactly when data entered the system.
- **Ethical Data Generation:** Realistic synthetic data simulates production edge cases (seasonality, return rates, varied payment methods) while adhering to strict data privacy (GDPR/CCPA) standards.
- **Idempotent Design:** Pipeline scripts use `if_exists='replace'` ensuring the pipeline can be re-run safely without duplicating data.

---

## 📸 Dashboard Preview

The Streamlit dashboard provides real-time business insights powered by the Gold Star Schema.

![Dashboard KPIs](https://img.shields.io/badge/KPIs-Revenue%2C%20Orders%2C%20AOV-brightgreen)
![Dashboard Charts](https://img.shields.io/badge/Charts-Category%20Revenue%2C%20Top%20Products-blue)

*(To see it live, follow the Quick Start steps below!)*

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Docker Desktop (Running)

### 1. Clone the repository
```bash
git clone https://github.com/BuddaPadmakar/dataforge-analytics.git
cd dataforge-analytics
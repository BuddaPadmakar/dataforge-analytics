#  DataForge Analytics Platform **End-to-End Data Engineering & Analytics Pipeline** ![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?style=for-the-badge&logo=postgresql) ![Docker](https://img.shields.io/badge/Docker-Compose-blue?style=for-the-badge&logo=docker) ![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit) 


End-to-End Data Engineering & Analytics Pipeline. An industry-grade, production-ready e-commerce data platform.

Business Value

A production-ready e-commerce data platform that processes raw transactional data and transforms it into actionable business insights. This project demonstrates the complete data lifecycle, focusing on data quality, scalable architecture, and analytical accessibility

🏗️ Architecture
This project implements the Medallion Architecture, the industry standard for scalable data platforms.

📄 Raw CSV --> 🥉Bronze (Raw) --> 🥈 Silver (Cleaned) --> 🥇 Gold (Star Schema) --> 📊 Dashboard

1. Bronze Layer (Raw): Ingests raw CSV data into PostgreSQL
2. Silver Layer (Cleaned): Cleans, standardizes, and deduplicates data.
3. Gold Layer (Modeled): Constructs a Star Schema for analytics.
4. Quality Gates: Automated checks ensure data integrity.

⛁ Tech Stack

● Language: Python

● Storage: PostgreSQL

● Infrastructure: Docker

● Transformation: Pandas

● Analytics: Streamlit, Plotly

● Version Control: Git, GitHub



🚀 Quick Start

1. Clone the repo: git clone https://github.com/BuddaPadmakar/dataforge-analytics.git
2. Setup environment: python3 -m venv venv then source venv/bin/activate then pip install -r requirements.txt
3. Start Database: docker compose up -d
4. Generate Data: python3 generate_data.py
5. Run Pipeline: python3 run_pipeline.py
6. View Dashboard: python3 -m streamlit run analytics/dashboard.py

👩🏻‍💻 Author

Padmakar Budda

Built to obsession for clean data

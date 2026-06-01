# 🏆 DataForge Analytics Platform **End-to-End Data Engineering & Analytics Pipeline** ![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?style=flat-square&logo=postgresql) ![Docker](https://img.shields.io/badge/Docker-Compose-blue?style=flat-square&logo=docker) ![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=flat-square&logo=streamlit)




DataForge Analytics Platform

End-to-End Data Engineering & Analytics Pipeline. An industry-grade, production-ready e-commerce data platform.

🏗️ Architecture
This project implements the Medallion Architecture (Bronze -> Silver -> Gold).

1. Bronze Layer (Raw): Ingests raw CSV data into PostgreSQL
2. Silver Layer (Cleaned): Cleans, standardizes, and deduplicates data.
3. Gold Layer (Modeled): Constructs a Star Schema for analytics.
4. Quality Gates: Automated checks ensure data integrity.

Tech Stack

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

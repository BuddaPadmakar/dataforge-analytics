#  DataForge Analytics Platform
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org) [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com) [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
---


End-to-End Data Engineering & Analytics Pipeline. An industry-grade, production-ready e-commerce data platform.


# Table of Contents

● [(Overview)]

● Architecture

● Tech Stack

● Data Architecture

● Data Model (Star Schema)

● Data Quality & Orchestration

● Project Structure

● Reproducibility




💡 Business Value

A production-ready e-commerce data platform that processes raw transactional data and transforms it into actionable business insights. This project demonstrates the complete data lifecycle, focusing on data quality, scalable architecture, and analytical accessibility

# 🏗️ Architecture

The data pipeline follows the Medallion Architecture pattern, ensuring data quality and scalability at each layer


📄 Source Systems: Raw CSVs --> Python Ingestion

🥉 Bronze Layer   --> Cleaning & Standardization 

🥈 Siver Layer  --> Star Schema Modeling 

🥇 Gold Layer   --> BI Analytics

📊 Streamlit Dashboard


⛁ Tech Stack

● Language: Python      

● Storage: PostgreSQL

● Infrastructure: Docker

● Transformation: Pandas

● Analytics: Streamlit, Plotly

● Version Control: Git, GitHub


# 📁 Project Structure


<img width="630" height="204" alt="image" src="https://github.com/user-attachments/assets/c912ca46-886d-4e7a-af12-6bba9f57add7" />


# 🚀 Quick Start

1. Clone the repo: git clone https://github.com/BuddaPadmakar/dataforge-analytics.git
2. Setup environment: python3 -m venv venv then source venv/bin/activate then pip install -r requirements.txt
3. Start Database: docker compose up -d
4. Generate Data: python3 generate_data.py
5. Run Pipeline: python3 run_pipeline.py
6. View Dashboard: python3 -m streamlit run analytics/dashboard.py

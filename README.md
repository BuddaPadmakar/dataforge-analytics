#  DataForge Analytics Platform
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org) [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com) [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
---


End-to-End Data Engineering & Analytics Pipeline. An industry-grade, production-ready e-commerce data platform.


# Table of Contents

● [Overview]

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

 
📄 Source Systems: Raw CSVs --> |Python Ingestion| B(🥉 Bronze Layer)  B --> |Cleaning & Standardization|  C(🥈 Siver Layer)  C -->|Star Schema Modeling| D(🥇 Gold Layer)   D --> |BI Analytics|  E(📊 Streamlit Dashboard)  

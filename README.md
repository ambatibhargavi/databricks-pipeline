# ETL Pipeline with Databricks DLT Overview

This project implements a scalable ETL (Extract, Transform, Load) pipeline using Databricks Delta Live Tables (DLT). The pipeline is designed with the Medallion Architecture (Bronze → Silver → Gold), ensuring reliable data ingestion, transformation, and analytics.

Architecture  
<img width="2322" height="680" alt="image" src="https://github.com/user-attachments/assets/d59d8831-603b-4023-b791-d70ba0a342e1" />
<img width="1435" height="817" alt="Screenshot 2025-08-15 at 21 22 37" src="https://github.com/user-attachments/assets/cd6d0c07-3a8c-4041-8385-67856ce6110a" />
<img width="1440" height="822" alt="Screenshot 2025-08-15 at 21 22 24" src="https://github.com/user-attachments/assets/065cb16b-c372-458e-8e5d-8fdae5d4072b" />
<img width="2700" height="1170" alt="image" src="https://github.com/user-attachments/assets/8528e0ef-6cfc-4ef1-8164-79b398a7dcbe" />

Bronze Layer → Raw data ingestion from the source system into Delta Lake.

Silver Layer → Data cleaning, standardization, and enrichment for downstream use.

Gold Layer → Aggregated and business-ready data for reporting and analytics.

Key Features

Automated data ingestion and processing using DLT.

Data quality enforcement with schema validation.

Scalable transformations following best practices in the Medallion Architecture.

Optimized for analytics and reporting use cases.

Tech Stack

Databricks (Delta Live Tables)

Delta Lake

Medallion Architecture

Use Cases

Business reporting and dashboards.

Reliable data pipelines for analytics.

Clean and standardized datasets for machine learning workflows.         

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

<img width="1439" height="807" alt="Screenshot 2025-08-17 at 14 25 57" src="https://github.com/user-attachments/assets/bc19855c-9a9d-456a-b4ec-be550b8f8789" />
<img width="1437" height="808" alt="Screenshot 2025-08-19 at 22 57 55" src="https://github.com/user-attachments/assets/78c78cf2-ed30-4d6b-9380-a9cfc7ad5d62" />
<img width="1440" height="809" alt="Screenshot 2025-08-17 at 14 29 46" src="https://github.com/user-attachments/assets/b38245ca-4321-4bab-b685-69210f31d437" />
<img width="261" height="185" alt="Screenshot 2025-08-21 at 16 33 58" src="https://github.com/user-attachments/assets/79986edf-df43-47a3-88f0-b99357e7162b" />
<img width="1440" height="813" alt="Screenshot 2025-08-21 at 16 33 31" src="https://github.com/user-attachments/assets/0895c392-e284-40c0-9463-c22ad517e58c" />

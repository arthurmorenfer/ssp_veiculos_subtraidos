🚗 São Paulo Vehicle Theft Analytics Pipeline
📋 Project Overview

This project establishes a complete data engineering pipeline for analyzing vehicle theft and robbery data provided by the São Paulo State Public Security Secretariat (SSP-SP). The goal is to transform messy, administrative Excel records into a high-performance analytical environment using a Medallion Architecture and Dimensional Modeling.
The Problem

Public security data in Brazil is often distributed in inconsistent .xlsx formats with non-standardized sheet names, messy string delimiters (double quotes), and high redundancy (One Big Table format), making direct analysis slow and error-prone.
🏗️ Architecture & Data Journey

The project follows the Medallion Architecture to ensure data quality and lineage:

    Raw Layer: Original .xlsx files as received from the SSP-SP.

    Bronze Layer: Data converted to .parquet. (Transitioned from CSV to Parquet to solve delimiter issues and reduce storage from 127MB to 16MB).

    Silver Layer: TBD

    Gold Layer: TBD

🚀 Key Technical Decisions
1. From CSV to Parquet (The Performance Pivot)

During the exploration phase, I identified that converting .xlsx to .csv was inefficient due to:

    Nested Quotes: Excessive double-quotes in text fields required complex cleaning.

    Storage: The file size doubled (63MB to 127MB).

    Performance: Parquet reduced the size to 16MB and improved DuckDB read speeds by ~45% (from 1.3s to 707ms).
    This was validated using 2025 data. (numbers above are refering this file)

2. Dimensional Modeling (Star Schema)

To enable fast multi-dimensional analysis, the "One Big Table" (OBT) was decomposed into:

    Fact Table: TBD 

    Dimension Tables: TBD 

3. Handling Missing Identities

TBD
🛠️ Tech Stack

    Language: Python 3.12 (Pandas for complex transformations).

    Engine: DuckDB (For lightning-fast SQL processing and Parquet integration).

    Format: Apache Parquet.

    Modeling: TBD

📈 How to Run

TBD

🧠 Lessons Learned

    Excel files are not "read-only" friendly; using openpyxl with specific flags is vital to prevent file corruption.

    Columnar storage (Parquet) is superior for public security data due to high compression and the read speed.

Developed by Arthur Moreno
Data Engineer & Analytics Specialist

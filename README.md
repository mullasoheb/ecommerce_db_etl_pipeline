🛒 E-Commerce ETL Pipeline
-------------------------------------------------------------------------------------------------------------------------
A beginner-friendly Data Engineering ETL pipeline built using Python, Pandas, and MySQL. The project demonstrates how raw E-Commerce data can be extracted from CSV files, cleaned and transformed, and loaded into a relational database for analysis and reporting.

📌 Project Overview
-------------------------------------------------------------------------------------------------------------------------

The E-Commerce Sales ETL Pipeline processes customer, product, and order data through three main stages:

Extract → Transform → Load

Extract: Read E-Commerce data from CSV files using Pandas.
Transform: Clean the data by removing duplicates, handling missing values, and converting data types.
Load: Insert the processed data into MySQL tables.
Report: Use SQL queries to generate basic sales insights.

This project demonstrates a simple end-to-end data pipeline similar to workflows used in Data Engineering.


🏗️ Project Architecture
-------------------------------------------------------------------------------------------------------------------------
             CSV Files
                 │
                 ▼
        ┌─────────────────┐
        │     Extract     │
        │     Pandas      │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │    Transform    │
        │ Data Cleaning   │
        │ Missing Values  │
        │ Duplicate Data  │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │      Load       │
        │ Python + MySQL  │
        └────────┬────────┘
                 │
                 ▼
          ┌─────────────┐
          │   MySQL DB  │
          │  E-Commerce_db  │
          └──────┬──────┘
                 │
                 ▼
        ┌─────────────────┐
        │  SQL Reporting  │
        │ Sales Analysis  │
        └─────────────────┘
        
🛠️ Technologies Used
-------------------------------------------------------------------------------------------------------------------------

Python
Pandas
MySQL
SQL
MySQL Connector/Python
CSV
Git & GitHub


⚙️ Installation & Setup
-------------------------------------------------------------------------------------------------------------------------
1. Clone the Repository
git clone https://github.com/mullasoheb/ecommerce_db_etl_pipeline

Navigate to the project:

cd ecommerce_db_etl_pipeline
2. Install Dependencies
pip install -r requirements.txt
3. Configure MySQL

Open:

config.py

Update your MySQL credentials:

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "ecommerce_db"
}

Important: Do not upload real database passwords or credentials to GitHub. Use environment variables or a .env file for production projects.

4. Create the Database

Open MySQL Workbench and execute:

sql/schema.sql

This creates the E-Commerce_db database and required tables.

▶️ Running the Pipeline
-------------------------------------------------------------------------------------------------------------------------

From the project root directory:

python src/main.py

The pipeline follows:

Extracting Data
       ↓
Transforming Data
       ↓
Loading Data
       ↓
MySQL Database
       ↓
Success
🔍 Verify the Data

After running the pipeline, verify the loaded data using:

USE E-Commerce_db;

SELECT * FROM customers;

SELECT * FROM products;

SELECT * FROM orders;

👨‍💻 Skills Demonstrated
-------------------------------------------------------------------------------------------------------------------------
Python
Pandas
SQL
MySQL
ETL
Data Cleaning
Data Transformation
Database Integration
Data Analysis
Git & GitHub

📄 License
-------------------------------------------------------------------------------------------------------------------------

This project is created for learning and portfolio purposes.

# End-to-End ETL Pipeline using Python & MySQL

## Project Overview
This project demonstrates a complete **ETL (Extract, Transform, Load) pipeline** built with **Python** and **MySQL**. The pipeline extracts raw sales data from CSV files, performs data cleaning and transformation using Python, and loads the clean data into a MySQL database. Finally, SQL analytics queries are used to generate business insights.

## Features
- **Extract:** Read raw CSV data from `data/raw/`
- **Transform:** 
  - Handle missing values
  - Convert data types
  - Compute derived metrics (`total_amount`)
- **Load:** Persist transformed data into MySQL database (`sales` table)
- **Analytics Queries:** 
  - Total revenue by region
  - Total sales per product
  - Highest order amount
  - Orders per day
- **Version Control:** Managed using Git & GitHub

## Folder Structure



etl-sales-pipeline/
│
├── data/
│ ├── raw/ # Raw CSV files (not pushed to GitHub)
│ └── processed/ # Cleaned CSV files (not pushed to GitHub)
│
├── scripts/
│ ├── extract.py # Script to read raw CSV data
│ ├── transform.py # Script to clean and transform data
│ └── load.py # Script to load data into MySQL
│
├── .gitignore
└── README.md


## Installation & Setup
1. Clone the repository:
```bash
git clone https://github.com/RajanRaj13/ETL-Pipeline-Python-SQL.git
cd ETL-Pipeline-Python-SQL


Create a virtual environment (optional):

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install pandas mysql-connector-python


Set up MySQL:

CREATE DATABASE etl_db;
CREATE USER 'etl_user'@'localhost' IDENTIFIED BY 'YourPassword';
GRANT ALL PRIVILEGES ON etl_db.* TO 'etl_user'@'localhost';
FLUSH PRIVILEGES;


Update load.py with your MySQL username/password.

Running the ETL Pipeline

Run transform script:

python3 scripts/transform.py


Load data into MySQL:

python3 scripts/load.py


Run analytics queries in MySQL:

USE etl_db;

-- Total revenue by region
SELECT region, SUM(total_amount) AS revenue
FROM sales
GROUP BY region;

-- Total sales per product
SELECT product, SUM(quantity) AS total_sold
FROM sales
GROUP BY product;

-- Highest order amount
SELECT customer, total_amount
FROM sales
ORDER BY total_amount DESC
LIMIT 1;

-- Orders per day
SELECT order_date, COUNT(*) AS num_orders
FROM sales
GROUP BY order_date;

Skills & Technologies

Languages: Python, SQL

Libraries: Pandas, MySQL Connector

Database: MySQL

Tools: Git, GitHub

Concepts: ETL pipeline, data cleaning, data transformation, SQL analytics

Project Outcome

Fully functional ETL pipeline

Business insights generated using SQL

Resume and portfolio-ready project


---

**Next Step:**  

1. Save this as `README.md` in your **project root folder**.  
2. Commit & push to GitHub:

```bash
git add README.md
git commit -m "Add project README"
git push
# Warehouse Database Project

This repository contains the necessary files to set up a simple data warehouse for sales data, including dimensional modeling (Star Schema), data loading scripts, and analytical queries using SQL features like `GROUPING SETS`, `ROLLUP`, `CUBE`, and `MATERIALIZED VIEWS`.

## Overview

This project aims to demonstrate a basic data warehouse implementation. It involves:

* **Database Schema Definition:** Creating tables for dimensions (Date, Product, Customer Segment) and a fact table (Sales).
* **Data Loading:** A shell script to download sample CSV data and load it into the PostgreSQL database.
* **Analytical Queries:** SQL queries to perform various aggregations and analyses on the sales data using advanced `GROUP BY` clauses and materialized views for performance optimization.

## Files in this Repository

* `cer_db.sql`: This SQL script defines the schema for the `CER_Database` data warehouse. It creates the following tables:
    * `DimDate`: A dimension table for date-related attributes.
    * `DimProduct`: A dimension table for product information.
    * `DimCustomerSegment`: A dimension table for customer segment (city) information.
    * `FactSales`: The fact table storing sales transactions, linked to the dimension tables via foreign keys.

* `query.sql`: This SQL script contains various analytical queries designed to work with the data warehouse:
    * **Grouping Sets Query:** Demonstrates `GROUPING SETS` to get sales totals at different granularities for products (Product ID, Product Type, Product ID only, Product Type only, and overall total).
    * **Rollup Query:** Uses `ROLLUP` to aggregate total sales hierarchically by Year, City, and Product ID, providing sub-totals and grand totals.
    * **Cube Query:** Utilizes `CUBE` to calculate average sales across all possible combinations of Year, City, and Product ID.
    * **Materialized View for Maximum Sales:** Creates a materialized view named `max_sales` to pre-compute and store the maximum sales for each combination of City, Product ID, and Product Type, improving query performance for this specific aggregation. Instructions to refresh the materialized view are also included.

* `loading_data.sh`: This is a Bash shell script responsible for:
    * Creating a `data` directory to store CSV files.
    * Downloading sample `DimDate.csv`, `DimProduct.csv`, `DimCustomerSegment.csv`, and `FactSales.csv` files from a specified cloud storage.
    * Loading the downloaded CSV data into the respective tables in your PostgreSQL `CER_Database` using the `\copy` command.

## How to Run the Project

Follow these steps to set up and run the warehouse database project:

### Prerequisites

* **PostgreSQL:** Ensure you have PostgreSQL installed and running on your system.
* **psql client:** The `psql` command-line client should be accessible from your terminal.
* **curl:** The `curl` command-line tool is required to download the CSV data.
* **Bash:** A Bash-compatible shell (standard on Linux/macOS, available via Git Bash on Windows).

### Step-by-Step Instructions

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Configure Database Connection in `loading_data.sh`:**
    Open the `loading_data.sh` file and modify the following variables with your PostgreSQL database credentials:

    ```bash
    DB_USER="your_username"   # e.g., "postgres"
    DB_HOST="your_host"       # e.g., "localhost" or an IP address
    DB_PORT="your_port_number" # e.g., "5432"
    export PGPASSWORD="your_password" # e.g., "mypassword"
    ```
    **Security Note:** Storing the password directly in the script is not recommended for production environments. For better security, consider using `~/.pgpass` file or environment variables set outside the script.

3.  **Create the Database and Tables:**
    First, create the database, then connect to it and create the tables.

    ```bash
    psql -U your_username -h your_host -p your_port_number -c "CREATE DATABASE CER_Database;"
    psql -U your_username -h your_host -p your_port_number -d CER_Database -f cer_db.sql
    ```
    Replace `your_username`, `your_host`, and `your_port_number` with your actual database credentials.

4.  **Load the Data:**
    Make the `loading_data.sh` script executable and run it to download the CSV files and load them into your database tables.

    ```bash
    chmod +x loading_data.sh
    ./loading_data.sh
    ```

5.  **Run Analytical Queries:**
    After the data is loaded, you can execute the analytical queries defined in `query.sql`.

    ```bash
    psql -U your_username -h your_host -p your_port_number -d CER_Database -f query.sql
    ```
    This will execute all queries in `query.sql` sequentially and display their results in your terminal. You can also copy and paste individual queries into a `psql` session to run them one by one.

6.  **Refreshing Materialized View (Optional):**
    If you make changes to the underlying `FactSales`, `DimProduct`, or `DimCustomerSegment` tables and want the `max_sales` materialized view to reflect those changes, you will need to refresh it:

    ```sql
    REFRESH MATERIALIZED VIEW max_sales;
    ```
    You can run this command directly in a `psql` session or include it in another SQL script.

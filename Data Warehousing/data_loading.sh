#!/bin/bash

# Set environment variables
DB_NAME="CER_Database"
DB_USER="username" # Give your user name here
DB_HOST="host" # Give the host IP address
DB_PORT="port_number" # Give the port number

# Password or use PGPASSWORD variable
export PGPASSWORD="password" # Give your password

# Directory to store the CSVs
DATA_DIR="./data"
mkdir -p "$DATA_DIR"

# Download the CSV files
echo "Downloading CSV files..."
curl -o "$DATA_DIR/DimDate.csv" "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/-omGFpVSWBIZKFSCxUkBwg/DimDate.csv"
curl -o "$DATA_DIR/DimProduct.csv" "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/Y-76u4An3zb5R6HxxFPabA/DimProduct.csv"
curl -o "$DATA_DIR/DimCustomerSegment.csv" "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/h_dnxb8yzQyVjeb8oYnm8A/DimCustomerSegment.csv"
curl -o "$DATA_DIR/FactSales.csv" "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/a8kTjzvpdqzOp46ODatyAA/FactSales.csv"

# Load CSVs into the tables
echo "Loading CSV data into PostgreSQL..."

psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "\copy DimDate FROM '$DATA_DIR/DimDate.csv' DELIMITER ',' CSV HEADER;"
psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "\copy DimProduct FROM '$DATA_DIR/DimProduct.csv' DELIMITER ',' CSV HEADER;"
psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "\copy DimCustomerSegment FROM '$DATA_DIR/DimCustomerSegment.csv' DELIMITER ',' CSV HEADER;"
psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -c "\copy FactSales FROM '$DATA_DIR/FactSales.csv' DELIMITER ',' CSV HEADER;"

echo "All data loaded successfully into $DB_NAME"

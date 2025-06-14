#!/bin/bash

# Step 1: Start MySQL server
echo "Starting MySQL server..."
# For Ubuntu/Debian
sudo service mysql start
# For macOS (Homebrew)
# brew services start mysql

# Step 2: Run SQL file to create database and table
echo "Setting up database and table from setup_mysql.sql..."
mysql -u root -p < setup_mysql.sql

echo "MySQL setup complete."

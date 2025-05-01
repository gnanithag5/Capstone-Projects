# Sales Database

## Overview

This project automates the execution of SQL scripts on a PostgreSQL database. It includes two SQL files: one to create the schema and the other to insert a large dataset. The `main.py` script connects to the PostgreSQL database and executes both SQL scripts sequentially. This setup proves useful for initializing or resetting a database environment with a predefined structure and data.

## Repository Structure

* `main.py`: Python script responsible for connecting to the PostgreSQL database and running the SQL files.
* `GeneratedScript.sql`: Contains SQL statements to define and create the required database schema (tables, constraints, etc.).
* `CoffeeData.sql`: Contains SQL insert statements or `COPY` commands to populate the database with a large volume of data.
* `requirements.txt`: Lists the Python dependency needed to connect and interact with PostgreSQL (`psycopg2-binary`).

## How It Works

The user begins by ensuring that PostgreSQL is running and accessible with the correct database credentials. After setting up the environment and installing the required Python packages (using `pip install -r requirements.txt`), the user runs the `main.py` script. This script establishes a connection to the specified PostgreSQL database and executes the `create_schema.sql` file to build the database structure. Once the schema is in place, the script proceeds to execute the `GeneratedScript.sql` file to populate the tables with data. This process efficiently automates database initialization in development or testing environments.

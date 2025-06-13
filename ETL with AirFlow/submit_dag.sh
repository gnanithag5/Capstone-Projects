#!/bin/bash

# --------------------------------------------
# Airflow DAG Submission Script
# --------------------------------------------

# Step 1: Set AIRFLOW_HOME (adjust this if your setup differs)
export AIRFLOW_HOME=~/airflow
echo "AIRFLOW_HOME is set to $AIRFLOW_HOME"

# Step 2: Create staging directory inside Airflow
echo "Creating staging directory..."
mkdir -p $AIRFLOW_HOME/dags/python_etl/staging
chmod -R 777 $AIRFLOW_HOME/dags/python_etl

# Step 3: Copy your DAG file into the Airflow dags folder
echo "Copying DAG file ETL_toll_data.py..."
cp ./dags/ETL_toll_data.py $AIRFLOW_HOME/dags/

# Step 4: List and verify DAGs
echo "Listing all DAGs..."
airflow dags list

echo "Verifying DAG 'etl_toll_data_pipeline' exists..."
airflow dags list | grep "etl_toll_data_pipeline"

# Step 5: List tasks
echo "Listing tasks in 'etl_toll_data_pipeline'..."
airflow tasks list etl_toll_data_pipeline

# Step 6: Trigger the DAG manually
echo "Triggering DAG..."
airflow dags trigger etl_toll_data_pipeline

echo "DAG submitted and triggered. Access the Airflow UI at http://localhost:8080"

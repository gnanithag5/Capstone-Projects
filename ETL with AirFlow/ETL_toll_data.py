from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import requests
import tarfile
import pandas as pd

# Use environment variable for Airflow home
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow")
STAGING_DIR = os.path.join(AIRFLOW_HOME, "dags", "python_etl", "staging")

# Ensure staging directory exists
os.makedirs(STAGING_DIR, exist_ok=True)

# Define default_args
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Task 1: Download the dataset
def download_dataset_func():
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz"
    dest_path = os.path.join(STAGING_DIR, "tolldata.tgz")
    response = requests.get(url)
    with open(dest_path, "wb") as f:
        f.write(response.content)
    print(f"Downloaded dataset to: {dest_path}")

# Task 2: Unzip the dataset
def unzip_data_func():
    tar_path = os.path.join(STAGING_DIR, "tolldata.tgz")
    with tarfile.open(tar_path) as tar:
        tar.extractall(path=STAGING_DIR)
    print(f"Extracted tar file to: {STAGING_DIR}")

# Task 3: Extract data from CSV
def extract_data_from_csv_func():
    df = pd.read_csv(os.path.join(STAGING_DIR, "vehicle-data.csv"))
    df.iloc[:, 0:4].to_csv(os.path.join(STAGING_DIR, "csv_data.csv"), index=False)

# Task 4: Extract data from TSV
def extract_data_from_tsv_func():
    df = pd.read_csv(os.path.join(STAGING_DIR, "tollplaza-data.tsv"), sep='\t')
    df.iloc[:, 4:7].to_csv(os.path.join(STAGING_DIR, "tsv_data.csv"), index=False)

# Task 5: Extract data from fixed width
def extract_data_from_fixed_width_func():
    input_file = os.path.join(STAGING_DIR, "payment-data.txt")
    output_file = os.path.join(STAGING_DIR, "fixed_width_data.csv")
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            selected = line[58:61] + ',' + line[62:67].strip()
            f_out.write(selected + '\n')

# Task 6: Consolidate data
def consolidate_data_func():
    df_csv = pd.read_csv(os.path.join(STAGING_DIR, "csv_data.csv"))
    df_tsv = pd.read_csv(os.path.join(STAGING_DIR, "tsv_data.csv"))
    df_fixed = pd.read_csv(os.path.join(STAGING_DIR, "fixed_width_data.csv"))
    final_df = pd.concat([df_csv, df_tsv, df_fixed], axis=1)
    final_df.to_csv(os.path.join(STAGING_DIR, "extracted_data.csv"), index=False)

# Task 7: Transform data
def transform_data_func():
    df = pd.read_csv(os.path.join(STAGING_DIR, "extracted_data.csv"))
    df.iloc[:, 3] = df.iloc[:, 3].str.upper()
    df.to_csv(os.path.join(STAGING_DIR, "transformed_data.csv"), index=False)

# Define DAG
with DAG(
    dag_id='etl_toll_data_pipeline',
    default_args=default_args,
    description='ETL pipeline for toll data using PythonOperator',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    download_dataset = PythonOperator(
        task_id='download_dataset',
        python_callable=download_dataset_func
    )

    unzip_data = PythonOperator(
        task_id='unzip_data',
        python_callable=unzip_data_func
    )

    extract_csv = PythonOperator(
        task_id='extract_data_from_csv',
        python_callable=extract_data_from_csv_func
    )

    extract_tsv = PythonOperator(
        task_id='extract_data_from_tsv',
        python_callable=extract_data_from_tsv_func
    )

    extract_fixed = PythonOperator(
        task_id='extract_data_from_fixed_width',
        python_callable=extract_data_from_fixed_width_func
    )

    consolidate_data = PythonOperator(
        task_id='consolidate_data',
        python_callable=consolidate_data_func
    )

    transform_data = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data_func
    )

    # Set dependencies
    download_dataset >> unzip_data >> extract_csv >> extract_tsv >> extract_fixed >> consolidate_data >> transform_data

from bs4 import BeautifulSoup

import requests

import pandas as pd

import numpy as np

import sqlite3

from datetime import datetime

 

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'

table_attribs = ["Name", "MC_USD_Billion"]

db_name = 'Banks.db'

table_name = 'Largest_Banks'

csv_path = './Largest_banks_data.csv'

exchange_rate_path = 'exchange_rate.csv'

 

# === Step 1: Logging function ===

def log_progress(message):

    timestamp_format = '%Y-%h-%d-%H:%M:%S'

    now = datetime.now()

    timestamp = now.strftime(timestamp_format)

    with open("./code_log.txt", "a") as f:

        f.write(f"{timestamp} : {message}\n")

 

# === Step 2: Extraction function ===

def extract(url):

    page = requests.get(url).text

    soup = BeautifulSoup(page, 'html.parser')

    table = soup.find_all('table', {'class': 'wikitable'})[0]  # First table

    rows = table.find_all('tr')[1:]  # Skip header

    data = []

    for row in rows:

        cols = row.find_all('td')

        if len(cols) >= 3:

            name = cols[1].get_text(strip=True)

            market_cap = cols[2].get_text(strip=True).replace('\n', '').replace(',', '')

            try:

                market_cap = float(market_cap)

                data.append([name, market_cap])

            except:

                continue

    df = pd.DataFrame(data, columns=table_attribs)

    return df

 

# === Step 3: Transformation function ===

def transform(df, exchange_rate_path):

    exchange_df = pd.read_csv(exchange_rate_path)

    exchange_rate = exchange_df.set_index('Currency').to_dict()['Rate']

    df['MC_USD_Billion'] = df['MC_USD_Billion'].astype(float)

    df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df['MC_USD_Billion']]

    df['MC_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in df['MC_USD_Billion']]

    df['MC_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in df['MC_USD_Billion']]

    return df

 

# === MAIN SCRIPT EXECUTION ===

 

log_progress("Preliminaries complete. Initiating ETL process")

 

df = extract(url)

log_progress("Data extraction complete. Initiating Transformation process")

 

df = transform(df, exchange_rate_path)

log_progress("Data transformation complete. Initiating Loading process")

 

# Print to verify (optional)

print(df)

print("5th largest bank MC in EUR:", df['MC_EUR_Billion'][4])

 

def load_to_csv(df, csv_path):

    df.to_csv(csv_path)

    log_progress("Data saved to CSV file")

 

def load_to_db(df, db_name, table_name):

    conn = sqlite3.connect(db_name)

    log_progress("SQL Connection initiated")

    df.to_sql(table_name, conn, if_exists='replace', index=False)

    log_progress("Data loaded to Database as a table, Executing queries")

    return conn

 

conn = load_to_db(df, db_name, table_name)

 

def run_query(query, conn):

    print(f"\nQuery: {query}")

    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:

        print(row)

 

# Queries

run_query(f"SELECT * FROM {table_name}", conn)

run_query(f"SELECT AVG(MC_GBP_Billion) FROM {table_name}", conn)

run_query(f"SELECT Name FROM {table_name} LIMIT 5", conn)

 

log_progress("Process Complete")

conn.close()

log_progress("Server Connection closed")
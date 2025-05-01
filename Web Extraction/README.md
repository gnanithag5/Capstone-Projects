# Web Extraction
---
## Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline to fetch data from a web source, transform it using real-world currency exchange rates, and store the final data into a SQLite database and CSV file. The data source is a Wikipedia page listing the world's largest banks by market capitalization.

The main objectives are:

* Web scraping the largest banks data using BeautifulSoup.
* Data transformation using current exchange rates from USD to GBP, EUR, and INR.
* Storing and querying the data using SQLite.
* Logging each step of the ETL process.

## Contents in the Repository

`etl_script.py`: Main Python script containing the ETL pipeline logic                      
`exchange_rate.csv`: CSV file with exchange rates (USD to GBP, EUR, INR)                       
`Banks.db`: SQLite database file storing the final data                                
`code_log.txt`: Log file recording ETL process steps with timestamps                       

## How It Works

**Step-by-Step ETL Process:**

**Extraction**

* The script scrapes a table from a Wikipedia archive link containing the largest banks by market capitalization.

**Transformation**

* Market capitalizations (in USD) are converted to other currencies (GBP, EUR, INR) using exchange rates provided in `exchange_rate.csv`.
* The script adds new columns for each converted currency and rounds values to two decimal places.

**Loading**

* The transformed data is stored in:
    * A CSV file named `Largest_banks_data.csv`.
    * A SQLite database named `Banks.db`, with a table named `Largest_Banks`.

**Logging**

* Each major step in the ETL process is logged into `code_log.txt` with a timestamp.

**Querying**

* A few SQL queries are executed to validate data insertion, fetch basic stats (e.g., average market cap in GBP), and preview the first few rows.

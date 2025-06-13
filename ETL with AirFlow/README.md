# Toll Data ETL Pipeline with Apache Airflow

This project automates the ETL (Extract, Transform, Load) process for toll data collected from various highway operators. The data, arriving in multiple formats, is consolidated into a clean CSV file for analysis.

---

## Features

* **Downloads** a `.tgz` dataset from a specified URL.
* **Extracts and parses** data from:
    * `.csv` files: vehicle data
    * `.tsv` files: toll plaza information
    * Fixed-width `.txt` files: payment records
* **Consolidates** all extracted data into a single, unified CSV file.
* **Capitalizes** vehicle types within the final output file for consistency.

---

## Getting Started

Follow these instructions to get your ETL pipeline up and running.

### Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8+**
* **Apache Airflow**: Install it using the provided `requirements.txt` file (details below).

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/yourusername/toll-data-etl-airflow.git](https://github.com/yourusername/toll-data-etl-airflow.git)
    cd toll-data-etl-airflow
    ```

2.  **Set up a virtual environment** (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Start Apache Airflow:**

    ```bash
    airflow db init
    airflow webserver --port 8080
    airflow scheduler
    ```

5.  **Submit the DAG** (in a new terminal while Airflow components are running):

    ```bash
    ./scripts/submitdag.sh
    ```

---

## Accessing the Airflow UI

Once Airflow is running, you can access the web interface in your browser:

[http://localhost:8080](http://localhost:8080)

# Historical Weather Forecast Accuracy Analysis Project

This project demonstrates a simplified **Extract, Transform, Load (ETL)** process applied to weather data for forecast accuracy analysis. It involves:

* **Extract:** Downloading raw synthetic weather data using Bash scripts.
* **Transform:** Parsing the downloaded data to extract relevant observed and forecasted temperatures. Calculating daily forecast accuracy and categorizing it into different labels (excellent, good, fair, poor).
* **Load:** Storing the processed daily weather data into a log file (`rx_poc.log`) and the historical forecast accuracy data into a tab-separated file (`historical_fc_accuracy.tsv`).

Furthermore, the project includes the generation of weekly statistics, providing a higher-level summary of the forecast performance over time.

## Project Breakdown

The project is divided into the following key exercises:

1.  **Initialize Weather Report Log File:** Setting up a log file (`rx_poc.log`) to store daily weather data, including observed and forecasted temperatures.
2.  **Download Raw Weather Data:** Downloading synthetic weather data containing both forecasted and observed temperatures.
3.  **Extract and Load Data:** Parsing the downloaded data to extract relevant forecast and observed temperatures for further processing.
4.  **Schedule Bash Script (`rx_poc.sh`):** Scheduling a script to run daily at noon local time to automatically gather the latest weather data.
5.  **Create Script for Historical Forecasting Accuracy (`fc_accuracy.sh`):** Developing a script to calculate the daily forecast accuracy by comparing forecasted and observed temperatures. The accuracy is categorized into different ranges (excellent, good, fair, poor), and the results are appended to a historical report file (`historical_fc_accuracy.tsv`).
6.  **Generate Weekly Statistics of Historical Forecasting Accuracy (`weekly_stats.sh`):** Analyzing a synthetic historical forecasting accuracy dataset to extract the last 7 days of data, calculate the minimum and maximum absolute forecast errors, and display these weekly statistics.

## Scripts

The following Bash scripts are part of this project:

* **`rx_poc.sh`**: A shell script designed to fetch weather data and calculate the daily forecast accuracy. This script is intended to be scheduled for daily execution.
* **`fc_accuracy.sh`**: A script responsible for computing the forecasting accuracy for a single day based on available data and appending the results to the historical log file (`historical_fc_accuracy.tsv`).
* **`weekly_stats.sh`**: A script that processes historical forecast accuracy data to calculate and display weekly statistics, specifically the minimum and maximum absolute errors observed in the forecasts over the past week.

## Data

The project utilizes the following synthetic dataset for testing and analysis:

* **`synthetic_historical_fc_accuracy.tsv`**: A tab-separated values file containing historical weather forecast accuracy data spanning multiple days. This dataset is used to test the `weekly_stats.sh` script. You can download this file using the following command:
    ```bash
    wget [https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-LX0117EN-Coursera/labs/synthetic_historical_fc_accuracy.tsv](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-LX0117EN-Coursera/labs/synthetic_historical_fc_accuracy.tsv)
    ```

## Getting Started

To get started with this project, you will need to:

1.  Create the initial weather report log file:
    ```bash
    touch rx_poc.log
    ```

2.  Add a header to the `rx_poc.log` file with the following tab-separated column names: `year`, `month`, `day`, `obs_temp`, `fc_temp`. You can achieve this using:
    ```bash
    header=$(echo -e "year\tmonth\tday\tobs_temp\tfc_temp")
    echo "$header" > rx_poc.log
    ```
    or more directly:
    ```bash
    echo -e "year\tmonth\tday\tobs_temp\tfc_temp" > rx_poc.log
    ```

Further steps will involve downloading weather data, implementing the `rx_poc.sh` and `fc_accuracy.sh` scripts, scheduling the daily execution, and finally developing the `weekly_stats.sh` script to analyze the historical accuracy data.


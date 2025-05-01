# Historical Weather Forecast Accuracy Analysis Project

## Overview

This project demonstrates a simplified **Extract, Transform, Load (ETL)** process applied to weather data for forecast accuracy analysis. It involves:

* **Extract:** Downloading raw synthetic weather data using Bash scripts.
* **Transform:** Parsing the downloaded data to extract relevant observed and forecasted temperatures. Calculating daily forecast accuracy and categorizing it into different labels (excellent, good, fair, poor).
* **Load:** Storing the processed daily weather data into a log file (`rx_poc.log`) and the historical forecast accuracy data into a tab-separated file (`historical_fc_accuracy.tsv`).

Furthermore, the project includes the generation of weekly statistics, providing a higher-level summary of the forecast performance over time.

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

## Scheduling the Daily Weather Data Collection (`rx_poc.sh`)

To automate the daily collection of weather data using the `rx_poc.sh` script, you can use a scheduling tool like `cron` on Linux or macOS.

**To set up a cron job to run `rx_poc.sh` daily at noon (12:00 PM) local time, you can add the following line to your crontab:**

```cron
0 12 * * * /path/to/your/rx_poc.sh

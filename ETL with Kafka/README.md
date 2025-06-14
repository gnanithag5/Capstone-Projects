# Toll Traffic Data Pipeline

This project simulates toll booth vehicle traffic using a **Kafka-based streaming data pipeline** and stores that data into a **MySQL database**. It's designed for local execution and structured for easy deployment on GitHub.

---

### Project Overview

This project includes the following components:

* **Kafka Producer**: A Python script (`toll_traffic_generator.py`) that simulates vehicles passing through toll booths, publishing traffic data as events.
* **Kafka Consumer**: A Python script (`streaming-data-reader.py`) that listens to the Kafka topic and inserts the received traffic records into a MySQL database.
* **MySQL Database**: Used for persistent storage of toll data, including `timestamp`, `vehicle ID`, `type`, and `plaza ID`.
* **Shell Scripts**: Automation scripts to set up Kafka, MySQL, create Kafka topics, and manage Python dependencies.
* **Orchestrator**: The `main.py` script, which automates the launch of both the Kafka producer and consumer after confirming Kafka is fully operational.



### Setup & Run Instructions

Follow these steps to set up and run the toll traffic data pipeline locally:

**1. Clone the repository**

First, clone the project repository to your local machine and navigate into its directory:


**2. Install Python dependencies**

This script will create a Python virtual environment and install all necessary packages listed in requirements.txt:

./dependencies.sh


**3. Start MySQL and set up the database**

This script will start your MySQL service (if not already running) and execute setup_mysql.sql to create the tolldata database and the livetolldata table:

./setup_mysql.sh


**4. Setup and start Kafka (keep terminal open)**

This script downloads and configures Kafka, then starts the Kafka server in KRaft mode. This process can take a moment.

./setup_kafka.sh

⚠️ Important: Keep this terminal window open and running. Kafka needs to remain active for the pipeline to function.

**5. In a new terminal, create the Kafka topic**

Open a new terminal window and run this script to create the Kafka topic named toll that the producer will publish to and the consumer will read from:

./create_kafka_topic.sh

**6. Run the pipeline orchestrator**

In a third terminal window, execute the main.py orchestrator script. This script will:

Wait for Kafka to be fully ready.
Launch the Kafka consumer in the background.
Launch the Kafka producer in the foreground, starting the traffic simulation.

python3 main.py


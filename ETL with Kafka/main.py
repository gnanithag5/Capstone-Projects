import subprocess
import threading
import time
import os

# Constants
KAFKA_DIR = "kafka_2.12-3.7.0"
TOPIC_CREATOR = "./create_kafka_topic.sh"
PRODUCER = "toll_traffic_generator.py"
CONSUMER = "streaming-data-reader.py"

def run_producer():
    print("\n[INFO] Starting Traffic Simulator (Producer)...")
    subprocess.run(["python3", PRODUCER])

def run_consumer():
    print("\n[INFO] Starting Kafka Consumer...")
    subprocess.run(["python3", CONSUMER])

def main():
    print("========== TOLL DATA PIPELINE LAUNCHER ==========\n")

    # Step 1: Prompt for Kafka server status
    print("[INFO] Make sure Kafka server is running:")
    print(f"  {KAFKA_DIR}/bin/kafka-server-start.sh config/kraft/server.properties")
    input("[WAITING] Press Enter after Kafka server has started...")

    # Step 2: Create Kafka topic
    print("\n[INFO] Creating Kafka topic...")
    subprocess.run([TOPIC_CREATOR], shell=True)

    # Step 3: Start consumer in a background thread
    consumer_thread = threading.Thread(target=run_consumer)
    consumer_thread.start()

    # Step 4: Delay to ensure consumer is ready
    time.sleep(3)

    # Step 5: Start producer in main thread
    run_producer()

    # Wait for consumer thread to finish (optional)
    consumer_thread.join()

    print("\n[INFO] Pipeline execution complete.")

if __name__ == "__main__":
    main()

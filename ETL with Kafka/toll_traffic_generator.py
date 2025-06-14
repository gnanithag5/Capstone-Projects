"""
Toll Traffic Simulator
"""
from time import sleep, time, ctime
from random import random, randint, choice
from kafka import KafkaProducer

# Connect to Kafka running locally
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Kafka topic name
TOPIC = 'toll'

# Weighted vehicle types
VEHICLE_TYPES = (
    "car", "car", "car", "car", "car", "car", "car", "car",
    "car", "car", "car", "truck", "truck", "truck",
    "truck", "van", "van"
)

# Send 100,000 simulated records
for _ in range(100000):
    vehicle_id = randint(10000, 10000000)
    vehicle_type = choice(VEHICLE_TYPES)
    now = ctime(time())
    plaza_id = randint(4000, 4010)

    message = f"{now},{vehicle_id},{vehicle_type},{plaza_id}"
    print(f"A {vehicle_type} has passed toll plaza {plaza_id} at {now}.")
    producer.send(TOPIC, message.encode("utf-8"))

    # Simulate delay
    sleep(random() * 2)

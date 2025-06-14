"""
Streaming data consumer
"""
from datetime import datetime
from kafka import KafkaConsumer
import mysql.connector

# Configuration section
TOPIC = 'toll'
DATABASE = 'tolldata'
USERNAME = 'root'
PASSWORD = 'your_password_here'  # <- Replace this with your actual password

print("Connecting to the database")
try:
    connection = mysql.connector.connect(
        host='localhost',         # Assuming local MySQL
        database=DATABASE,
        user=USERNAME,
        password=PASSWORD
    )
except Exception:
    print("Could not connect to database. Please check credentials")
else:
    print("Connected to database")

cursor = connection.cursor()

print("Connecting to Kafka")
consumer = KafkaConsumer(TOPIC, bootstrap_servers='localhost:9092')
print("Connected to Kafka")
print(f"Reading messages from the topic {TOPIC}")

for msg in consumer:
    message = msg.value.decode("utf-8")
    try:
        timestamp, vehicle_id, vehicle_type, plaza_id = message.split(",")

        # Format timestamp
        dateobj = datetime.strptime(timestamp, '%a %b %d %H:%M:%S %Y')
        timestamp = dateobj.strftime("%Y-%m-%d %H:%M:%S")

        # Insert into MySQL
        sql = "INSERT INTO livetolldata (timestamp, vehicle_id, vehicle_type, toll_plaza_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (timestamp, vehicle_id, vehicle_type, plaza_id))
        connection.commit()
        print(f"A {vehicle_type} was inserted into the database")
    except Exception as e:
        print("Error inserting data:", e)

connection.close()

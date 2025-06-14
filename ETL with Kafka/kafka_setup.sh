#!/bin/bash

# Set Kafka version and download URL
KAFKA_VERSION="3.7.0"
KAFKA_URL="https://archive.apache.org/dist/kafka/3.7.0/kafka_2.12-${KAFKA_VERSION}.tgz"
KAFKA_DIR="kafka_2.12-${KAFKA_VERSION}"

# Step 1: Download Kafka
echo "Downloading Kafka version ${KAFKA_VERSION}..."
wget -q ${KAFKA_URL} -O kafka_${KAFKA_VERSION}.tgz

# Step 2: Extract Kafka
echo "Extracting Kafka..."
tar -xzf kafka_${KAFKA_VERSION}.tgz

# Step 3: Move into Kafka directory
cd ${KAFKA_DIR} || exit

# Step 4: Generate a cluster UUID
echo "Generating Kafka cluster UUID..."
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

# Step 5: Format Kafka storage (configure KRaft)
echo "Configuring Kafka storage..."
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties

# Step 6: Start Kafka server
echo "Starting Kafka server..."
bin/kafka-server-start.sh config/kraft/server.properties

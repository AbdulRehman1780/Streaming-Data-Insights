#!/bin/bash

# Function to start Kafka components
function start_kafka() {
    echo "Starting Kafka components..."
    # Start Zookeeper
    zookeeper-server-start.sh config/zookeeper.properties > /dev/null 2>&1 &
    # Start Kafka server
    kafka-server-start.sh config/server.properties > /dev/null 2>&1 &
    # Add more commands to start other Kafka components if needed
}

# Function to start Kafka producer
function start_producer() {
    echo "Starting Kafka producer..."
    python producer.py > /dev/null 2>&1 &
}

# Function to start Kafka consumers
function start_consumers() {
    echo "Starting Kafka consumers..."
    # Start Consumer 1
    python consumer_1.py > /dev/null 2>&1 &
    # Start Consumer 2
    python consumer_2.py > /dev/null 2>&1 &
    # Start Consumer 3
    python consumer_3.py > /dev/null 2>&1 &
}

# Main function
function main() {
    start_kafka
    start_producer
    start_consumers
}

# Execute main function
main

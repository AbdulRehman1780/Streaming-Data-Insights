from kafka import KafkaProducer
import json
import time

def produce_data(producer, input_file, topic):
    with open(input_file, 'r') as file:
        for line in file:
            data = json.loads(line)
            producer.send(topic, json.dumps(data).encode('utf-8'))
            time.sleep(1)  # Simulating real-time streaming
        producer.flush()

def main():
    bootstrap_servers = 'localhost:9092'
    input_file = 'preprocessed_amazon_dataset.json'
    topic = 'amazon_data'
    
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    produce_data(producer, input_file, topic)

if __name__ == "__main__":
    main()

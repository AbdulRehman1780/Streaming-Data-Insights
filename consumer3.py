from kafka import KafkaConsumer
from pymongo import MongoClient
from collections import Counter
import matplotlib.pyplot as plt

# MongoDB Configuration
mongo_host = 'localhost'
mongo_port = 27017
mongo_db_name = 'streaming_data_db'
mongo_collection_name = 'innovative_results'

# Function to connect to MongoDB
def connect_to_mongodb():
    client = MongoClient(mongo_host, mongo_port)
    db = client[mongo_db_name]
    collection = db[mongo_collection_name]
    return collection

# Function to store data in MongoDB
def store_data_in_mongodb(collection, data):
    collection.insert_one(data)

# Function to perform unique analysis and print real-time insights or visualizations
def innovative_approach(consumer, topic):
    collection = connect_to_mongodb()
    frequent_item_counts = Counter()
    total_transactions = 0
    
    for message in consumer:
        transaction = message.value.decode('utf-8').split(',')
        
        # Unique analysis: Count occurrences of each item in real-time
        frequent_item_counts.update(transaction)
        total_transactions += 1
        
        # Update insights or visualizations
        if total_transactions % 100 == 0:  # Print insights or visualizations periodically
            print(f"Total transactions processed: {total_transactions}")
            print("Top 5 most frequent items:")
            for item, count in frequent_item_counts.most_common(5):
                print(f"- {item}: {count} occurrences")
            
            # Visualize frequent item occurrences
            items, counts = zip(*frequent_item_counts.most_common())
            plt.bar(items, counts)
            plt.xlabel('Item')
            plt.ylabel('Occurrences')
            plt.title('Frequent Item Occurrences')
            plt.xticks(rotation=45)
            plt.show()
            
            # Store insights or visualizations in MongoDB
            data = {
                'total_transactions': total_transactions,
                'top_5_frequent_items': {item: count for item, count in frequent_item_counts.most_common(5)}
            }
            store_data_in_mongodb(collection, data)

def main():
    bootstrap_servers = 'localhost:9092'
    topic = 'amazon_data'
    
    consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers, group_id='group3')
    innovative_approach(consumer, topic)

if __name__ == "__main__":
    main()

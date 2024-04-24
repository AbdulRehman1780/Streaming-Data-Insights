import json
import os
import pandas as pd
from tqdm import tqdm
import time
from kafka import KafkaProducer, KafkaConsumer

# sampling the dataset to 15 gb

def sample_json(input_file, output_file, target_size_gb, filter_key='also_buy'):
    target_size_bytes= target_size_gb * 1024**3
    current_size_bytes = 0
    
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding= 'utf-8') as outfile:
        for line in tqdm(infile):
            record = json.loads(line)
            if record.get(filter_key):
                outfile.write(json.dumps(record) + '\n')
                current_size_bytes += len(line.encode('utf-8'))
                
            if current_size_bytes >= target_size_bytes:
                break
                
    print(f"Finished sampling. output size: {current_size_bytes/ 1024**3:.2f} GB")

# pre-processing

def load_sampled_dataset(input_file):
    sampled_data = pd.read_json(input_file, lines=True)
    return sampled_data

def preprocess_data(data):
    data = data.drop_duplicates()
    data = data.dropna()
    return data

def generate_preprocessed_json(data, output_file):
    data.to_json(output_file, orient='records', lines=True)
    print(f"Preprocessed data saved to: {output_file}")

def real_time_preprocessing(input_file, output_file, interval=60):
    while True:
        sampled_data = load_sampled_dataset(input_file)
        preprocessed_data = preprocess_data(sampled_data)
        generate_preprocessed_json(preprocessed_data, output_file)
        time.sleep(interval)

input_file = 'sampled_amazon_dataset.json'
output_file = 'preprocessed_amazon_dataset.json'

real_time_preprocessing(input_file, output_file)
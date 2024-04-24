# Streaming-Data-Insights

## Overview

This project demonstrates how to perform streaming data analysis using Apache Kafka for message streaming and MongoDB for storing results. The project focuses on frequent itemset mining on Amazon metadata in a streaming environment.

## Approach

1. **Sampling the Dataset**: Initially, the dataset is sampled to a manageable size (15 GB) using a custom Python script. This sampled dataset is used for subsequent analysis.

2. **Preprocessing**: The sampled dataset is preprocessed to clean and format it for analysis. Duplicate records are removed, and missing values are handled.

3. **Real-time Preprocessing**: A real-time preprocessing function is implemented to continuously load the sampled dataset, preprocess it, and save the preprocessed data to a JSON file at regular intervals. This ensures that the data remains up-to-date and ready for analysis.

4. **Streaming Pipeline Setup**: A Kafka producer application is developed to stream the preprocessed data in real-time. Three consumer applications are created to subscribe to the producer's data stream.

5. **Frequent Itemset Mining**: In the context of this project, frequent itemset mining refers to the process of identifying sets of items that frequently co-occur together in the dataset. This is a fundamental task in data mining and is often used in market basket analysis, recommendation systems, and other data-driven applications.

### Consumer 1 and Consumer 2:
Two of the consumer applications (Consumer 1 and Consumer 2) are responsible for implementing well-known algorithms for frequent itemset mining:

1. **Consumer 1 (Apriori Algorithm)**: This consumer implements the Apriori algorithm, a classic algorithm for mining frequent itemsets. The Apriori algorithm uses a bottom-up approach to generate candidate itemsets and prune infrequent ones based on the downward closure property. It iteratively generates itemsets of increasing sizes and efficiently prunes the search space, making it suitable for large datasets.

2. **Consumer 2 (PCY Algorithm)**: This consumer implements the PCY (Park-Chen-Yu) algorithm, another popular algorithm for frequent itemset mining. The PCY algorithm improves upon the Apriori algorithm by introducing a hash-based technique to reduce the number of candidate itemsets. It uses a hash table to count item pairs and filters out infrequent item pairs before generating candidate itemsets, thereby reducing memory requirements and speeding up the mining process.

### Consumer 3 (Innovative Approach):
The third consumer application (Consumer 3) takes a different approach to frequent itemset mining:

3. **Consumer 3 (Innovative Approach)**: Consumer 3 implements a custom approach for mining frequent itemsets and providing unique insights and real-time visualizations. Instead of using traditional algorithms like Apriori or PCY, Consumer 3 leverages streaming data characteristics and applies innovative techniques for data analysis. This could involve techniques such as:

   - **Custom Algorithms**: Developing novel algorithms tailored to the specific characteristics of the dataset or the streaming environment.
   - **Optimization Techniques**: Exploring optimization techniques such as approximation, incremental processing, or online algorithms to enhance performance and accuracy.
   - **Real-time Insights and Visualizations**: Generating real-time insights and visualizations that showcase unique patterns or trends in the data. This could include interactive dashboards, anomaly detection, trend analysis, or sentiment analysis.
   
Consumer 3 aims to go beyond traditional frequent itemset mining approaches and provide valuable insights and actionable information from the streaming data in innovative ways. It focuses on creativity and adaptability to extract meaningful patterns and knowledge from the dataset in real-time.

By implementing this diverse set of consumer applications, the project aims to demonstrate different approaches to frequent itemset mining and highlight the versatility of streaming data analysis techniques.


6. **Database Integration**: Each consumer is modified to connect to MongoDB and store the results. MongoDB is chosen for its flexibility and scalability, making it suitable for streaming data analysis.

## Why MongoDB?

MongoDB is chosen as the database for storing results due to its non-relational nature, which fits well with the schema-less nature of streaming data. It provides flexibility in data modeling and scalability for handling large volumes of data.

## Dependencies

- Python 3.x
- Kafka (for message streaming)
- MongoDB (for storing results)
- Required Python libraries (kafka-python, pandas, tqdm, pymongo, matplotlib)

## Usage

1. Install the required dependencies.
2. Configure Kafka and MongoDB as per your setup.
3. Run the sampling script to sample the dataset.
4. Preprocess the sampled dataset using the provided scripts.
5. Run the Kafka producer and consumer applications.
6. Monitor the MongoDB collections for storing the results.

## Contributors

- Abdul Rehman 21i-1780
- Ramish Shakeel 21i-1363
- Musa Yaseen 21-2653

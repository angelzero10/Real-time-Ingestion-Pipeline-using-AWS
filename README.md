
# Real-time Ingestion Pipeline Project

## Overview

This project implements a real-time ingestion pipeline for sensor data collection using AWS managed services. The primary goal is to process a dataset of recommended fishing rivers and streams, stream the data to AWS Kinesis, and aggregate it by county in real-time, storing the results in DynamoDB.

## Architecture

The pipeline consists of:
- **Data Producer**: A Python application that reads data from a CSV file, adds a timestamp, and streams it to AWS Kinesis Data Streams.
- **AWS Kinesis Data Streams**: Captures and transports the streaming data in real-time.
- **AWS Lambda Function**: Processes data from Kinesis in batches and aggregates the count of records for each county within the batch.
- **AWS DynamoDB**: Stores the aggregated counts, with each entry representing the count of records per county for the specific batch of data.

## Components

- **Data Input**: The dataset is a CSV file that contains information about recommended fishing rivers and streams.
- **AWS Kinesis**: Data is streamed to AWS Kinesis Data Streams from the CSV file.
- **AWS Lambda**: The Lambda function processes each batch, aggregates the count of records per county, and writes the results to DynamoDB.
- **AWS DynamoDB**: A NoSQL database that stores the aggregated count for each county.

## How It Works

1. **Data Streaming**: A Python application streams data from the CSV file into AWS Kinesis Data Streams at a rate of at least 10 rows per second.
2. **Batch Processing**: The Lambda function is triggered by new records in Kinesis. It processes the batch, aggregates the number of records for each county, and writes the result to DynamoDB.
3. **Storage**: The result is stored in DynamoDB with the structure:
   - County
   - Timestamp
   - Count (number of records for the county in the current batch)

## Setup and Usage

### Prerequisites

- AWS account with sufficient permissions to create and manage Kinesis, Lambda, and DynamoDB resources.
- AWS CLI configured with the profile `devops-training`.
- Python 3.x installed.
- `pip` package manager installed.

### Instructions

1. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Build the Application**
   ```
   ./scripts/build.sh
   ```

3. **Deploy the Infrastructure**
   ```
   ./scripts/deploy.sh
   ```

4. **Start Streaming Data**
   ```
   ./scripts/stream.sh
   ```

5. **Run Unit Tests**
   ```
   ./scripts/unit_test.sh
   ```

### DynamoDB Data Structure

Each entry in DynamoDB stores:
- **County**: Name of the county.
- **Timestamp**: The time when the batch was processed.
- **Count**: The number of records for that county in the batch.

## Cleanup

To destroy the infrastructure, run:
```
cd infra
terraform destroy -auto-approve
```

## Notes

- The pipeline is designed to track the count of records per county per batch, not as a rolling count over a period of time.
- Ensure that you have an AWS profile named `devops-training` properly configured before deploying.

import csv
import time
import boto3
import datetime

def get_kinesis_client(profile_name, region_name):
    session = boto3.Session(profile_name=profile_name, region_name=region_name)
    return session.client('kinesis')

def read_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def add_timestamp(row):
    row['Timestamp'] = datetime.datetime.utcnow().isoformat()
    return row

def send_records(kinesis_client, stream_name, records):
    response = kinesis_client.put_records(StreamName=stream_name, Records=records)
    if response['FailedRecordCount'] > 0:
        print("Failed to put some records")

def stream_data():
    aws_profile = "devops-training"
    aws_region = "ap-northeast-1"  # Tokyo region
    kinesis_stream_name = "fishing-data-stream"

    kinesis_client = get_kinesis_client(aws_profile, aws_region)
    rows = read_csv('data/recommended-fishing-rivers-and-streams-1.csv')
    index = 0

    while True:
        batch = []
        for _ in range(10):  # Publish at least 10 rows per second
            if index >= len(rows):
                index = 0  # Restart from the beginning
            row = add_timestamp(rows[index].copy())
            data = str(row).encode('utf-8')
            batch.append({'Data': data, 'PartitionKey': str(index)})
            index += 1
        send_records(kinesis_client, kinesis_stream_name, batch)
        time.sleep(1)

if __name__ == "__main__":
    stream_data()
import json
import base64
import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_name = 'AggregatedData'  
    table = dynamodb.Table(table_name)

    # Aggregated counts per County
    county_counts = {}

    # Current time minus 5 minutes
    time_threshold = datetime.utcnow() - timedelta(minutes=5)

    for record in event['Records']:
        # Decode Kinesis data
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        data = eval(payload) 

        # Extract County and Timestamp
        county = data.get('County')
        timestamp_str = data.get('Timestamp')
        if not county or not timestamp_str:
            continue

        timestamp = datetime.fromisoformat(timestamp_str)

        # Only consider records within the last 5 minutes
        if timestamp >= time_threshold:
            county_counts[county] = county_counts.get(county, 0) + 1

    # Write aggregated counts to DynamoDB
    for county, count in county_counts.items():
        table.put_item(
            Item={
                'County': county,
                'Timestamp': datetime.utcnow().isoformat(),
                'Count': count
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Aggregation successful!')
    }

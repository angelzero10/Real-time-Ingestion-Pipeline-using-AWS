import unittest
import boto3
from src.app import get_kinesis_client

class TestEndToEnd(unittest.TestCase):
    def test_kinesis_stream_exists(self):
        aws_profile = "devops-training"
        aws_region = "ap-northeast-1"
        kinesis_stream_name = "fishing-data-stream"

        kinesis_client = get_kinesis_client(aws_profile, aws_region)
        response = kinesis_client.describe_stream(StreamName=kinesis_stream_name)
        self.assertEqual(response['StreamDescription']['StreamStatus'], 'ACTIVE')

if __name__ == '__main__':
    unittest.main()

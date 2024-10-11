from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.analytics import KinesisDataStreams
from diagrams.aws.general import User

with Diagram("Real-time Ingestion Pipeline", show=False):
    user = User("Data Producer")

    with Cluster("AWS"):
        kinesis = KinesisDataStreams("Fishing Data Stream")
        lambda_function = Lambda("Aggregation Function")
        dynamodb = Dynamodb("Aggregated Data Table")

    user >> kinesis >> lambda_function >> dynamodb

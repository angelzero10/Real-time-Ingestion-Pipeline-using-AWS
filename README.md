
Real-time Ingestion Pipeline Project
====================================

Overview
--------

This project implements a real-time ingestion pipeline for sensor data collection using AWS managed services. It ingests data from a CSV dataset, streams it to AWS Kinesis Data Streams, processes it with AWS Lambda, aggregates the data, and stores the results in AWS DynamoDB.

Architecture
------------

The pipeline consists of:

- **Data Producer**: A Python application that reads data from a CSV file, adds a timestamp, and streams it to AWS Kinesis Data Streams at a rate of at least 10 rows per second.
- **AWS Kinesis Data Streams**: Captures and transports the streaming data.
- **AWS Lambda Function**: Processes data in real-time, performing aggregation on the `County` field for each batch.
- **AWS DynamoDB**: Stores the aggregated results per county per batch.

Project Structure
-----------------

```
project_root/
├── .github/
│   └── workflows/
│       ├── build.yml
│       ├── test.yml
│       └── deploy.yml
├── data/
│   └── recommended-fishing-rivers-and-streams-1.csv
├── src/
│   ├── app.py
│   ├── __init__.py
│   └── lambda_function.py
├── tests/
│   ├── unit/
│   │   └── test_app.py
│   └── e2e/
│       └── test_end_to_end.py
├── infra/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── lambda_function.zip
├── diagrams/
│   ├── architecture_diagram.py
│   └── architecture_diagram.png
├── scripts/
│   ├── build.sh
│   ├── unit_test.sh
│   ├── deploy.sh
│   └── stream.sh
├── requirements.txt
├── README.txt
└── .gitignore
```

Prerequisites
-------------

- **AWS Account**: An AWS account with the profile `devops-training` configured.
- **AWS CLI**: Installed and configured with the `devops-training` profile.
- **Terraform**: Installed (version 0.12 or later).
- **Python**: Python 3.x installed.
- **pip**: Python package manager.
- **Virtual Environment**: Using `python3 -m venv venv` for virtual environments.

Setup and Deployment
--------------------

### 1. Clone the Repository

```bash
git clone https://github.com/angelzero10/luis.ayala.git
cd luis.ayala
```

### 2. Set Up Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Build the Application

```bash
chmod +x scripts/build.sh
./scripts/build.sh
```

This script will:

- Install necessary dependencies for the Lambda function.
- Package the Lambda function code into `lambda_function.zip`.

### 5. Run Unit Tests

```bash
chmod +x scripts/unit_test.sh
./scripts/unit_test.sh
```

### 6. Run End-to-End Tests

```bash
python -m unittest discover -s tests/e2e -p 'test_*.py'
```

### 7. Deploy Infrastructure

```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

This script will:

- Initialize Terraform.
- Apply the Terraform configuration to create AWS resources:
  - Kinesis Data Stream
  - AWS Lambda Function
  - DynamoDB Table
  - Necessary IAM Roles and Policies

### 8. Start Streaming Data

```bash
chmod +x scripts/stream.sh
./scripts/stream.sh
```

This script will:

- Run the `app.py` script to start streaming data to Kinesis Data Streams indefinitely.

### 9. Deactivate Virtual Environment (Optional)

After you're done, you can deactivate the virtual environment:

```bash
deactivate
```

Testing
-------

### Unit Tests

Run unit tests to verify individual components:

```bash
./scripts/unit_test.sh
```

### End-to-End Tests

Run end-to-end tests to verify the entire pipeline:

```bash
python -m unittest discover -s tests/e2e -p 'test_*.py'
```

### Terraform Plan Validation

As part of testing, you can also validate the Terraform plan:

```bash
cd infra
terraform init
terraform plan
```

Deployment
----------

Deployment is handled via Terraform scripts located in the `infra/` directory.

To deploy the infrastructure manually:

```bash
cd infra
terraform init
terraform apply -auto-approve
```

To destroy the infrastructure:

```bash
terraform destroy -auto-approve
```

GitHub Actions CI/CD
--------------------

The project includes GitHub Actions workflows located in `.github/workflows/`:

- **build.yml**: Automates the build process on code push or pull request.
- **test.yml**: Runs unit tests, end-to-end tests, and `terraform plan` on code push or pull request.
- **deploy.yml**: Deploys the infrastructure to AWS on push to the `main` branch.

Ensure you have set up the necessary AWS credentials in your GitHub repository secrets.

AWS Profile and Region
----------------------

The AWS resources are deployed to the Tokyo region (`ap-northeast-1`), and the AWS CLI uses the profile `devops-training`.

Ensure your `~/.aws/credentials` and `~/.aws/config` files are set up accordingly.

Example `~/.aws/config`:

```
[profile devops-training]
region = ap-northeast-1
output = json
```

Example `~/.aws/credentials`:

```
[devops-training]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

Notes
-----

- **Data Streaming**: The `stream.sh` script runs indefinitely. Use `Ctrl+C` to stop it.
- **Lambda Function**: The Lambda function aggregates counts per county per batch and stores them in DynamoDB.
- **DynamoDB Data**: You can view the aggregated data in the DynamoDB table named `AggregatedData`.

Troubleshooting
---------------

- **Lambda Function Errors**: Check AWS CloudWatch Logs for the Lambda function if you encounter issues.
- **AWS Permissions**: Ensure the IAM roles and policies have the necessary permissions.
- **AWS Credentials**: Verify that your AWS CLI is configured correctly with the `devops-training` profile.

Cleanup
-------

To avoid incurring charges on AWS, remember to destroy the infrastructure when it's no longer needed:

```bash
cd infra
terraform destroy -auto-approve
```

Also, deactivate and remove the Python virtual environment if desired:

```bash
deactivate
rm -rf venv
```

Additional Information
----------------------

### Architecture Diagram

The architecture diagram is generated using the `diagrams` Python library.

To regenerate the diagram:

```bash
python diagrams/architecture_diagram.py
```

The diagram will be saved as `diagrams/architecture_diagram.png`.

### Dependencies

The `requirements.txt` file includes all the Python dependencies:

```
boto3
diagrams
```

### .gitignore

The `.gitignore` file is set up to exclude:

- Python cache files
- Virtual environment directories
- Build artifacts
- Terraform state files

Contributing
------------

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Create a pull request.

License
-------

This project is licensed under the MIT License.

Contact
-------

For any questions or issues, please open an issue in the repository or contact the maintainer.

#!/bin/bash
echo "Deploying infrastructure..."
cd infra
terraform init
terraform apply -auto-approve
echo "Deployment completed."

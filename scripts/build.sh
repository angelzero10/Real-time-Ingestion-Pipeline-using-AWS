#!/bin/bash
echo "Building the application..."

# Build the application 
cd src
zip -r ../infra/lambda_function.zip lambda_function.py
cd ..
#!/bin/bash
echo "Running unit tests..."
python -m unittest discover -s tests/unit -p 'test_*.py'

#!/bin/bash

# Create project structure
mkdir -p cyber-triage-forensics/{collector/artifacts,backend/{api,analysis},dashboard/{frontend,backend},infrastructure/terraform,docs}

# Create virtual environment
cd cyber-triage-forensics
python3 -m venv venv
source venv/bin/activate

# Install AWS CLI
pip install awscli boto3

# Configure AWS (you'll be prompted for credentials)
aws configure

echo "Environment setup complete!"
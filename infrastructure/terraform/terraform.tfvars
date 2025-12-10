environment     = "dev"
aws_region      = "us-east-1"
project_name    = "tara"
s3_bucket_name  = "tara-evidence-dev-bucket"

# DynamoDB capacity
dynamodb_read_capacity  = 5
dynamodb_write_capacity = 5

# Lambda settings
lambda_timeout = 300
lambda_memory  = 512

# Logging
enable_logging      = true
log_retention_days  = 30

# Recovery
enable_point_in_time_recovery = true

# API Gateway throttling
api_gateway_throttle_settings = {
  burst_limit = 5000
  rate_limit  = 2000
}

# Tags
tags = {
  Environment = "dev"
  Project     = "TARA"
  ManagedBy   = "Terraform"
}

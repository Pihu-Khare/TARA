import os

class ProductionConfig:
    """Production configuration"""
    DEBUG = False
    TESTING = False
    
    # AWS Settings
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    
    # DynamoDB (managed AWS service)
    DYNAMODB_CASES_TABLE = 'tara-cases-prod'
    DYNAMODB_ARTIFACTS_TABLE = 'tara-artifacts-prod'
    DYNAMODB_FINDINGS_TABLE = 'tara-findings-prod'
    DYNAMODB_COC_TABLE = 'tara-chain-of-custody-prod'
    
    # S3
    S3_BUCKET = os.getenv('S3_BUCKET', 'tara-evidence-prod')
    S3_REGION = os.getenv('S3_REGION', 'us-east-1')
    
    # Analysis
    YARA_RULES_PATH = '/opt/yara/rules'
    ML_MODEL_PATH = '/opt/models'
    
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET = os.getenv('JWT_SECRET')

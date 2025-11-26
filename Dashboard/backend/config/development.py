import os

class DevelopmentConfig:
    """Development configuration"""
    DEBUG = True
    TESTING = False
    
    # Flask settings
    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    
    # CORS
    CORS_ORIGINS = ['http://localhost:3000', 'http://localhost:5173']
    
    # AWS Settings (use local/moto for dev)
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
    
    # Local DynamoDB (for testing)
    DYNAMODB_ENDPOINT = os.getenv('DYNAMODB_ENDPOINT', 'http://localhost:8000')
    
    # Tables
    DYNAMODB_CASES_TABLE = 'tara-cases-dev'
    DYNAMODB_ARTIFACTS_TABLE = 'tara-artifacts-dev'
    DYNAMODB_FINDINGS_TABLE = 'tara-findings-dev'
    DYNAMODB_COC_TABLE = 'tara-chain-of-custody-dev'
    
    # S3
    S3_BUCKET = os.getenv('S3_BUCKET', 'tara-evidence-dev')
    S3_REGION = os.getenv('S3_REGION', 'us-east-1')
    
    # Upload
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024 * 1024  # 5GB
    UPLOAD_FOLDER = '/tmp/uploads'
    
    # Analysis
    YARA_RULES_PATH = os.getenv('YARA_RULES_PATH', './rules')
    ML_MODEL_PATH = os.getenv('ML_MODEL_PATH', './models')
    
    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-prod')
    JWT_SECRET = os.getenv('JWT_SECRET', 'jwt-secret-key-change-in-prod')
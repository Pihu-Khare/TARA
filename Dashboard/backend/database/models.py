import boto3
import json
from datetime import datetime
from uuid import uuid4
from app import current_app

dynamodb = boto3.resource('dynamodb')

class Case:
    """DynamoDB Case Model"""
    
    def __init__(self, title, host, severity='Normal', status='Open', analyst=None):
        self.case_id = f"CASE-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}-{uuid4().hex[:8].upper()}"
        self.title = title
        self.host = host
        self.severity = severity
        self.status = status
        self.analyst = analyst
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = datetime.utcnow().isoformat()
        self.artifact_count = 0
        self.bad_count = 0
        self.suspicious_count = 0
    
    def save(self):
        """Save case to DynamoDB"""
        table = dynamodb.Table(current_app.config['DYNAMODB_CASES_TABLE'])
        table.put_item(Item=self.to_dict())
        return self.case_id
    
    @staticmethod
    def get(case_id):
        """Retrieve case from DynamoDB"""
        table = dynamodb.Table(current_app.config['DYNAMODB_CASES_TABLE'])
        response = table.get_item(Key={'case_id': case_id})
        return response.get('Item')
    
    @staticmethod
    def list_all(limit=50):
        """List all cases"""
        table = dynamodb.Table(current_app.config['DYNAMODB_CASES_TABLE'])
        response = table.scan(Limit=limit)
        return response.get('Items', [])
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'case_id': self.case_id,
            'title': self.title,
            'host': self.host,
            'severity': self.severity,
            'status': self.status,
            'analyst': self.analyst,
            'artifact_count': self.artifact_count,
            'bad_count': self.bad_count,
            'suspicious_count': self.suspicious_count,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class Artifact:
    """DynamoDB Artifact Model"""
    
    def __init__(self, case_id, filename, file_type, size, sha256):
        self.artifact_id = str(uuid4())
        self.case_id = case_id
        self.filename = filename
        self.file_type = file_type
        self.size = size
        self.sha256 = sha256
        self.collected_at = datetime.utcnow().isoformat()
        self.s3_path = f"s3://{case_id}/{self.artifact_id}/{filename}"
    
    def save(self):
        """Save artifact to DynamoDB"""
        table = dynamodb.Table(current_app.config['DYNAMODB_ARTIFACTS_TABLE'])
        table.put_item(Item=self.to_dict())
        return self.artifact_id
    
    @staticmethod
    def get_by_case(case_id):
        """Get all artifacts for a case"""
        table = dynamodb.Table(current_app.config['DYNAMODB_ARTIFACTS_TABLE'])
        response = table.query(
            KeyConditionExpression='case_id = :case_id',
            ExpressionAttributeValues={':case_id': case_id}
        )
        return response.get('Items', [])
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'artifact_id': self.artifact_id,
            'case_id': self.case_id,
            'filename': self.filename,
            'file_type': self.file_type,
            'size': self.size,
            'sha256': self.sha256,
            's3_path': self.s3_path,
            'collected_at': self.collected_at
        }

class Finding:
    """DynamoDB Finding Model"""
    
    def __init__(self, case_id, title, severity, finding_type, detected_by):
        self.finding_id = str(uuid4())
        self.case_id = case_id
        self.title = title
        self.severity = severity
        self.finding_type = finding_type
        self.detected_by = detected_by
        self.detected_at = datetime.utcnow().isoformat()
        self.confidence = 0.0
    
    def save(self):
        """Save finding to DynamoDB"""
        table = dynamodb.Table(current_app.config['DYNAMODB_FINDINGS_TABLE'])
        table.put_item(Item=self.to_dict())
        return self.finding_id
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'finding_id': self.finding_id,
            'case_id': self.case_id,
            'title': self.title,
            'severity': self.severity,
            'finding_type': self.finding_type,
            'detected_by': self.detected_by,
            'confidence': self.confidence,
            'detected_at': self.detected_at
        }

class ChainOfCustody:
    """Chain of Custody Log Model"""
    
    def __init__(self, case_id, artifact_id, action, user, role):
        self.log_id = str(uuid4())
        self.case_id = case_id
        self.artifact_id = artifact_id
        self.action = action
        self.user = user
        self.role = role
        self.timestamp = datetime.utcnow().isoformat()
        self.hash_verified = False
    
    def save(self):
        """Save to DynamoDB"""
        table = dynamodb.Table(current_app.config['DYNAMODB_COC_TABLE'])
        table.put_item(Item=self.to_dict())
        return self.log_id
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'log_id': self.log_id,
            'case_id': self.case_id,
            'artifact_id': self.artifact_id,
            'action': self.action,
            'user': self.user,
            'role': self.role,
            'timestamp': self.timestamp,
            'hash_verified': self.hash_verified
        }

import boto3
from flask import current_app

class S3Service:
    """AWS S3 operations"""
    
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.bucket = current_app.config['S3_BUCKET']
    
    def upload_file(self, file_path, case_id, artifact_id):
        """Upload file to S3"""
        key = f"{case_id}/{artifact_id}"
        try:
            self.s3_client.upload_file(
                file_path,
                self.bucket,
                key,
                ExtraArgs={'ServerSideEncryption': 'AES256'}
            )
            return True
        except Exception as e:
            print(f"S3 upload error: {e}")
            return False
    
    def generate_presigned_url(self, case_id, filename, expiration=3600):
        """Generate presigned URL for upload"""
        key = f"{case_id}/{filename}"
        try:
            url = self.s3_client.generate_presigned_url(
                'put_object',
                Params={'Bucket': self.bucket, 'Key': key},
                ExpiresIn=expiration
            )
            return url
        except Exception as e:
            print(f"Presigned URL error: {e}")
            return None
    
    def get_file(self, case_id, artifact_id):
        """Download file from S3"""
        key = f"{case_id}/{artifact_id}"
        try:
            response = self.s3_client.get_object(Bucket=self.bucket, Key=key)
            return response['Body'].read()
        except Exception as e:
            print(f"S3 download error: {e}")
            return None

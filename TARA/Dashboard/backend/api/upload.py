from flask_restx import Namespace, Resource, fields
from flask import request, current_app
import hashlib
import boto3
import os

ns = Namespace('upload', description='Evidence upload')

@ns.route('/presign')
class PresignedURL(Resource):
    @ns.doc('get_presigned_url')
    def post(self):
        """Get presigned URL for S3 upload"""
        data = request.get_json()
        case_id = data.get('case_id')
        filename = data.get('filename')
        
        s3_client = boto3.client('s3')
        bucket = current_app.config['S3_BUCKET']
        key = f"{case_id}/{filename}"
        
        try:
            url = s3_client.generate_presigned_url(
                'put_object',
                Params={'Bucket': bucket, 'Key': key},
                ExpiresIn=3600
            )
            return {
                'success': True,
                'url': url,
                'bucket': bucket,
                'key': key
            }, 200
        except Exception as e:
            return {'error': str(e)}, 500

@ns.route('/complete')
class CompleteUpload(Resource):
    @ns.doc('complete_upload')
    def post(self):
        """Complete upload and trigger analysis"""
        data = request.get_json()
        case_id = data.get('case_id')
        artifact_id = data.get('artifact_id')
        sha256 = data.get('sha256')
        
        from database.models import ChainOfCustody
        coc = ChainOfCustody(
            case_id=case_id,
            artifact_id=artifact_id,
            action='Upload',
            user='System',
            role='Collector'
        )
        coc.save()
        
        return {
            'success': True,
            'message': 'Upload completed',
            'artifact_id': artifact_id
        }, 200

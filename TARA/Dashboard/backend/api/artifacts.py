from flask_restx import Namespace, Resource, fields
from flask import request
from database.models import Artifact
import boto3

ns = Namespace('artifacts', description='Artifact management')

artifact_model = ns.model('Artifact', {
    'artifact_id': fields.String(),
    'case_id': fields.String(required=True),
    'filename': fields.String(required=True),
    'file_type': fields.String(),
    'size': fields.Integer(),
    'sha256': fields.String(),
    's3_path': fields.String(),
    'collected_at': fields.String()
})

@ns.route('/case/<string:case_id>')
class CaseArtifacts(Resource):
    @ns.doc('get_case_artifacts')
    def get(self, case_id):
        """Get all artifacts for a case"""
        artifacts = Artifact.get_by_case(case_id)
        return {
            'success': True,
            'count': len(artifacts),
            'data': artifacts
        }, 200

@ns.route('/<string:artifact_id>')
class ArtifactDetail(Resource):
    @ns.doc('get_artifact')
    def get(self, artifact_id):
        """Get artifact details"""
        table = boto3.resource('dynamodb').Table('tara-artifacts')
        response = table.get_item(Key={'artifact_id': artifact_id})
        
        if 'Item' not in response:
            return {'error': 'Artifact not found'}, 404
        
        return {
            'success': True,
            'data': response['Item']
        }, 200

from flask_restx import Namespace, Resource, fields
from database.models import Finding

ns = Namespace('analysis', description='Analysis and findings')

finding_model = ns.model('Finding', {
    'finding_id': fields.String(),
    'case_id': fields.String(required=True),
    'title': fields.String(required=True),
    'severity': fields.String(),
    'finding_type': fields.String(),
    'detected_by': fields.String(),
    'confidence': fields.Float(),
    'detected_at': fields.String()
})

@ns.route('/case/<string:case_id>')
class CaseFindings(Resource):
    @ns.doc('get_case_findings')
    def get(self, case_id):
        """Get findings for a case"""
        # Query findings from DynamoDB
        import boto3
        table = boto3.resource('dynamodb').Table('tara-findings')
        response = table.query(
            KeyConditionExpression='case_id = :cid',
            ExpressionAttributeValues={':cid': case_id}
        )
        
        findings = response.get('Items', [])
        return {
            'success': True,
            'count': len(findings),
            'data': findings
        }, 200

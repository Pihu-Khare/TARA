from flask_restx import Namespace, Resource, fields
from flask import request, current_app
from database.models import Case

ns = Namespace('cases', description='Case management operations')

# Define models
case_model = ns.model('Case', {
    'case_id': fields.String(),
    'title': fields.String(required=True),
    'host': fields.String(required=True),
    'severity': fields.String(enum=['Critical', 'Warning', 'Normal']),
    'status': fields.String(enum=['Open', 'In Progress', 'Closed']),
    'analyst': fields.String(),
    'created_at': fields.String(),
    'updated_at': fields.String(),
    'artifact_count': fields.Integer(),
    'bad_count': fields.Integer(),
    'suspicious_count': fields.Integer()
})

@ns.route('')
class CaseList(Resource):
    @ns.doc('list_cases')
    def get(self):
        """List all cases"""
        severity = request.args.get('severity', 'All')
        status = request.args.get('status', 'All')
        
        cases = Case.list_all()
        
        if severity != 'All':
            cases = [c for c in cases if c['severity'] == severity]
        if status != 'All':
            cases = [c for c in cases if c['status'] == status]
        
        return {
            'success': True,
            'count': len(cases),
            'data': cases
        }, 200
    
    @ns.doc('create_case')
    @ns.expect(case_model)
    def post(self):
        """Create new case"""
        data = ns.payload
        case = Case(
            title=data['title'],
            host=data['host'],
            severity=data.get('severity', 'Normal'),
            status=data.get('status', 'Open'),
            analyst=data.get('analyst')
        )
        case_id = case.save()
        return {
            'success': True,
            'message': 'Case created',
            'case_id': case_id,
            'data': case.to_dict()
        }, 201

@ns.route('/<string:case_id>')
class CaseDetail(Resource):
    @ns.doc('get_case')
    def get(self, case_id):
        """Get case details"""
        case = Case.get(case_id)
        if not case:
            return {'error': 'Case not found'}, 404
        
        return {
            'success': True,
            'data': case
        }, 200
    
    @ns.doc('update_case')
    @ns.expect(case_model)
    def put(self, case_id):
        """Update case"""
        data = ns.payload
        case = Case.get(case_id)
        if not case:
            return {'error': 'Case not found'}, 404
        
        # Update fields
        case['title'] = data.get('title', case['title'])
        case['status'] = data.get('status', case['status'])
        case['severity'] = data.get('severity', case['severity'])
        
        table = boto3.resource('dynamodb').Table(
            current_app.config['DYNAMODB_CASES_TABLE']
        )
        table.put_item(Item=case)
        
        return {
            'success': True,
            'message': 'Case updated',
            'data': case
        }, 200

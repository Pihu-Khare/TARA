from flask import Flask
from flask_cors import CORS
from flask_restx import Api
import os

def create_app(config_name='development'):
    """Create and configure Flask application"""
    app = Flask(__name__)
    
    # Load configuration
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        from config.production import ProductionConfig
        app.config.from_object(ProductionConfig)
    else:
        from config.development import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)
    
    # Initialize extensions
    CORS(app)
    api = Api(app, version='1.0', title='TARA Backend', 
              description='Cyber Triage & Digital Forensics API')
    
    # Register namespaces
    from api.cases import ns as cases_ns
    from api.artifacts import ns as artifacts_ns
    from api.analysis import ns as analysis_ns
    from api.upload import ns as upload_ns
    
    api.add_namespace(cases_ns)
    api.add_namespace(artifacts_ns)
    api.add_namespace(analysis_ns)
    api.add_namespace(upload_ns)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Resource not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {'error': 'Internal server error'}, 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

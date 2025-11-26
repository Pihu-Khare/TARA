import subprocess
from database.models import Finding
from flask import current_app

class AnalysisService:
    """Coordinate analysis tasks"""
    
    @staticmethod
    def run_yara_scan(case_id, artifact_path):
        """Run YARA scan on artifact"""
        try:
            rules_path = current_app.config['YARA_RULES_PATH']
            cmd = f"yara -r {rules_path} {artifact_path}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            findings = []
            for line in result.stdout.split('\n'):
                if line.strip():
                    finding = Finding(
                        case_id=case_id,
                        title=line.split()[0],
                        severity='Critical',
                        finding_type='File',
                        detected_by='YARA'
                    )
                    finding.confidence = 0.95
                    finding.save()
                    findings.append(finding.to_dict())
            
            return findings
        except Exception as e:
            print(f"YARA scan error: {e}")
            return []
    
    @staticmethod
    def run_anomaly_detection(case_id, artifact_id):
        """Run ML anomaly detection"""
        try:
            # Load ML model
            import pickle
            model_path = current_app.config['ML_MODEL_PATH']
            
            # Run detection
            findings = []
            # Placeholder for ML logic
            
            return findings
        except Exception as e:
            print(f"ML analysis error: {e}")
            return []

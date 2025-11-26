# 🛡️ TARA — Triage, Analysis & Reporting Automation

TARA is a **cloud-native digital forensics triage system** that automates the early stages of cyber-incident investigation. It securely collects system artifacts from endpoints, analyzes them using rule-based checks and AI-driven anomaly detection, and generates **tamper-proof forensic reports**. Designed with AWS serverless microservices, TARA helps investigators quickly identify suspicious activity, prioritize threats, and streamline digital forensics workflows.

---

## 🚀 Features

### 🔍 Automated Artifact Collection
- Lightweight Python-based collector
- Gathers processes, network connections, logs, and file metadata
- Generates SHA-256 hashes for chain of custody
- Secure upload to AWS S3 using pre-signed URLs

### 🧠 Intelligent Triage Engine
- Rule-based detection (YARA patterns, suspicious binaries, unusual ports)
- AI anomaly detection using Isolation Forest
- Severity scoring and summarized findings
- Structured triage output in JSON

### ☁️ Cloud-Native Architecture
- AWS Lambda for compute
- API Gateway for secure routing
- DynamoDB / RDS for metadata
- S3 for encrypted evidence storage
- Cognito for authentication and access control

### 📄 Automated Forensic Reporting
- Generates tamper-proof PDF reports
- Includes anomalies, indicators, timestamps, and evidence summaries
- Reports stored in S3 with signed URLs

### 🔐 Security & Chain of Custody
- SHA-256 hashing + timestamping
- Encrypted S3 storage
- IAM least-privilege roles
- Logged actions for forensic integrity

---

## 🏗️ System Architecture


---

## 📦 Tech Stack

- **Backend:** AWS Lambda, API Gateway, S3, DynamoDB/RDS, CloudWatch  
- **Frontend:** React or Flutter Web  
- **AI/ML:** Python, scikit-learn (Isolation Forest), YARA  
- **Collector:** Python  
- **Reporting:** Python + ReportLab / wkhtmltopdf  

---

## 📁 Suggested Repository Structure


---

## 🧪 Testing

- Synthetic artifacts (fake logs, process lists, mock anomalies)
- Public forensic datasets (CICIDS, CTU-13)
- Safe YARA test strings
- End-to-end workflow tests using Jest/PyTest

No real malware is required.

---

## 📌 Use Cases

- Rapid triage during cyber incidents  
- Automated pre-analysis for digital forensics  
- SOC enrichment and alert validation  
- DFIR training and simulation  

---

## 🤝 Contributing

Contributions, issues, and feature suggestions are welcome.  
Please avoid uploading harmful files or real malware.

---

## 📜 License

MIT / Apache-2.0 / GPL — choose based on your needs.

---

## ⭐ Acknowledgments

Inspired by DFIR methodologies, cloud-native design, and modern threat detection techniques.

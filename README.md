# MAaaS - Multi-Agent as a Service Enterprise Platform

**Full-Cycle MAaaS Enterprise Platform** - Transform client organizations into autonomous, secure, and scalable agentic ecosystems.

## 🎯 Mission

The Swarm Agency is a **Full-Cycle Multi-Agent as a Service (MAaaS) Enterprise Platform** that transforms client organizations into autonomous, secure, and scalable agentic ecosystems. We operate as the "Meta-Developer," creating and orchestrating specialized AI workforces that handle everything from data management to cybersecurity, reliability engineering, and growth operations.

## 🏗️ Architecture: The 5-Pillar System

### PILLAR 1: WORKFORCE FABRICATION ✅
- **Organizational Mapping:** Ingest client org charts and SOPs to generate Virtual Agentic Maps
- **Agent Catalogue:** Library of Base Agent Classes across departments
- **Factory Pipeline:** Automated agent instantiation, configuration, and E-Contract generation

### PILLAR 2: DATA SOVEREIGNTY 🚧
- SQL Schema design and optimization
- Vector Stores (RAG) and Knowledge Graphs
- Oblivious RAM (ORAM) for private data access

### PILLAR 3: CYBER-INFRASTRUCTURE 🚧
- Active vulnerability scanning
- Network Management
- Session-Level Semantic Firewalls

### PILLAR 4: RELIABILITY ENGINEERING 🚧
- SRE roles for SLA enforcement
- Automated bug fixing
- System monitoring

### PILLAR 5: GROWTH OPERATIONS 🚧
- Omnichannel marketing
- Business Intelligence
- ROI monitoring

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Virtual environment (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/aiwork400/MAaaS.git
cd MAaaS

# Create and activate virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\Activate.ps1
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install streamlit pandas plotly fastapi uvicorn rich
```

### Running the Factory

```bash
# Interactive Factory CLI
python run_swarm_factory.py
```

### Running the Dashboard

```bash
# Streamlit Dashboard
streamlit run dashboard.py
```

### Running the API Server

```bash
# FastAPI REST API
uvicorn api_server:app --reload --port 8000
```

## 📁 Project Structure

```
MAaaS/
├── catalogue/              # Base Agent Classes (Templates)
│   ├── gent_ProjectManager.py
│   ├── agent_Compliance.py
│   ├── Agent_DBA.py
│   ├── Agent_NetSec.py
│   └── ...
├── clients/                # Client-specific configurations
│   ├── Nexus/              # Nexus Financial Assurance agents
│   └── nexus_*.json        # Client profiles and deployment plans
├── factory_logs/           # Provenance and audit logs
├── dashboard.py            # Streamlit Command Center
├── api_server.py           # FastAPI REST API
├── run_swarm_factory.py    # Interactive Factory CLI
└── specification.md        # Project Constitution
```

## 🔧 Key Features

### Agent Factory
- **Intake Analysis:** Detects client needs (Data, Security, Growth triggers)
- **Mapping:** Maps client roles to specialized agents
- **Fabrication:** Instantiates and configures agents
- **E-Contracts:** Generates token budgets and deliverables

### Dashboard (Streamlit)
- **Overview:** System health, active agents, contract status
- **Cyber-Infrastructure:** Firewall logs, patch status
- **Growth & Financials:** Budget separation, ROI monitoring
- **Chat Ops:** Real-time communication with Nexus_PM

### API Server (FastAPI)
- RESTful endpoints for agent management
- Contract management
- Provenance logs
- Chat interface
- System metrics

## 🔒 Security Features

- **MPC Protocols:** Yao's GC, GMW, SPDZ for privacy-preserving computations
- **Session-Level Firewalls:** Prevents cross-domain context bypass (C6)
- **Provenance Tracking:** Full audit trails (C5 compliance)
- **Side-Channel Hardening:** Constant-time operations (CBS-02-002)

## 📚 Documentation

- [Specification](specification.md) - Project Constitution & Technical Specs
- [File Doctor README](FILE_DOCTOR_README.md) - JSON Encoding Repair Utility
- [Chat Ops Integration](CHAT_OPS_INTEGRATION.md) - Real Agent Communication

## 🛠️ Utilities

### File Doctor
Repair JSON files with encoding issues:
```bash
python file_doctor.py --all --check    # Check files
python file_doctor.py --all             # Repair files
```

## 📊 Example Client: Nexus Financial Assurance Ltd.

The repository includes a complete example deployment for **Nexus Financial Assurance Ltd.**:

- **Industry:** FinTech / Audit Services
- **Agents:** Nexus_PM, Nexus_Compliance, Nexus_Researcher, Nexus_NetSec
- **Workflow:** WF-AUDIT-01 (Automated Transaction Audit)
- **Security:** Yao's Garbled Circuits for PII protection

## 🤝 Contributing

This is a private enterprise platform. For questions or contributions, please contact the repository owner.

## 📄 License

Proprietary - All rights reserved

## 🔗 References

- **Master Data:** `Master Data for MAaaS.pdf`
- **Deployment Plan:** `clients/nexus_deployment_plan.json`
- **GitHub Repository:** https://github.com/aiwork400/MAaaS

---

**Built with:** Python, Streamlit, FastAPI, Rich CLI
**Security:** MPC (Yao's GC, GMW, SPDZ), Session Firewalls, Provenance Tracking


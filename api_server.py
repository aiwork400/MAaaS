#!/usr/bin/env python3
"""
MAaaS API Server - FastAPI REST API
Provides programmatic access to the Swarm Agency ecosystem.

Endpoints:
- Health & Status
- Agent Management
- Contract Management
- Workflow Execution
- Provenance Logs
- System Metrics
"""

from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
from pathlib import Path as PathLib
from datetime import datetime
import json
import sys

# Add repository root to path
REPO_ROOT = PathLib(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# Import shared file utilities (used by both dashboard and API server)
try:
    from file_utils import read_json_file_robust, read_jsonl_file_robust
except ImportError:
    # Fallback: try importing from dashboard (which also uses file_utils)
    try:
        from dashboard import (
            read_json_file_robust,
            read_jsonl_file_robust,
        )
    except ImportError:
        # Final fallback: basic implementation
        def read_json_file_robust(file_path: PathLib) -> Dict[str, Any]:
            encodings = ["utf-8-sig", "utf-8", "utf-16", "utf-16-le", "utf-16-be", "latin-1"]
            for encoding in encodings:
                try:
                    with open(file_path, "r", encoding=encoding) as f:
                        return json.loads(f.read())
                except (UnicodeDecodeError, json.JSONDecodeError):
                    continue
            raise ValueError(f"Could not decode file {file_path}")
        
        def read_jsonl_file_robust(file_path: PathLib) -> List[Dict[str, Any]]:
            if not file_path.exists():
                return []
            encodings = ["utf-8-sig", "utf-8", "utf-16", "utf-16-le", "utf-16-be", "latin-1"]
            logs = []
            for encoding in encodings:
                try:
                    with open(file_path, "r", encoding=encoding) as f:
                        for line in f:
                            line = line.strip()
                            if line:
                                try:
                                    logs.append(json.loads(line))
                                except json.JSONDecodeError:
                                    continue
                        return logs
                except UnicodeDecodeError:
                    continue
            return []

# Import dashboard data loaders
try:
    from dashboard import (
        load_agents,
        load_econtracts,
        load_project_status,
        load_provenance_logs
    )
except ImportError:
    # Fallback implementations
    def load_agents() -> List[Dict[str, Any]]:
        nexus_dir = REPO_ROOT / "clients" / "Nexus"
        agents = []
        if nexus_dir.exists():
            for agent_file in nexus_dir.glob("Nexus_*.py"):
                agents.append({
                    "name": agent_file.stem,
                    "file": agent_file.name,
                    "status": "ACTIVE"
                })
        return agents
    
    def load_econtracts() -> Dict[str, Dict[str, Any]]:
        return {}
    
    def load_project_status() -> Dict[str, Any]:
        return {"status": "UNKNOWN", "client": "Nexus Financial Assurance Ltd."}
    
    def load_provenance_logs() -> List[Dict[str, Any]]:
        provenance_path = REPO_ROOT / "factory_logs" / "nexus_provenance_audit.jsonl"
        if provenance_path.exists():
            return read_jsonl_file_robust(provenance_path)
        return []
    
    def load_agents() -> List[Dict[str, Any]]:
        nexus_dir = REPO_ROOT / "clients" / "Nexus"
        agents = []
        if nexus_dir.exists():
            for agent_file in nexus_dir.glob("Nexus_*.py"):
                agents.append({
                    "name": agent_file.stem,
                    "file": agent_file.name,
                    "status": "ACTIVE"
                })
        return agents
    
    def load_econtracts() -> Dict[str, Dict[str, Any]]:
        return {}
    
    def load_project_status() -> Dict[str, Any]:
        return {"status": "UNKNOWN", "client": "Nexus Financial Assurance Ltd."}
    
    def load_provenance_logs() -> List[Dict[str, Any]]:
        provenance_path = REPO_ROOT / "factory_logs" / "nexus_provenance_audit.jsonl"
        if provenance_path.exists():
            return read_jsonl_file_robust(provenance_path)
        return []

# Initialize FastAPI app
app = FastAPI(
    title="MAaaS API Server",
    description="REST API for Swarm Agency Multi-Agent as a Service Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class HealthResponse(BaseModel):
    status: str
    timestamp: str
    version: str

class AgentInfo(BaseModel):
    name: str
    file: str
    status: str
    last_updated: Optional[str] = None

class ContractInfo(BaseModel):
    contract_id: str
    status: str
    agent_id: Optional[str] = None
    base_class: Optional[str] = None

class ProvenanceLogEntry(BaseModel):
    timestamp: str
    agent_id: str
    action: str
    mpc_protocol: Optional[str] = None
    details: Optional[Dict[str, Any]] = None

class SystemMetrics(BaseModel):
    sla_uptime: float
    active_agents: int
    signed_contracts: int
    total_contracts: int

# ============================================================================
# HEALTH & STATUS ENDPOINTS
# ============================================================================

@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint with API information."""
    return {
        "service": "MAaaS API Server",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        version="1.0.0"
    )

@app.get("/status", response_model=Dict[str, Any])
async def system_status():
    """Get overall system status."""
    try:
        project_status = load_project_status()
        agents = load_agents()
        contracts = load_econtracts()
        
        return {
            "system_status": project_status.get("status", "UNKNOWN"),
            "client": project_status.get("client", "Nexus Financial Assurance Ltd."),
            "sla_uptime": project_status.get("sla_uptime", 99.8),
            "active_agents": len(agents),
            "signed_contracts": sum(1 for c in contracts.values() if c.get("status") == "SIGNED"),
            "total_contracts": len(contracts),
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading system status: {str(e)}")

# ============================================================================
# AGENT MANAGEMENT ENDPOINTS
# ============================================================================

@app.get("/agents", response_model=List[AgentInfo])
async def list_agents():
    """List all active agents."""
    try:
        agents = load_agents()
        return [AgentInfo(**agent) for agent in agents]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading agents: {str(e)}")

@app.get("/agents/{agent_name}", response_model=AgentInfo)
async def get_agent(agent_name: str = Path(..., description="Agent name (e.g., Nexus_Compliance)")):
    """Get details for a specific agent."""
    try:
        agents = load_agents()
        agent = next((a for a in agents if a["name"] == agent_name), None)
        if not agent:
            raise HTTPException(status_code=404, detail=f"Agent '{agent_name}' not found")
        return AgentInfo(**agent)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading agent: {str(e)}")

# ============================================================================
# CONTRACT MANAGEMENT ENDPOINTS
# ============================================================================

@app.get("/contracts", response_model=Dict[str, ContractInfo])
async def list_contracts():
    """List all E-Contracts."""
    try:
        contracts = load_econtracts()
        return {
            agent_type: ContractInfo(**contract)
            for agent_type, contract in contracts.items()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading contracts: {str(e)}")

@app.get("/contracts/{contract_id}", response_model=ContractInfo)
async def get_contract(contract_id: str = Path(..., description="Contract ID")):
    """Get details for a specific contract."""
    try:
        contracts = load_econtracts()
        contract = next(
            (c for c in contracts.values() if c.get("contract_id") == contract_id),
            None
        )
        if not contract:
            raise HTTPException(status_code=404, detail=f"Contract '{contract_id}' not found")
        return ContractInfo(**contract)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading contract: {str(e)}")

# ============================================================================
# PROVENANCE LOGS ENDPOINTS
# ============================================================================

@app.get("/provenance", response_model=List[ProvenanceLogEntry])
async def get_provenance_logs(
    limit: int = Query(100, ge=1, le=1000, description="Maximum number of log entries to return"),
    agent_id: Optional[str] = Query(None, description="Filter by agent ID")
):
    """Get provenance audit logs."""
    try:
        logs = load_provenance_logs()
        
        # Filter by agent_id if provided
        if agent_id:
            logs = [log for log in logs if log.get("agent_id", "").startswith(agent_id)]
        
        # Limit results
        logs = logs[-limit:] if limit else logs
        
        return [
            ProvenanceLogEntry(
                timestamp=log.get("timestamp", ""),
                agent_id=log.get("agent_id", "Unknown"),
                action=log.get("action", ""),
                mpc_protocol=log.get("mpc_protocol"),
                details=log
            )
            for log in logs
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading provenance logs: {str(e)}")

# ============================================================================
# METRICS ENDPOINTS
# ============================================================================

@app.get("/metrics", response_model=SystemMetrics)
async def get_metrics():
    """Get system metrics."""
    try:
        project_status = load_project_status()
        agents = load_agents()
        contracts = load_econtracts()
        
        return SystemMetrics(
            sla_uptime=project_status.get("sla_uptime", 99.8),
            active_agents=len(agents),
            signed_contracts=sum(1 for c in contracts.values() if c.get("status") == "SIGNED"),
            total_contracts=len(contracts)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading metrics: {str(e)}")

# ============================================================================
# DEPLOYMENT PLAN ENDPOINT
# ============================================================================

@app.get("/deployment-plan", response_model=Dict[str, Any])
async def get_deployment_plan():
    """Get the Nexus deployment plan."""
    try:
        deployment_plan_path = REPO_ROOT / "clients" / "nexus_deployment_plan.json"
        if not deployment_plan_path.exists():
            raise HTTPException(status_code=404, detail="Deployment plan not found")
        
        plan = read_json_file_robust(deployment_plan_path)
        return plan
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading deployment plan: {str(e)}")

# ============================================================================
# CHAT ENDPOINTS
# ============================================================================

class ChatRequest(BaseModel):
    message: str = Field(..., description="User message to Nexus_PM")

class ChatResponse(BaseModel):
    response: str
    agent_id: str
    timestamp: str

# Cache for Nexus_PM agent instance
_nexus_pm_cache = None

def get_nexus_pm_agent():
    """Get or create Nexus_PM agent instance (cached)."""
    global _nexus_pm_cache
    
    if _nexus_pm_cache is None:
        try:
            from clients.Nexus.Nexus_PM import Nexus_PM
            
            agent = Nexus_PM("Nexus_PM", "Audit Workflow Supervisor")
            
            # Load and sign contract if not already signed
            if not agent.active_contract or agent.active_contract.get("status") != "SIGNED":
                deployment_plan_path = REPO_ROOT / "clients" / "nexus_deployment_plan.json"
                if deployment_plan_path.exists():
                    try:
                        plan = read_json_file_robust(deployment_plan_path)
                        pm_info = plan.get("deployment_plan", {}).get("agent_instances", {}).get("project_manager", {})
                        
                        contract = {
                            "contract_id": pm_info.get("contract_id", "Nexus Financial Assurance Ltd.-PM-MASTER"),
                            "financial_terms": {
                                "token_budget_max": 100000,
                            },
                            "deliverables": ["End-to-end coordination of WF-AUDIT-01"],
                            "security_protocols": {
                                "mpc_required": True,
                                "session_firewall_enabled": True,
                            },
                        }
                        
                        agent.sign_contract(contract)
                        
                        # Register known subordinate agents
                        agent.register_subordinate_agent("researcher", "Nexus_Researcher-001")
                        agent.register_subordinate_agent("compliance", "Nexus_Compliance-001")
                        if (REPO_ROOT / "clients" / "Nexus" / "Nexus_NetSec.py").exists():
                            agent.register_subordinate_agent("netsec", "Nexus_NetSec-001")
                    except Exception:
                        pass  # Contract loading failed, but agent can still function
            
            _nexus_pm_cache = agent
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to instantiate Nexus_PM: {str(e)}")
    
    return _nexus_pm_cache

@app.post("/chat", response_model=ChatResponse)
async def chat_with_pm(request: ChatRequest):
    """Send a message to Nexus_PM and get a response."""
    try:
        agent = get_nexus_pm_agent()
        response_text = agent.process_chat_request(request.message)
        
        return ChatResponse(
            response=response_text,
            agent_id=agent.agent_id,
            timestamp=datetime.now().isoformat()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")

@app.get("/chat/history")
async def get_chat_capabilities():
    """Get information about chat capabilities."""
    try:
        agent = get_nexus_pm_agent()
        return {
            "agent_id": agent.agent_id,
            "agent_name": agent.name,
            "specialization": agent.specialization,
            "contract_status": agent.active_contract.get("status") if agent.active_contract else "UNSIGNED",
            "capabilities": [
                "System status queries",
                "Workflow progress (WF-AUDIT-01)",
                "Budget and financial information",
                "Agent swarm status",
                "General project assistance"
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting chat info: {str(e)}")

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "Resource not found", "path": str(request.url.path)}
    )

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "error": str(exc)}
    )

# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api_server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )


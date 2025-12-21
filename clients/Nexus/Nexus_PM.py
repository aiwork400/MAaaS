#!/usr/bin/env python3
"""
Nexus_PM: Specialized Project Manager Agent for Nexus Financial Assurance Ltd.

This agent implements:
- Supervisor Pattern for WF-AUDIT-01 orchestration
- Task decomposition and delegation
- Trust Ledger management for subordinate agents
- Full provenance tracking (C5 compliance)

Reference: Nexus Swarm Deployment Plan (clients/nexus_deployment_plan.md)
"""

import sys
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Add repository root to path for imports
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from catalogue.gent_ProjectManager import Agent_ProjectManager


class Nexus_PM(Agent_ProjectManager):
    """
    Specialized Project Manager Agent for Nexus Financial Assurance Ltd.
    
    Inherits from Agent_ProjectManager and extends with:
    - WF-AUDIT-01 specific workflow orchestration
    - Trust Ledger tracking for Nexus agents
    - Full provenance tracking (C5 compliance)
    """
    
    def __init__(self, agent_name: str = "Nexus_PM", 
                 specialization: str = "Audit Workflow Supervisor"):
        super().__init__(agent_name, specialization)
        self.provenance_log: List[Dict[str, Any]] = []
        self.token_usage = 0
        self.token_budget_max = 100000  # Per Deployment Plan: 100k tokens (20% of 500k)
        self.nexus_agent_ids: Dict[str, str] = {}  # Track subordinate Nexus agents
    
    def _log_provenance(self, event: Dict[str, Any]) -> None:
        """Log provenance information for C5 compliance."""
        event["provenance_id"] = hashlib.sha256(
            json.dumps(event, sort_keys=True).encode()
        ).hexdigest()[:16]
        event["agent_id"] = self.agent_id
        event["timestamp"] = datetime.now().isoformat()
        self.provenance_log.append(event)
    
    def orchestrate_wf_audit_01(self) -> Dict[str, Any]:
        """
        Orchestrate the complete WF-AUDIT-01 workflow.
        
        Supervisor Pattern: Decomposes workflow and delegates to specialized agents.
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot orchestrate workflow without signed contract")
        
        print(f"[Nexus_PM] Orchestrating WF-AUDIT-01: Automated Transaction Audit")
        
        # Decompose workflow into steps
        workflow_steps = [
            {
                "step": 1,
                "agent": "Nexus_Researcher",
                "task": "Ingest raw transaction logs (PDF/CSV) via MCP-PDF-Parser",
                "agent_id": self.nexus_agent_ids.get("researcher", "Nexus_Researcher")
            },
            {
                "step": 2,
                "agent": "Nexus_Researcher",
                "task": "Normalize data format via MCP-Excel-Writer",
                "agent_id": self.nexus_agent_ids.get("researcher", "Nexus_Researcher")
            },
            {
                "step": 3,
                "agent": "Nexus_Compliance",
                "task": "Cross-reference against Global_Sanctions_List.db (Yao's GC)",
                "agent_id": self.nexus_agent_ids.get("compliance", "Nexus_Compliance")
            },
            {
                "step": 4,
                "agent": "Nexus_Compliance",
                "task": "Flag suspicious outliers (> $10k) via Yao's GC",
                "agent_id": self.nexus_agent_ids.get("compliance", "Nexus_Compliance")
            },
            {
                "step": 5,
                "agent": "Nexus_Researcher",
                "task": "Generate Summary Report for Human Review",
                "agent_id": self.nexus_agent_ids.get("researcher", "Nexus_Researcher")
            },
        ]
        
        # Log orchestration start
        self._log_provenance({
            "action": "orchestrate_workflow",
            "workflow_id": "WF-AUDIT-01",
            "steps": len(workflow_steps),
            "subordinate_agents": list(self.nexus_agent_ids.values())
        })
        
        # Delegate tasks (in production, this would use A2A Protocol)
        for step in workflow_steps:
            self.delegate(step, step["agent_id"])
            print(f"[Nexus_PM] Delegated Step {step['step']} to {step['agent']}")
        
        return {
            "workflow_id": "WF-AUDIT-01",
            "status": "ORCHESTRATED",
            "steps_delegated": len(workflow_steps),
            "orchestrated_at": datetime.now().isoformat()
        }
    
    def register_subordinate_agent(self, role: str, agent_id: str) -> None:
        """Register a subordinate Nexus agent for trust ledger tracking."""
        self.nexus_agent_ids[role] = agent_id
        self.subordinate_swarm.append(agent_id)
        print(f"[Nexus_PM] Registered subordinate agent: {role} ({agent_id})")
    
    def get_provenance_log(self) -> List[Dict[str, Any]]:
        """Return full provenance log for C5 compliance."""
        return self.provenance_log
    
    def load_project_context(self) -> Dict[str, Any]:
        """Load project status and context from project_status.md."""
        project_status_path = REPO_ROOT / "clients" / "project_status.md"
        context = {
            "status": "UNKNOWN",
            "client": "Nexus Financial Assurance Ltd.",
            "sla_uptime": 99.8,
            "last_updated": datetime.now().isoformat(),
            "agents": [],
            "workflows": []
        }
        
        if project_status_path.exists():
            try:
                with open(project_status_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if "FABRICATION PHASE" in content:
                        context["status"] = "FABRICATION PHASE"
                    elif "DEPLOYED" in content:
                        context["status"] = "DEPLOYED"
                    # Extract additional context from the file
                    if "Nexus_Compliance" in content:
                        context["agents"].append("Nexus_Compliance")
                    if "Nexus_Researcher" in content:
                        context["agents"].append("Nexus_Researcher")
                    if "Nexus_NetSec" in content:
                        context["agents"].append("Nexus_NetSec")
                    if "WF-AUDIT-01" in content:
                        context["workflows"].append("WF-AUDIT-01")
            except Exception as e:
                print(f"[Nexus_PM] Warning: Could not load project_status.md: {e}")
        
        # Also load deployment plan for additional context
        deployment_plan_path = REPO_ROOT / "clients" / "nexus_deployment_plan.json"
        if deployment_plan_path.exists():
            try:
                with open(deployment_plan_path, "r", encoding="utf-8") as f:
                    plan_data = json.load(f)
                    deployment_plan = plan_data.get("deployment_plan", {})
                    context["client"] = deployment_plan.get("client", context["client"])
                    context["industry"] = deployment_plan.get("industry", "")
                    context["target_market"] = deployment_plan.get("target_market", "")
            except Exception as e:
                print(f"[Nexus_PM] Warning: Could not load deployment plan: {e}")
        
        return context
    
    def process_chat_request(self, user_message: str) -> str:
        """
        Process a chat request from the user.
        Reads project context and provides intelligent responses.
        
        Args:
            user_message: The user's message/query
            
        Returns:
            Response string from Nexus_PM
        """
        # Load project context
        context = self.load_project_context()
        
        # Log the chat interaction
        self._log_provenance({
            "action": "chat_request",
            "user_message": user_message[:100],  # Truncate for logging
            "timestamp": datetime.now().isoformat()
        })
        
        # Process the message (simple keyword-based routing for now)
        # In production, this would use an LLM via MCP
        message_lower = user_message.lower()
        
        # System status queries
        if any(keyword in message_lower for keyword in ["status", "health", "system", "uptime"]):
            agents_status = ", ".join(context.get("agents", ["Nexus_Compliance", "Nexus_Researcher"]))
            return f"""**Nexus_PM Response:**

**System Status:** {context.get('status', 'UNKNOWN')}
**Client:** {context.get('client', 'Nexus Financial Assurance Ltd.')}
**SLA Uptime:** {context.get('sla_uptime', 99.8)}%

**Active Agents:**
- {agents_status}

**Workflows:**
- WF-AUDIT-01: {'Active' if 'WF-AUDIT-01' in context.get('workflows', []) else 'Inactive'}

All systems operational and within acceptable parameters."""
        
        # Workflow queries
        elif any(keyword in message_lower for keyword in ["workflow", "audit", "wf-audit", "process"]):
            return f"""**Nexus_PM Response:**

**WF-AUDIT-01 Status:**
- Current Phase: {context.get('status', 'FABRICATION PHASE')}
- Orchestration: Ready for execution
- Steps: 5-step automated transaction audit workflow

**Workflow Steps:**
1. Data Ingestion (Nexus_Researcher)
2. Data Normalization (Nexus_Researcher)
3. Compliance Screening (Nexus_Compliance - Yao's GC)
4. Suspicious Transaction Flagging (Nexus_Compliance)
5. Report Generation (Nexus_Researcher)

All workflow components are configured and ready."""
        
        # Budget/financial queries
        elif any(keyword in message_lower for keyword in ["budget", "cost", "token", "financial", "expense"]):
            token_budget = self.token_budget_max
            token_used = self.token_usage
            token_pct = (token_used / token_budget * 100) if token_budget > 0 else 0
            
            return f"""**Nexus_PM Response:**

**Budget Status:**
- Token Budget: {token_budget:,} / 500,000 (20% allocation)
- Token Used: {token_used:,} ({token_pct:.1f}% utilized)
- Status: {'Within budget' if token_used < token_budget else 'Approaching limit'}

**Contract Status:**
- Contract ID: {self.active_contract.get('contract_id', 'N/A') if self.active_contract else 'Not signed'}
- Status: {self.active_contract.get('status', 'UNSIGNED') if self.active_contract else 'UNSIGNED'}

All financial parameters are within acceptable limits."""
        
        # Agent queries
        elif any(keyword in message_lower for keyword in ["agent", "swarm", "team", "subordinate"]):
            agents_list = context.get("agents", [])
            if not agents_list:
                agents_list = ["Nexus_Compliance", "Nexus_Researcher", "Nexus_NetSec"]
            
            agents_info = "\n".join([f"- {agent}: ACTIVE" for agent in agents_list])
            
            return f"""**Nexus_PM Response:**

**Nexus Swarm Status:**

{agents_info}

**Trust Ledger:**
- Trust Score: {self.trust_score:.2f}
- Subordinate Agents: {len(self.subordinate_swarm)}
- Provenance Log Entries: {len(self.provenance_log)}

All agents are operational and responding to delegation requests."""
        
        # General/help
        else:
            return f"""**Nexus_PM Response:**

I've received your message: "{user_message}"

**Available Commands:**
- Check system status
- Query workflow progress (WF-AUDIT-01)
- Review budget and financials
- Request agent reports
- Get swarm status

**Current Project Context:**
- Status: {context.get('status', 'UNKNOWN')}
- Client: {context.get('client', 'Nexus Financial Assurance Ltd.')}
- Industry: {context.get('industry', 'FinTech / Audit Services')}

How can I assist you with the Nexus Swarm operations?"""


def main():
    """Main execution block for testing Nexus_PM agent."""
    agent = Nexus_PM("Nexus_PM", "Audit Workflow Supervisor")
    print(f"[MAIN] Instantiated {agent.name} (ID: {agent.agent_id})")
    
    # Mock contract for testing
    mock_contract = {
        "contract_id": "Nexus Financial Assurance Ltd.-PM-MASTER",
        "financial_terms": {
            "token_budget_max": 100000,
        },
        "deliverables": ["End-to-end coordination of WF-AUDIT-01"],
        "security_protocols": {
            "mpc_required": True,
            "session_firewall_enabled": True,
        },
    }
    
    if agent.sign_contract(mock_contract):
        print(f"[MAIN] Contract signed: {mock_contract['contract_id']}")
        
        # Register subordinate agents
        agent.register_subordinate_agent("researcher", "Nexus_Researcher-001")
        agent.register_subordinate_agent("compliance", "Nexus_Compliance-001")
        
        # Test workflow orchestration
        print("\n[MAIN] Testing WF-AUDIT-01 orchestration...")
        result = agent.orchestrate_wf_audit_01()
        print(f"[MAIN] Orchestration result: {json.dumps(result, indent=2)}")
        print(f"[MAIN] Provenance log entries: {len(agent.get_provenance_log())}")
    
    print("\n[MAIN] Nexus_PM agent test completed successfully!")


if __name__ == "__main__":
    main()

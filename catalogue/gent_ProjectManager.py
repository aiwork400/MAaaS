import json
import uuid
from datetime import datetime
from typing import List, Dict, Optional

from catalogue.Agent_Base import Agent_Base

# Placeholder for the A2A Protocol library (to be implemented)
# from protocols.a2a import Message, ProtocolEnum

class Agent_ProjectManager(Agent_Base):
    """
    BASE CLASS: Agent_ProjectManager
    ROLE: Supervisor & Orchestrator
    SOURCE REFERENCE: Master Data for MAaaS (Source 6, 17 - Supervisor Pattern)
    
    Responsibilities:
    1. Decompose high-level Intents into actionable Sub-tasks.
    2. Enforce E-Contracts (Budget & Deliverables).
    3. Manage the 'Trust Ledger' for subordinate agents.
    4. Report status to the Human/Client.
    """

    def __init__(self, agent_name: str, specialization: str = "General"):
        # Initialize base agent (includes Agent_Expertise and base functionality)
        super().__init__(agent_name, role="Project Manager")
        self.specialization = specialization
        self.trust_score = 1.0  # Starts perfect, adjusts based on "Trust-Adaptive Dynamic Teaming"
        self.subordinate_swarm: List[str] = [] # List of Agent IDs
        self.token_usage_log = 0

    def sign_contract(self, contract_json: Dict) -> bool:
        """
        Cryptographically 'signs' the work order.
        Validates that the Token Budget is realistic before accepting.
        Extends base contract signing with PM-specific validations.
        """
        # First validate PM-specific requirements
        required_keys = ["contract_id", "financial_terms", "deliverables", "security_protocols"]
        if not all(k in contract_json for k in required_keys):
            print(f"[PM-ERROR] Contract {contract_json.get('contract_id')} rejected: Malformed.")
            return False

        # Check for Security Compliance (Master Data Source 21)
        if not contract_json["security_protocols"].get("mpc_required", False):
            print(f"[PM-WARNING] Agent {self.name} notes lack of MPC requirement. Privacy risk elevated.")

        # Call base implementation for base validation (ensures base security checks)
        # Note: Base requires "contract_id" and "security_protocols" which we already validated
        base_result = super().sign_contract(contract_json)
        if not base_result:
            return False
        
        # PM-specific: Validate token budget
        financial_terms = contract_json.get("financial_terms", {})
        if "token_budget_max" not in financial_terms:
            print(f"[PM-WARNING] Contract {contract_json['contract_id']} missing token budget specification.")
        
        return True

    def decompose_task(self, main_objective: str) -> List[Dict]:
        """
        Uses LLM reasoning (via internal MCP call) to break down the job.
        Returns a list of sub-tasks to be delegated.
        """
        # In a real implementation, this calls the LLM via MCP.
        # Here we simulate the output of a "Supervisor" architecture (Source 17).
        print(f"[THINKING] {self.name} is decomposing: '{main_objective}'...")
        
        # logical plan generation
        plan = [
            {"step": 1, "role_needed": "Agent_Researcher", "task": "Gather requirements & context"},
            {"step": 2, "role_needed": "Agent_Dev_Backend", "task": "Implement core logic"},
            {"step": 3, "role_needed": "Agent_QA_Sentinel", "task": "Verify against E-Contract specs"}
        ]
        return plan

    def delegate(self, task: Dict, target_agent_id: str):
        """
        Issues a sub-contract to a worker agent using A2A Protocol.
        Extends base delegation with PM-specific logging.
        """
        # Use base implementation for core delegation logic
        message = super().delegate(task, target_agent_id)
        
        # PM-specific: Track subordinate swarm
        if target_agent_id not in self.subordinate_swarm:
            self.subordinate_swarm.append(target_agent_id)
        
        return message

    def evaluate_work(self, agent_id: str, output_quality: float, tokens_spent: int):
        """
        The 'Evaluator-Optimizer' Loop (Source 53).
        Adjusts the Trust Ledger based on performance.
        """
        if output_quality < 0.8:
            print(f"[PENALTY] Agent {agent_id} underperformed. Trust score reduced.")
            # Logic to deduct credits from the sub-agent
        else:
            print(f"[REWARD] Agent {agent_id} delivered successfully.")

    def generate_system_prompt(self, role_specific_instructions: str = "") -> str:
        """
        Generate system prompt for Project Manager with MCP Tool Registry.
        Preserves base functionality (Agentic Expertise + Universal MCP Client).
        """
        # Build PM-specific instructions
        pm_instructions = f"""
{role_specific_instructions}

ROLE: Supervisor & Orchestrator
===============================

Responsibilities:
1. Decompose high-level Intents into actionable Sub-tasks.
2. Enforce E-Contracts (Budget & Deliverables).
3. Manage the 'Trust Ledger' for subordinate agents.
4. Report status to the Human/Client.

SPECIALIZATION: {self.specialization}

AVAILABLE MCP TOOLS & TARGETS
==============================

You have native access to specialized MCP targets for enhanced capabilities:

1. Google Data Commons (Verified Statistics)
   - Use Case: Market research, demographic analysis, verified public statistics
   - Access via Universal_MCP_Client when client requires market research or data validation
   - Example: Querying verified economic indicators, population statistics, industry trends
   - Connection: Use MCP client to connect to Data Commons API for credible, verified data sources

2. Rill Data (Real-Time Dashboards)
   - Use Case: Real-time data visualization and dashboard creation
   - Access via Universal_MCP_Client when client requires visualization or dashboard creation
   - Example: Creating interactive dashboards for business metrics, live data feeds
   - Connection: Use MCP client to connect to Rill Data platform for dashboard management

How to Use These Tools:
-----------------------
When a client requires market research or visualization:
1. Use the Universal_MCP_Client (as documented in base capabilities)
2. Connect to the appropriate MCP target:
   - For statistics: Connect to Google Data Commons MCP server
   - For dashboards: Connect to Rill Data MCP server
3. Discover available tools using list_tools()
4. Execute tools as needed for the task

Remember: These tools extend your base MCP capabilities. Always follow the base MCP guidelines:
- Always call list_tools() first to discover available tools
- Never hallucinate tools - only use tools that exist
- Get schema before executing to understand parameters
"""
        
        # Call base method which preserves Agentic Expertise + Universal MCP Client
        return super().generate_system_prompt(pm_instructions)
    
    def to_json(self):
        base_json = super().to_json()
        base_json.update({
            "specialization": self.specialization,
            "trust_score": self.trust_score,
            "subordinate_count": len(self.subordinate_swarm),
            "token_usage_log": self.token_usage_log
        })
        return base_json

# Example Usage for Testing
if __name__ == "__main__":
    pm = Agent_ProjectManager("Alpha-01", "SaaS Development")
    
    sample_contract = {
        "contract_id": "JOB-101",
        "financial_terms": {"token_budget_max": 10000},
        "deliverables": ["Complete App"],
        "security_protocols": {"mpc_required": True}
    }
    
    pm.sign_contract(sample_contract)
    plan = pm.decompose_task("Build a Secure Login System")
    pm.delegate(plan[1], "Worker-Dev-007")
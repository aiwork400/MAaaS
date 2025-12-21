import uuid
from datetime import datetime
from typing import Dict, Optional, List


class Agent_Researcher:
    """
    BASE CLASS: Agent_Researcher
    DEPARTMENT: Operations & Interactors (The "Hands")

    ROLE:
        - Use MCP tools to fetch and synthesize credibility-checked web/data sources.
        - Support Consultancy, Tech, and Finance workflows with grounded context.
        - Respect MPC / privacy policies when interacting with sensitive client data.

    TOOLING REFERENCE:
        - Model Context Protocol (MCP) for tool calls and context augmentation.
        - Evaluator-Optimizer pattern for iterative refinement of research outputs.
    """

    def __init__(self, agent_name: str, tool_set: Optional[List[str]] = None):
        self.agent_id = str(uuid.uuid4())
        self.name = agent_name
        self.tool_set = tool_set or ["MCP-WebSearch", "MCP-Docs"]
        self.active_contract: Optional[Dict] = None

    def sign_contract(self, contract_json: Dict) -> bool:
        """
        Contract pattern for research work:
        - Ensure security posture and approved data sources are declared.
        """
        required_keys = ["contract_id", "research_scope", "security_protocols"]
        if not all(k in contract_json for k in required_keys):
            print(f"[RESEARCH-ERROR] Contract {contract_json.get('contract_id')} rejected: Malformed.")
            return False

        security = contract_json["security_protocols"]
        if not security.get("mpc_required", False):
            print(f"[RESEARCH-WARNING] {self.name} notes missing MPC requirement for sensitive data joins.")
        if not security.get("session_firewall_enabled", False):
            print(f"[RESEARCH-WARNING] {self.name} notes missing Session Firewall (risk of context bypass C6).")

        approved_sources = contract_json["research_scope"].get("approved_sources", [])
        if not approved_sources:
            print(f"[RESEARCH-WARNING] Contract {contract_json['contract_id']} has no 'approved_sources' list.")

        self.active_contract = contract_json
        self.active_contract["status"] = "SIGNED"
        self.active_contract["signed_at"] = datetime.now().isoformat()

        print(f"[RESEARCH-INFO] Agent {self.name} accepted Contract {contract_json['contract_id']}.")
        return True

    def delegate(self, task: Dict, target_agent_id: str):
        """
        Research delegation pattern:
        - Used to pass refined requirements or synthesized findings onward
          (e.g., to Dev, Finance, or Strategy agents).
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot delegate without a signed Research Contract.")

        message = {
            "from": self.agent_id,
            "to": target_agent_id,
            "type": "RESEARCH_TASK",
            "payload": task,
            "context_file": "Client_SOPs.md",
        }

        print(f"[RESEARCH-DELEGATION] {self.name} passed research task '{task.get('task')}' to Agent {target_agent_id}.")
        return message

    def to_json(self) -> Dict:
        return {
            "agent_id": self.agent_id,
            "role": "Researcher",
            "name": self.name,
            "tools": self.tool_set,
            "status": "ACTIVE" if self.active_contract else "IDLE",
        }



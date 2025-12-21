import uuid
from datetime import datetime
from typing import Dict, Optional


class Agent_FinancialOfficer:
    """
    BASE CLASS: Agent_FinancialOfficer
    DEPARTMENT: Finance & Legal (The "Auditors")

    ROLE:
        - Optimize token usage and enforce budget constraints.
        - Generate and validate financial reports/invoices for MAaaS jobs.
        - Check that contracts respect the security posture (MPC, Firewalls).

    SECURITY REFERENCE:
        - Master Data for MAaaS (MPC & Cryptographic Security Frameworks)
        - Token Economy & E-Contracts standard (Article 2, Repo Rules)
    """

    def __init__(self, agent_name: str, access_level: str = "Read-Only (MPC Secured)"):
        self.agent_id = str(uuid.uuid4())
        self.name = agent_name
        self.access_level = access_level
        self.active_contract: Optional[Dict] = None
        self.total_tokens_spent: int = 0

    def sign_contract(self, contract_json: Dict) -> bool:
        """
        Mirror pattern from Agent_ProjectManager.sign_contract:
        - Validate schema.
        - Enforce/flag security standards (MPC requirement, session firewalls).
        """
        required_keys = ["contract_id", "financial_terms", "deliverables", "security_protocols"]
        if not all(k in contract_json for k in required_keys):
            print(f"[FINANCE-ERROR] Contract {contract_json.get('contract_id')} rejected: Malformed.")
            return False

        financial_terms = contract_json["financial_terms"]
        if "token_budget_max" not in financial_terms:
            print(f"[FINANCE-WARNING] Contract {contract_json['contract_id']} missing 'token_budget_max'.")

        # Security posture check (MPC + Session Firewalls as per Master Data)
        security = contract_json["security_protocols"]
        if not security.get("mpc_required", False):
            print(f"[FINANCE-WARNING] {self.name} notes missing MPC requirement. Privacy/integrity risk elevated.")
        if not security.get("session_firewall_enabled", False):
            print(f"[FINANCE-WARNING] {self.name} notes missing Session Firewall. Cross-agent leakage risk elevated.")

        self.active_contract = contract_json
        self.active_contract["status"] = "SIGNED"
        self.active_contract["signed_at"] = datetime.now().isoformat()

        print(f"[FINANCE-INFO] Agent {self.name} accepted Contract {contract_json['contract_id']}.")
        return True

    def delegate(self, task: Dict, target_agent_id: str):
        """
        Financial delegation pattern:
        - Used to request cost analyses, audits, or invoice generation from
          subordinate agents (e.g., analytics agents, external billing tools).
        - Follows the same A2A-style message structure as Agent_ProjectManager.
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot delegate without a signed Financial Contract.")

        message = {
            "from": self.agent_id,
            "to": target_agent_id,
            "type": "FINANCE_TASK",
            "payload": task,
            "context_file": "Client_SOPs.md",
        }

        # In a full implementation this would publish on the A2A bus.
        print(f"[FINANCE-DELEGATION] {self.name} assigned '{task.get('task')}' to Agent {target_agent_id}.")
        return message

    def record_token_spend(self, tokens: int):
        """
        Update the internal token ledger, enforcing the budget ceiling if present.
        """
        if not self.active_contract:
            print("[FINANCE-ERROR] No active contract; cannot record token spend.")
            return

        self.total_tokens_spent += tokens
        budget = self.active_contract["financial_terms"].get("token_budget_max")
        if budget is not None and self.total_tokens_spent > budget:
            print(
                f"[FINANCE-PENALTY] Agent {self.name} exceeded token budget "
                f"({self.total_tokens_spent}/{budget})."
            )
        else:
            print(
                f"[FINANCE-INFO] Agent {self.name} recorded token spend "
                f"({self.total_tokens_spent}/{budget or 'UNBOUNDED'})."
            )

    def to_json(self) -> Dict:
        return {
            "agent_id": self.agent_id,
            "role": "Financial Officer",
            "name": self.name,
            "access_level": self.access_level,
            "status": "ACTIVE" if self.active_contract else "IDLE",
            "total_tokens_spent": self.total_tokens_spent,
        }



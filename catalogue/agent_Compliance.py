import uuid
from datetime import datetime
from typing import Dict, Optional


class Agent_Compliance:
    """
    BASE CLASS: Agent_Compliance
    DEPARTMENT: Finance & Legal (The "Auditors")

    ROLE:
        - Screen transactions and entities against regulatory watchlists.
        - Enforce client-specific compliance policies (e.g., GDPR, SOX).
        - Ensure MPC-based data privacy when handling PII, as per Master Data.

    SECURITY REFERENCE:
        - Master Data for MAaaS (MPC, ZK, and verifiable execution layers).
        - Security Challenges C5 (Provenance) and C6 (Context Bypass).
    """

    def __init__(self, agent_name: str, jurisdiction: str = "EU/GDPR"):
        self.agent_id = str(uuid.uuid4())
        self.name = agent_name
        self.jurisdiction = jurisdiction
        self.active_contract: Optional[Dict] = None

    def sign_contract(self, contract_json: Dict) -> bool:
        """
        Compliance contract pattern:
        - Require explicit MPC mandate and provenance tracking.
        - Bind to specific regulatory frameworks and watchlist sources.
        """
        required_keys = ["contract_id", "policy_scope", "security_protocols", "provenance_policy"]
        if not all(k in contract_json for k in required_keys):
            print(f"[COMPLIANCE-ERROR] Contract {contract_json.get('contract_id')} rejected: Malformed.")
            return False

        security = contract_json["security_protocols"]
        if not security.get("mpc_required", False):
            print(
                f"[COMPLIANCE-WARNING] {self.name} requires MPC for PII; "
                f"non-MPC flows may violate client mandates."
            )
        if not security.get("session_firewall_enabled", False):
            print(
                f"[COMPLIANCE-WARNING] {self.name} warns about missing Session Firewall "
                f"(risk of cross-domain context bypass C6)."
            )

        provenance = contract_json["provenance_policy"]
        if provenance.get("mode") != "Full":
            print(
                f"[COMPLIANCE-WARNING] Provenance mode '{provenance.get('mode')}' "
                f"may not satisfy Full Provenance Tracking requirements (C5)."
            )

        self.active_contract = contract_json
        self.active_contract["status"] = "SIGNED"
        self.active_contract["signed_at"] = datetime.now().isoformat()

        print(f"[COMPLIANCE-INFO] Agent {self.name} accepted Contract {contract_json['contract_id']}.")
        return True

    def delegate(self, task: Dict, target_agent_id: str):
        """
        Compliance delegation pattern:
        - Forward enhanced screening tasks or escalations to other agents
          (e.g., Researcher for additional evidence or ProjectManager for
          workflow decisions).
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot delegate without a signed Compliance Contract.")

        message = {
            "from": self.agent_id,
            "to": target_agent_id,
            "type": "COMPLIANCE_TASK",
            "payload": task,
            "context_file": "Client_SOPs.md",
        }

        print(
            f"[COMPLIANCE-DELEGATION] {self.name} delegated compliance task "
            f"'{task.get('task')}' to Agent {target_agent_id}."
        )
        return message

    def to_json(self) -> Dict:
        return {
            "agent_id": self.agent_id,
            "role": "Compliance",
            "name": self.name,
            "jurisdiction": self.jurisdiction,
            "status": "ACTIVE" if self.active_contract else "IDLE",
        }



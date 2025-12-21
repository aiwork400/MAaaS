import uuid
from datetime import datetime
from typing import Dict, Optional


class Agent_Dev_Backend:
    """
    BASE CLASS: Agent_Dev_Backend
    DEPARTMENT: Engineering & Tech (The "Builders")

    ROLE:
        - Implement secure backend logic and API/DB integrations.
        - Respect MPC-aware data flows and avoid side-channel vulnerabilities.
        - Collaborate with QA and Security agents via A2A for Evaluator-Optimizer loops.

    SECURITY REFERENCE:
        - Master Data for MAaaS (MPC protocols, side-channel risks, cb-mpc audit).
    """

    def __init__(self, agent_name: str, stack: str = "Python/FastAPI", specialization: str = "Backend API"):
        self.agent_id = str(uuid.uuid4())
        self.name = agent_name
        self.stack = stack
        self.specialization = specialization
        self.active_contract: Optional[Dict] = None
        self.last_build_artifact: Optional[str] = None

    def sign_contract(self, contract_json: Dict) -> bool:
        """
        Contract pattern:
        - Validate presence of technical specs and security posture.
        - Log whether MPC, session firewalls, and side-channel constraints are in place.
        """
        required_keys = ["contract_id", "technical_spec", "security_protocols"]
        if not all(k in contract_json for k in required_keys):
            print(f"[DEV-ERROR] Contract {contract_json.get('contract_id')} rejected: Malformed.")
            return False

        security = contract_json["security_protocols"]
        if not security.get("mpc_required", False):
            print(f"[DEV-WARNING] {self.name} notes missing MPC requirement for sensitive workloads.")
        if security.get("allows_variable_time_crypto", False):
            print(
                f"[DEV-WARNING] {self.name} detected 'allows_variable_time_crypto'. "
                f"Timing side-channel risk (see cb-mpc audit)."
            )

        self.active_contract = contract_json
        self.active_contract["status"] = "SIGNED"
        self.active_contract["signed_at"] = datetime.now().isoformat()
        print(f"[DEV-INFO] Agent {self.name} accepted Contract {contract_json['contract_id']}.")
        return True

    def delegate(self, task: Dict, target_agent_id: str):
        """
        Backend delegation pattern:
        - Used to send tasks to QA, Research, or SecOps agents
          (e.g., performance tests, threat modeling, requirements refinement).
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot delegate without a signed Technical Contract.")

        message = {
            "from": self.agent_id,
            "to": target_agent_id,
            "type": "ENGINEERING_TASK",
            "payload": task,
            "context_file": "Client_SOPs.md",
        }

        print(f"[DEV-DELEGATION] {self.name} assigned '{task.get('task')}' to Agent {target_agent_id}.")
        return message

    def register_build_artifact(self, artifact_uri: str):
        """
        Save reference to the build artifact (e.g., container image, git ref).
        """
        self.last_build_artifact = artifact_uri
        print(f"[DEV-INFO] {self.name} produced build artifact at {artifact_uri}.")

    def to_json(self) -> Dict:
        return {
            "agent_id": self.agent_id,
            "role": "Backend Developer",
            "name": self.name,
            "stack": self.stack,
            "specialization": self.specialization,
            "status": "ACTIVE" if self.active_contract else "IDLE",
            "last_build_artifact": self.last_build_artifact,
        }



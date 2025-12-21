"""
Mapping-to-MAaaS process for Nexus Financial Assurance Ltd.

This script:
1. Loads the Nexus client profile.
2. Selects appropriate base agents from the MARKET_AGENT_CATALOGUE (Finance).
3. Instantiates ProjectManager, Researcher, Compliance, and FinancialOfficer.
4. Generates E-Contracts that satisfy the MPC data privacy requirements and
   Full Provenance Tracking mandates from the client profile and Master Data.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any


# Ensure repository root is on sys.path when running this script directly.
BASE_DIR = Path(__file__).resolve().parent
REPO_ROOT = BASE_DIR.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from catalogue.agent_catalogue import (  # type: ignore  # noqa
    get_default_agents_for_market,
    Agent_ProjectManager,
    Agent_FinancialOfficer,
    Agent_Researcher,
    Agent_Compliance,
)
from swarm_protocols import SECURITY_STANDARDS, describe_security_posture  # type: ignore  # noqa
PROFILE_PATH = BASE_DIR / "nexus_financial_assurance.json"


def load_client_profile() -> Dict[str, Any]:
    # Use utf-8-sig to be robust against potential BOM markers in the JSON file.
    with PROFILE_PATH.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def build_security_block(client_profile: Dict[str, Any]) -> Dict[str, Any]:
    mandates = client_profile["security_mandates"]
    return {
        "mpc_required": mandates.get("mpc_requirement", "").upper() == "TRUE",
        "mpc_justification": mandates.get("mpc_justification"),
        "session_firewall_enabled": SECURITY_STANDARDS["session_firewalls"]["enabled"],
        "session_firewall_mode": SECURITY_STANDARDS["session_firewalls"]["mode"],
        "provenance_required": "Full" in mandates.get("audit_trail", ""),
        "security_posture_summary": describe_security_posture(),
    }


def generate_econtracts(client_profile: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    company = client_profile["client_meta"]["company_name"]
    security_block = build_security_block(client_profile)
    financials = client_profile["financial_constraints"]

    # 1. Project Manager (Audit Workflow Coordinator replacement)
    pm_contract = {
        "contract_id": f"{company}-PM-MASTER",
        "financial_terms": {
            "token_budget_max": financials["total_token_budget_monthly"],
            "penalty_clause": financials["penalty_clause"],
        },
        "deliverables": ["End-to-end coordination of WF-AUDIT-01"],
        "security_protocols": security_block,
    }

    # 2. Researcher (Junior Data Analyst replacement)
    researcher_contract = {
        "contract_id": f"{company}-RES-01",
        "research_scope": {
            "workflow_ids": ["WF-AUDIT-01"],
            "approved_sources": ["MCP-PDF-Parser", "MCP-Excel-Writer", "MCP-Web-Search"],
        },
        "security_protocols": security_block,
    }

    # 3. Compliance (Compliance Screener replacement)
    compliance_contract = {
        "contract_id": f"{company}-COMP-01",
        "policy_scope": {
            "watchlists": ["Global_Sanctions_List.db"],
            "regimes": ["GDPR", "SOX"],
        },
        "security_protocols": security_block,
        "provenance_policy": {
            "mode": "Full",
            "description": "Full Provenance Tracking with neural provenance / audit logs (C5).",
        },
    }

    # 4. Financial Officer (cross-cutting token and cost auditor)
    finance_contract = {
        "contract_id": f"{company}-FIN-01",
        "financial_terms": {
            "token_budget_max": financials["total_token_budget_monthly"],
            "penalty_clause": financials["penalty_clause"],
        },
        "deliverables": ["Monthly cost and token usage reports"],
        "security_protocols": security_block,
    }

    return {
        "project_manager": pm_contract,
        "researcher": researcher_contract,
        "compliance": compliance_contract,
        "financial_officer": finance_contract,
    }


def instantiate_agents_and_sign(client_profile: Dict[str, Any]) -> Dict[str, Any]:
    # Use Finance market mapping as Nexus is FinTech / Audit Services.
    market_agents = get_default_agents_for_market("Finance")

    # Instantiate agents with Nexus-specific names.
    pm: Agent_ProjectManager = market_agents["management"]("Nexus_PM", "Audit Workflow Supervisor")
    researcher: Agent_Researcher = market_agents["research"]("Nexus_Researcher", ["MCP-PDF-Parser", "MCP-Excel-Writer"])
    compliance: Agent_Compliance = market_agents["compliance"]("Nexus_Compliance", "EU/GDPR + SOX")
    finance: Agent_FinancialOfficer = market_agents["finance"]("Nexus_Finance_Officer")

    contracts = generate_econtracts(client_profile)

    pm.sign_contract(contracts["project_manager"])
    researcher.sign_contract(contracts["researcher"])
    compliance.sign_contract(contracts["compliance"])
    finance.sign_contract(contracts["financial_officer"])

    return {
        "agents": {
            "project_manager": pm.to_json(),
            "researcher": researcher.to_json(),
            "compliance": compliance.to_json(),
            "financial_officer": finance.to_json(),
        },
        "contracts": contracts,
    }


def main() -> None:
    profile = load_client_profile()
    result = instantiate_agents_and_sign(profile)
    output_path = BASE_DIR / "nexus_mapping_output.json"
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"[MAPPING] Nexus Mapping-to-MAaaS completed. Output written to {output_path}.")


if __name__ == "__main__":
    main()



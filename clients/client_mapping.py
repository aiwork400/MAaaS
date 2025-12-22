"""
Client Mapping Utilities
=========================

Generic client mapping functions for the Swarm Factory.
These functions were previously client-specific but are now generalized
for use with any client profile.
"""

from typing import Dict, Any, List
from pathlib import Path
import json


def load_client_profile(profile_path: Path) -> Dict[str, Any]:
    """
    Load and parse a client profile JSON file.
    
    Args:
        profile_path: Path to the client profile JSON file
        
    Returns:
        Dictionary containing the client profile data
        
    Raises:
        FileNotFoundError: If profile file doesn't exist
        json.JSONDecodeError: If file is not valid JSON
    """
    if not profile_path.exists():
        raise FileNotFoundError(f"Client profile not found at {profile_path}")
    
    # Try multiple encodings
    for encoding in ["utf-8-sig", "utf-8", "latin-1", "cp1252"]:
        try:
            with open(profile_path, "r", encoding=encoding) as f:
                content = f.read()
                # Remove any BOM or null bytes
                content = content.replace('\x00', '').strip()
                if content.startswith('\ufeff'):
                    content = content[1:]
                return json.loads(content)
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    
    # Last resort: read as binary
    with open(profile_path, "rb") as f:
        content = f.read()
        start_idx = content.find(b'{')
        if start_idx >= 0:
            content = content[start_idx:]
            text = content.decode('utf-8', errors='ignore')
            return json.loads(text)
    
    raise ValueError(f"Could not decode client profile file: {profile_path}")


def generate_econtracts(client_profile: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Generate E-Contracts for base agents (Compliance, Researcher, PM).
    
    Args:
        client_profile: Client profile dictionary
        
    Returns:
        Dictionary mapping agent types to their E-Contract definitions
    """
    company = client_profile.get("client_meta", {}).get("company_name", "Client")
    financials = client_profile.get("financial_constraints", {})
    base_budget = financials.get("total_token_budget_monthly", 500000)
    
    contracts = {}
    
    # Compliance Agent Contract
    contracts["compliance"] = {
        "contract_id": f"{company}-COMPLIANCE-01",
        "agent_role": "Agent_Compliance",
        "financial_terms": {
            "token_budget_max": int(base_budget * 0.15),  # 15% of total
            "reward_pool": 100,
            "penalty_condition": "Security Vulnerability or Token Overrun"
        },
        "security_protocols": {
            "mpc_required": True,
            "session_firewall_enabled": True,
            "provenance_tracking": "Full"
        },
        "policy_scope": {
            "jurisdiction": client_profile.get("client_meta", {}).get("jurisdiction", "EU/GDPR"),
            "watchlist_sources": ["OFAC", "EU_Sanctions", "PEP"]
        },
        "provenance_policy": {
            "mode": "Full",
            "log_all_operations": True
        }
    }
    
    # Researcher Agent Contract
    contracts["researcher"] = {
        "contract_id": f"{company}-RESEARCHER-01",
        "agent_role": "Agent_Researcher",
        "financial_terms": {
            "token_budget_max": int(base_budget * 0.20),  # 20% of total
            "reward_pool": 100,
            "penalty_condition": "Inaccurate Research or Token Overrun"
        },
        "security_protocols": {
            "mpc_required": True,
            "session_firewall_enabled": True
        },
        "research_scope": {
            "approved_sources": ["MCP-WebSearch", "MCP-Docs", "MCP-PDF-Parser"],
            "data_quality_requirements": "Credibility-checked sources only"
        }
    }
    
    # Project Manager Contract
    contracts["pm"] = {
        "contract_id": f"{company}-PM-01",
        "agent_role": "Agent_ProjectManager",
        "financial_terms": {
            "token_budget_max": int(base_budget * 0.25),  # 25% of total
            "reward_pool": 150,
            "penalty_condition": "Project Failure or Token Overrun"
        },
        "security_protocols": {
            "mpc_required": True,
            "session_firewall_enabled": True
        },
        "deliverables": {
            "workflow_coordination": True,
            "status_reporting": True,
            "trust_ledger_management": True
        }
    }
    
    return contracts


def build_security_block(client_profile: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build security configuration block for client deployment.
    
    Args:
        client_profile: Client profile dictionary
        
    Returns:
        Dictionary containing security configuration
    """
    security_requirements = client_profile.get("security_requirements", {})
    financials = client_profile.get("financial_constraints", {})
    
    security_block = {
        "mpc_required": security_requirements.get("mpc_required", True),
        "session_firewall_enabled": security_requirements.get("session_firewall_enabled", True),
        "provenance_tracking": security_requirements.get("provenance_tracking", "Full"),
        "encryption_at_rest": security_requirements.get("encryption_at_rest", True),
        "encryption_in_transit": security_requirements.get("encryption_in_transit", True),
        "access_control": {
            "role_based": True,
            "audit_logging": True
        },
        "compliance_frameworks": security_requirements.get("compliance_frameworks", ["GDPR"]),
        "penalty_clause": financials.get("penalty_clause", "Standard SLA penalties apply")
    }
    
    return security_block


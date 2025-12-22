"""
Agent Catalogue for MAaaS

This module exposes the Swarm Agency's base agent classes and maps them to
research-backed target markets: Consultancy, Tech, and Finance.

Security & Architecture Reference:
- Master Data for MAaaS (file:///c%3A/Users/PC/MAaaS/Master%20Data%20for%20MAaaS.pdf)
- MPC, MCP, and A2A-based multi-agent patterns (Supervisor, Evaluator-Optimizer).

Base Agent Class:
- Agent_Base: Core agent template with MCP capability for external tool access
"""

from typing import Dict, Type

from catalogue.Agent_Base import Agent_Base, generate_agent_system_prompt
from catalogue.gent_ProjectManager import Agent_ProjectManager
from catalogue.agent_FinancialOfficer import Agent_FinancialOfficer
from catalogue.agent_Dev_Backend import Agent_Dev_Backend
from catalogue.agent_Researcher import Agent_Researcher
from catalogue.agent_Compliance import Agent_Compliance


# High-level view of which base agents are relevant to which market verticals.
MARKET_AGENT_CATALOGUE: Dict[str, Dict[str, Type]] = {
    "Consultancy": {
        "management": Agent_ProjectManager,
        "research": Agent_Researcher,
        "finance": Agent_FinancialOfficer,
    },
    "Tech": {
        "management": Agent_ProjectManager,
        "engineering_backend": Agent_Dev_Backend,
        "research": Agent_Researcher,
    },
    "Finance": {
        "management": Agent_ProjectManager,
        "finance": Agent_FinancialOfficer,
        "research": Agent_Researcher,
        "compliance": Agent_Compliance,
    },
}


def get_default_agents_for_market(market: str) -> Dict[str, Type]:
    """
    Return the default role->AgentClass mapping for a given market.
    This is the entrypoint for the Mapping-to-MAaaS process once a Client Profile
    is provided.
    """
    key = market.strip().title()
    if key not in MARKET_AGENT_CATALOGUE:
        raise KeyError(f"Unknown market '{market}'. Known: {list(MARKET_AGENT_CATALOGUE.keys())}")
    return MARKET_AGENT_CATALOGUE[key]


__all__ = [
    "Agent_Base",
    "generate_agent_system_prompt",
    "Agent_ProjectManager",
    "Agent_FinancialOfficer",
    "Agent_Dev_Backend",
    "Agent_Researcher",
    "Agent_Compliance",
    "MARKET_AGENT_CATALOGUE",
    "get_default_agents_for_market",
]



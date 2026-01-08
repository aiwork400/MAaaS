"""
ExecutiveLiaison Agent Package

Provides executive communication and reporting capabilities.
"""

from pathlib import Path
from agency_swarm import Agent

# Read instructions from the instructions.md file
_instruct_path = Path(__file__).parent / "instructions.md"
with open(_instruct_path, "r", encoding="utf-8") as f:
    _instructions = f.read()


class ExecutiveLiaison(Agent):
    """
    Executive Liaison Agent for MAaaS
    
    Serves as the primary interface between the MAaaS ecosystem and client executives.
    Handles executive communication, status reporting, and strategic alignment.
    """
    
    def __init__(self, name: str = "ExecutiveLiaison", **kwargs):
        super().__init__(
            name=name,
            instructions=_instructions,
            **kwargs
        )


# Export both the class and the tools
from agency.ExecutiveLiaison.tools import (
    ExecutiveReportingTool,
    ExecutiveCommunicationTool,
    reporting_tool,
    communication_tool
)

__all__ = [
    'ExecutiveLiaison',
    'ExecutiveReportingTool',
    'ExecutiveCommunicationTool',
    'reporting_tool',
    'communication_tool'
]

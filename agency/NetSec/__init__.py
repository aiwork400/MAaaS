"""
NetSec Agent Package

Network Security Sentinel for auditing and compliance monitoring.
"""

from pathlib import Path
from agency_swarm import Agent
from agency_swarm.tools import BaseTool

# Read instructions from the instructions.md file
_instruct_path = Path(__file__).parent / "instructions.md"
with open(_instruct_path, "r", encoding="utf-8") as f:
    _instructions = f.read()

# Import tools
from agency.NetSec.tools import AuditLog, VerifyEncryption


class NetSec(Agent):
    """
    Network Security Sentinel Agent for MAaaS
    
    Responsible for auditing and enforcing crypto-contracts.
    Monitors swarm communications for contract violations, PII leaks, and unauthorized access.
    """
    
    def __init__(self, name: str = "NetSec", **kwargs):
        super().__init__(
            name=name,
            instructions=_instructions,
            tools=[AuditLog, VerifyEncryption],
            **kwargs
        )


__all__ = ['NetSec', 'AuditLog', 'VerifyEncryption']

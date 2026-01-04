#!/usr/bin/env python3
"""
ApexGrowthSystems_Researcher: Specialized Researcher Agent for Nexus Financial Assurance Ltd.

This agent implements:
- MCP integration for PDF parsing and Excel writing (WF-AUDIT-01 Steps 1-2)
- MPC-aware data processing for PII protection
- Full provenance tracking (C5 compliance)

Reference: Nexus Swarm Deployment Plan (clients/nexus_deployment_plan.md)
"""

import sys
import os
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Add repository root to path for imports
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from catalogue.agent_Researcher import Agent_Researcher


class MCPClient:
    """
    Model Context Protocol (MCP) client for data processing tools.
    
    Implements MCP-PDF-Parser and MCP-Excel-Writer for WF-AUDIT-01.
    """
    
    @staticmethod
    def parse_pdf(input_file: str, mpc_mode: bool = True) -> Dict[str, Any]:
        """
        Parse PDF transaction logs using MCP-PDF-Parser.
        
        In MPC mode, PII remains encrypted during parsing.
        """
        mcp_call = {
            "tool": "MCP-PDF-Parser",
            "params": {
                "input_file": input_file,
                "output_format": "structured_json",
                "mpc_mode": mpc_mode
            }
        }
        
        # Simulated MCP call (in production, this interfaces with MCP server)
        print(f"[MCP] Parsing PDF: {input_file} (MPC mode: {mpc_mode})")
        
        # Mock parsed data (in production, comes from MCP server)
        mock_data = {
            "file": input_file,
            "transactions": [
                {"transaction_id": "TX-001", "amount_encrypted": "encrypted_value_1"},
                {"transaction_id": "TX-002", "amount_encrypted": "encrypted_value_2"},
            ],
            "parsed_at": datetime.now().isoformat(),
            "mpc_mode": mpc_mode
        }
        
        return mock_data
    
    @staticmethod
    def write_excel(data: Dict[str, Any], template: str = "Nexus_Audit_Template.xlsx", 
                   mpc_mode: bool = True) -> str:
        """
        Write normalized data to Excel using MCP-Excel-Writer.
        
        In MPC mode, data remains encrypted in intermediate storage.
        """
        mcp_call = {
            "tool": "MCP-Excel-Writer",
            "params": {
                "data": data,
                "template": template,
                "mpc_mode": mpc_mode
            }
        }
        
        print(f"[MCP] Writing Excel: {template} (MPC mode: {mpc_mode})")
        
        # Mock output path
        output_path = f"normalized_transactions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        return output_path


class ApexGrowthSystems_Researcher(Agent_Researcher):
    """
    Specialized Researcher Agent for Nexus Financial Assurance Ltd.
    
    Inherits from Agent_Researcher and extends with:
    - MCP tool integration for PDF/Excel processing
    - MPC-aware data normalization
    - Full provenance tracking (C5 compliance)
    """
    
    def __init__(self, agent_name: str = "ApexGrowthSystems_Researcher", 
                 tool_set: Optional[List[str]] = None):
        if tool_set is None:
            tool_set = ["MCP-PDF-Parser", "MCP-Excel-Writer", "MCP-Web-Search"]
        super().__init__(agent_name, tool_set)
        self.mcp_client = MCPClient()
        self.provenance_log: List[Dict[str, Any]] = []
        self.token_usage = 0
        self.token_budget_max = 200000  # Per Deployment Plan: 200k tokens (40% of 500k)
    
    def _log_provenance(self, event: Dict[str, Any]) -> None:
        """Log provenance information for C5 compliance."""
        event["provenance_id"] = hashlib.sha256(
            json.dumps(event, sort_keys=True).encode()
        ).hexdigest()[:16]
        event["agent_id"] = self.agent_id
        event["timestamp"] = datetime.now().isoformat()
        self.provenance_log.append(event)
    
    def process_wf_audit_01_step1(self, pdf_file: str) -> Dict[str, Any]:
        """
        Execute Step 1 of WF-AUDIT-01: Ingest raw transaction logs (PDF/CSV).
        
        Uses MCP-PDF-Parser with MPC mode enabled.
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot process workflow without signed contract")
        
        print(f"[ApexGrowthSystems_Researcher] Processing WF-AUDIT-01 Step 1: PDF ingestion")
        
        # Parse PDF via MCP (MPC mode enabled)
        parsed_data = self.mcp_client.parse_pdf(pdf_file, mpc_mode=True)
        
        # Log provenance
        self._log_provenance({
            "action": "parse_pdf",
            "input_file": pdf_file,
            "mcp_tool": "MCP-PDF-Parser",
            "mpc_mode": True,
            "output_hash": hashlib.sha256(
                json.dumps(parsed_data, sort_keys=True).encode()
            ).hexdigest()[:16]
        })
        
        return parsed_data
    
    def process_wf_audit_01_step2(self, parsed_data: Dict[str, Any]) -> str:
        """
        Execute Step 2 of WF-AUDIT-01: Normalize data format.
        
        Uses MCP-Excel-Writer to create standardized transaction records.
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot process workflow without signed contract")
        
        print(f"[ApexGrowthSystems_Researcher] Processing WF-AUDIT-01 Step 2: Data normalization")
        
        # Write normalized data to Excel via MCP (MPC mode enabled)
        output_path = self.mcp_client.write_excel(parsed_data, mpc_mode=True)
        
        # Log provenance
        self._log_provenance({
            "action": "normalize_data",
            "mcp_tool": "MCP-Excel-Writer",
            "mpc_mode": True,
            "output_file": output_path
        })
        
        return output_path
    
    def get_provenance_log(self) -> List[Dict[str, Any]]:
        """Return full provenance log for C5 compliance."""
        return self.provenance_log


def main():
    """Main execution block for testing ApexGrowthSystems_Researcher agent."""
    agent = ApexGrowthSystems_Researcher("ApexGrowthSystems_Researcher", ["MCP-PDF-Parser", "MCP-Excel-Writer"])
    print(f"[MAIN] Instantiated {agent.name} (ID: {agent.agent_id})")
    
    # Mock contract for testing
    mock_contract = {
        "contract_id": "Nexus Financial Assurance Ltd.-RES-01",
        "research_scope": {
            "workflow_ids": ["WF-AUDIT-01"],
            "approved_sources": ["MCP-PDF-Parser", "MCP-Excel-Writer", "MCP-Web-Search"],
        },
        "security_protocols": {
            "mpc_required": True,
            "session_firewall_enabled": True,
        },
    }
    
    if agent.sign_contract(mock_contract):
        print(f"[MAIN] Contract signed: {mock_contract['contract_id']}")
        
        # Test workflow execution
        print("\n[MAIN] Testing WF-AUDIT-01 Steps 1-2...")
        step1_result = agent.process_wf_audit_01_step1("transaction_logs.pdf")
        step2_result = agent.process_wf_audit_01_step2(step1_result)
        
        print(f"[MAIN] Step 1 result: {len(step1_result.get('transactions', []))} transactions parsed")
        print(f"[MAIN] Step 2 result: Normalized data written to {step2_result}")
        print(f"[MAIN] Provenance log entries: {len(agent.get_provenance_log())}")
    
    print("\n[MAIN] ApexGrowthSystems_Researcher agent test completed successfully!")


if __name__ == "__main__":
    main()

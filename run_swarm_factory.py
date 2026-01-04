#!/usr/bin/env python3
"""
Swarm Agency Factory Pipeline
Prime Orchestrator - Automated Agent Fabrication System

This script implements the Factory Pipeline lifecycle:
1. Intake: Load client profile and validate
2. Mapping: Map client roles to agent catalogue
3. Approval: Review and approve agent generation plan
4. Fabrication: Generate specialized agent instances

Reference: Master Data for MAaaS.pdf
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

try:
    from rich.console import Console  # type: ignore
    from rich.panel import Panel  # type: ignore
    from rich.table import Table  # type: ignore
    from rich.prompt import Confirm, Prompt  # type: ignore
    from rich.progress import Progress, SpinnerColumn, TextColumn  # type: ignore
    from rich.markdown import Markdown  # type: ignore
except ImportError:
    print("ERROR: 'rich' library not installed. Please run: pip install rich")
    sys.exit(1)

# Add repository root to path
REPO_ROOT = Path(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from catalogue.agent_catalogue import get_default_agents_for_market
from catalogue.Agent_DBA import Agent_DBA
from catalogue.Agent_NetSec import Agent_NetSec
from catalogue.Agent_Marketer import Agent_Marketer
from clients.client_mapping import (
    load_client_profile,
    generate_econtracts,
    build_security_block,
)

console = Console()


class SwarmFactory:
    """Main factory orchestrator for agent fabrication."""
    
    def __init__(self, profile_path: Optional[Path] = None, auto_approve: bool = False):
        self.client_profile: Optional[Dict[str, Any]] = None
        self.client_name: str = ""
        self.client_dir: Path = REPO_ROOT / "clients"
        self.profile_path: Optional[Path] = profile_path
        self.client_dir_name: str = ""  # Will be set based on client name
        self.nexus_dir: Path = self.client_dir / "Nexus"  # Default, will be updated
        self.auto_approve = auto_approve
        self.agent_templates = {
            "Nexus_Compliance": {
                "base_class": "Agent_Compliance",
                "file": "Nexus_Compliance.py",
                "description": "Compliance Screener with Yao's GC for watchlist matching"
            },
            "Nexus_Researcher": {
                "base_class": "Agent_Researcher",
                "file": "Nexus_Researcher.py",
                "description": "Data Analyst with MCP tools for PDF/Excel processing"
            },
            "Nexus_PM": {
                "base_class": "Agent_ProjectManager",
                "file": "Nexus_PM.py",
                "description": "Audit Workflow Coordinator (Supervisor Pattern)"
            },
            "Nexus_DBA": {
                "base_class": "Agent_DBA",
                "file": "Nexus_DBA.py",
                "description": "Database Architect with Blind Indexing (ORAM) for PII protection"
            },
            "Nexus_NetSec": {
                "base_class": "Agent_NetSec",
                "file": "Nexus_NetSec.py",
                "description": "Network Security Sentinel with Session Firewall (C6 protection)"
            },
            "Nexus_Marketer": {
                "base_class": "Agent_Marketer",
                "file": "Nexus_Marketer.py",
                "description": "Growth Officer for Omnichannel Marketing & BI"
            },
        }
        self.detected_triggers: List[str] = []
    
    def stage_intake(self) -> bool:
        """Stage 1: Intake - Load and validate client profile."""
        console.print("\n[bold cyan]===========================================================[/bold cyan]")
        console.print("[bold cyan]STAGE 1: INTAKE[/bold cyan]")
        console.print("[bold cyan]===========================================================[/bold cyan]\n")
        
        # Use provided profile path or default
        if self.profile_path is None:
            profile_path = self.client_dir / "nexus_financial_assurance.json"
        else:
            profile_path = self.profile_path
        
        if not profile_path.exists():
            console.print(f"[red]ERROR: Client profile not found at {profile_path}[/red]")
            return False
        
        try:
            # Try multiple encodings and handle binary files
            for encoding in ["utf-8-sig", "utf-8", "latin-1", "cp1252"]:
                try:
                    with open(profile_path, "r", encoding=encoding) as f:
                        content = f.read()
                        # Remove any BOM or null bytes
                        content = content.replace('\x00', '').strip()
                        if content.startswith('\ufeff'):
                            content = content[1:]
                        self.client_profile = json.loads(content)
                    break
                except (UnicodeDecodeError, json.JSONDecodeError) as e:
                    if encoding == "cp1252":  # Last attempt
                        console.print(f"[yellow]Warning: Encoding issue, trying binary read...[/yellow]")
                        # Last resort: read as binary and decode
                        with open(profile_path, "rb") as f:
                            content = f.read()
                            # Try to find JSON start
                            start_idx = content.find(b'{')
                            if start_idx >= 0:
                                content = content[start_idx:]
                                # Try UTF-8 decode
                                try:
                                    text = content.decode('utf-8', errors='ignore')
                                    self.client_profile = json.loads(text)
                                    break
                                except:
                                    pass
                    continue
            
            if self.client_profile is None:
                console.print("[red]ERROR: Could not decode client profile file[/red]")
                console.print("[yellow]Creating mock profile for testing...[/yellow]")
                # Create a minimal mock profile for testing
                self.client_profile = {
                    "client_meta": {
                        "company_name": "Nexus Financial Assurance Ltd.",
                        "industry": "FinTech / Audit Services",
                        "size": "Mid-Market (50 employees)",
                        "primary_pain_point": "Manual compliance checks are too slow and prone to human error. Data privacy is critical."
                    },
                    "organizational_structure": {
                        "human_roles": [],
                        "maas_replacement_opportunities": []
                    },
                    "sops_and_workflows": [],
                    "security_mandates": {
                        "protocol_level": "High",
                        "mpc_requirement": "TRUE",
                        "mpc_justification": "Client data contains PII",
                        "audit_trail": "Full Provenance Tracking (C5) required."
                    },
                    "financial_constraints": {
                        "total_token_budget_monthly": 500000,
                        "penalty_clause": "Any data leak results in immediate contract termination."
                    }
                }
            
            self.client_name = self.client_profile.get("client_meta", {}).get("company_name", 
                               self.client_profile.get("client_name", "Unknown Client"))
            
            # Set client directory name (sanitized from client name)
            import re
            self.client_dir_name = re.sub(r'[^\w\s-]', '', self.client_name).strip().replace(' ', '_')
            self.nexus_dir = self.client_dir / self.client_dir_name
            
            # Update agent templates to use client prefix instead of "Nexus"
            client_prefix = self.client_dir_name.replace('_', '')
            self.agent_templates = {
                f"{client_prefix}_Compliance": {
                    "base_class": "Agent_Compliance",
                    "file": f"{client_prefix}_Compliance.py",
                    "description": "Compliance Screener with Yao's GC for watchlist matching"
                },
                f"{client_prefix}_Researcher": {
                    "base_class": "Agent_Researcher",
                    "file": f"{client_prefix}_Researcher.py",
                    "description": "Data Analyst with MCP tools for PDF/Excel processing"
                },
                f"{client_prefix}_PM": {
                    "base_class": "Agent_ProjectManager",
                    "file": f"{client_prefix}_PM.py",
                    "description": "Audit Workflow Coordinator (Supervisor Pattern)"
                },
                f"{client_prefix}_DBA": {
                    "base_class": "Agent_DBA",
                    "file": f"{client_prefix}_DBA.py",
                    "description": "Database Architect with Blind Indexing (ORAM) for PII protection"
                },
                f"{client_prefix}_NetSec": {
                    "base_class": "Agent_NetSec",
                    "file": f"{client_prefix}_NetSec.py",
                    "description": "Network Security Sentinel with Session Firewall (C6 protection)"
                },
                f"{client_prefix}_Marketer": {
                    "base_class": "Agent_Marketer",
                    "file": f"{client_prefix}_Marketer.py",
                    "description": "Growth Officer for Omnichannel Marketing & BI"
                },
            }
            
            # Display client info
            table = Table(title="Client Profile Loaded", show_header=True, header_style="bold magenta")
            table.add_column("Field", style="cyan")
            table.add_column("Value", style="green")
            
            table.add_row("Company", self.client_name)
            table.add_row("Industry", self.client_profile["client_meta"]["industry"])
            table.add_row("Size", self.client_profile["client_meta"]["size"])
            table.add_row("Primary Pain Point", self.client_profile["client_meta"]["primary_pain_point"])
            
            console.print(table)
            
            # Analyze triggers for new 5-Pillar agents
            self._analyze_triggers()
            
            console.print(f"\n[green][OK] Client profile loaded successfully[/green]")
            return True
            
        except Exception as e:
            console.print(f"[red]ERROR loading client profile: {e}[/red]")
            return False
    
    def _analyze_triggers(self) -> None:
        """
        Analyze client profile for triggers that recommend new 5-Pillar agents.
        
        Data Triggers: "Legacy Data," "Slow Queries," "Unstructured Docs" → Agent_DBA
        Security Triggers: "Compliance," "PII," "Finance," "Health" → Agent_NetSec
        Growth Triggers: "Sales," "Marketing," "Customer Acquisition" → Agent_Marketer
        """
        if not self.client_profile:
            return
        
        # Combine all text fields for analysis
        text_to_analyze = []
        text_to_analyze.append(self.client_profile.get("client_meta", {}).get("primary_pain_point", ""))
        text_to_analyze.append(self.client_profile.get("client_meta", {}).get("industry", ""))
        
        # Check workflows and SOPs
        for workflow in self.client_profile.get("sops_and_workflows", []):
            text_to_analyze.append(workflow.get("name", ""))
            text_to_analyze.append(" ".join(workflow.get("steps", [])))
        
        # Check organizational structure
        for opp in self.client_profile.get("organizational_structure", {}).get("maas_replacement_opportunities", []):
            text_to_analyze.append(opp.get("current_task", ""))
            text_to_analyze.append(opp.get("mapping_requirement", ""))
        
        combined_text = " ".join(text_to_analyze).lower()
        
        # Data Triggers (strict matching for primary triggers, with fallback)
        data_primary = ["legacy data", "slow queries", "unstructured docs"]
        data_fallback = ["database", "sql", "vector store", "rag", "knowledge graph", "data migration", "schema"]
        if any(trigger in combined_text for trigger in data_primary) or \
           any(trigger in combined_text for trigger in data_fallback):
            self.detected_triggers.append("DATA")
            console.print(f"[yellow][TRIGGER] Data triggers detected -> Recommending Agent_DBA[/yellow]")
        
        # Security Triggers (strict matching for primary triggers, with fallback)
        security_primary = ["compliance", "pii", "finance", "health"]
        security_fallback = ["security", "vulnerability", "firewall", "audit", "gdpr", "sox", "hipaa", "cyber"]
        if any(trigger in combined_text for trigger in security_primary) or \
           any(trigger in combined_text for trigger in security_fallback):
            self.detected_triggers.append("SECURITY")
            console.print(f"[yellow][TRIGGER] Security triggers detected -> Recommending Agent_NetSec[/yellow]")
        
        # Growth Triggers (strict matching for primary triggers, with fallback)
        growth_primary = ["sales", "marketing", "customer acquisition"]
        growth_fallback = ["roi", "campaign", "growth", "revenue", "conversion", "analytics", "bi", "business intelligence"]
        if any(trigger in combined_text for trigger in growth_primary) or \
           any(trigger in combined_text for trigger in growth_fallback):
            self.detected_triggers.append("GROWTH")
            console.print(f"[yellow][TRIGGER] Growth triggers detected -> Recommending Agent_Marketer[/yellow]")
        
        if not self.detected_triggers:
            console.print(f"[dim]No 5-Pillar triggers detected in client profile[/dim]")
    
    def stage_mapping(self) -> Dict[str, Any]:
        """Stage 2: Mapping - Map client roles to agent catalogue."""
        console.print("\n[bold cyan]===========================================================[/bold cyan]")
        console.print("[bold cyan]STAGE 2: MAPPING[/bold cyan]")
        console.print("[bold cyan]===========================================================[/bold cyan]\n")
        
        # Determine market from client profile
        industry = self.client_profile["client_meta"]["industry"]
        if "FinTech" in industry or "Finance" in industry:
            market = "Finance"
        elif "Tech" in industry or "Software" in industry:
            market = "Tech"
        else:
            market = "Consultancy"
        
        console.print(f"[yellow]Detected Market: {market}[/yellow]\n")
        
        # Get agent catalogue for market
        market_agents = get_default_agents_for_market(market)
        
        # Map client roles to agents
        mapping = {
            "target_market": market,
            "agents_to_fabricate": [],
            "existing_agents": [],
        }
        
        # Check which agents already exist
        self.nexus_dir.mkdir(parents=True, exist_ok=True)
        
        # Always include base agents (Compliance, Researcher, PM) - use client prefix
        client_prefix = self.client_dir_name.replace('_', '')
        base_agents = [f"{client_prefix}_Compliance", f"{client_prefix}_Researcher", f"{client_prefix}_PM"]
        
        # Add 5-Pillar agents based on detected triggers
        pillar_agents = []
        if "DATA" in self.detected_triggers:
            pillar_agents.append(f"{client_prefix}_DBA")
        if "SECURITY" in self.detected_triggers:
            pillar_agents.append(f"{client_prefix}_NetSec")
        if "GROWTH" in self.detected_triggers:
            pillar_agents.append(f"{client_prefix}_Marketer")
        
        # Check all relevant agents
        agents_to_check = base_agents + pillar_agents
        
        for agent_name in agents_to_check:
            if agent_name not in self.agent_templates:
                continue
                
            agent_info = self.agent_templates[agent_name]
            agent_file = self.nexus_dir / agent_info["file"]
            
            if agent_file.exists():
                mapping["existing_agents"].append({
                    "name": agent_name,
                    "file": agent_info["file"],
                    "status": "EXISTS"
                })
                console.print(f"[green][OK] {agent_name} already exists ({agent_info['file']})[/green]")
            else:
                mapping["agents_to_fabricate"].append({
                    "name": agent_name,
                    "base_class": agent_info["base_class"],
                    "file": agent_info["file"],
                    "description": agent_info["description"],
                    "status": "TO_FABRICATE",
                    "trigger": self._get_trigger_for_agent(agent_name)
                })
                trigger_note = f" (trigger: {mapping['agents_to_fabricate'][-1]['trigger']})" if mapping['agents_to_fabricate'][-1]['trigger'] else ""
                console.print(f"[yellow][->] {agent_name} needs fabrication ({agent_info['file']}){trigger_note}[/yellow]")
        
        # Display mapping table
        table = Table(title="Agent Mapping Plan", show_header=True, header_style="bold magenta")
        table.add_column("Agent", style="cyan")
        table.add_column("Base Class", style="yellow")
        table.add_column("Status", style="green")
        table.add_column("Description", style="white")
        
        for agent in mapping["existing_agents"]:
            table.add_row(agent["name"], "-", "[green]EXISTS[/green]", "-")
        
        for agent in mapping["agents_to_fabricate"]:
            table.add_row(
                agent["name"],
                agent["base_class"],
                "[yellow]TO_FABRICATE[/yellow]",
                agent["description"]
            )
        
        console.print("\n")
        console.print(table)
        
        return mapping
    
    def _get_trigger_for_agent(self, agent_name: str) -> str:
        """Get the trigger that recommended this agent."""
        if "_DBA" in agent_name:
            return "DATA" if "DATA" in self.detected_triggers else ""
        elif "_NetSec" in agent_name:
            return "SECURITY" if "SECURITY" in self.detected_triggers else ""
        elif "_Marketer" in agent_name:
            return "GROWTH" if "GROWTH" in self.detected_triggers else ""
        return ""
    
    def stage_approval(self, mapping: Dict[str, Any]) -> bool:
        """Stage 3: Approval - Review and approve fabrication plan."""
        console.print("\n[bold cyan]===========================================================[/bold cyan]")
        console.print("[bold cyan]STAGE 3: APPROVAL[/bold cyan]")
        console.print("[bold cyan]===========================================================[/bold cyan]\n")
        
        # Display summary
        existing_count = len(mapping["existing_agents"])
        to_fabricate_count = len(mapping["agents_to_fabricate"])
        
        summary = f"""
**Fabrication Plan Summary:**

- **Target Market:** {mapping['target_market']}
- **Existing Agents:** {existing_count} (will be skipped)
- **Agents to Fabricate:** {to_fabricate_count}

**Agents to Generate:**
"""
        for agent in mapping["agents_to_fabricate"]:
            summary += f"\n- **{agent['name']}** ({agent['base_class']}): {agent['description']}"
        
        if existing_count > 0:
            summary += f"\n\n**Existing Agents (Skipped):**"
            for agent in mapping["existing_agents"]:
                summary += f"\n- **{agent['name']}** (already exists)"
        
        console.print(Panel(Markdown(summary), title="Fabrication Plan", border_style="cyan"))
        
        # Request approval
        if to_fabricate_count == 0:
            console.print("\n[green]All agents already exist. No fabrication needed.[/green]")
            return True
        
        if self.auto_approve:
            console.print("[green]Auto-approval enabled: Proceeding with fabrication...[/green]")
            return True
        
        approved = Confirm.ask("\n[bold]Approve fabrication plan?[/bold]", default=True)
        return approved
    
    def fabricate_agent(self, agent_info: Dict[str, Any]) -> bool:
        """Fabricate a single agent instance."""
        agent_name = agent_info["name"]
        base_class = agent_info["base_class"]
        file_name = agent_info["file"]
        
        console.print(f"\n[bold yellow]Fabricating {agent_name}...[/bold yellow]")
        
        # Generate agent code based on base class
        if base_class == "Agent_Researcher":
            return self._fabricate_researcher(agent_name, file_name)
        elif base_class == "Agent_ProjectManager":
            return self._fabricate_pm(agent_name, file_name)
        elif base_class == "Agent_DBA":
            return self._fabricate_dba(agent_name, file_name)
        elif base_class == "Agent_NetSec":
            return self._fabricate_netsec(agent_name, file_name)
        elif base_class == "Agent_Marketer":
            return self._fabricate_marketer(agent_name, file_name)
        else:
            console.print(f"[red]Unknown base class: {base_class}[/red]")
            return False
    
    def _fabricate_researcher(self, agent_name: str, file_name: str) -> bool:
        """Generate Nexus_Researcher.py specialized agent."""
        agent_path = self.nexus_dir / file_name
        
        code = f'''#!/usr/bin/env python3
"""
{agent_name}: Specialized Researcher Agent for Nexus Financial Assurance Ltd.

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
        mcp_call = {{
            "tool": "MCP-PDF-Parser",
            "params": {{
                "input_file": input_file,
                "output_format": "structured_json",
                "mpc_mode": mpc_mode
            }}
        }}
        
        # Simulated MCP call (in production, this interfaces with MCP server)
        print(f"[MCP] Parsing PDF: {{input_file}} (MPC mode: {{mpc_mode}})")
        
        # Mock parsed data (in production, comes from MCP server)
        mock_data = {{
            "file": input_file,
            "transactions": [
                {{"transaction_id": "TX-001", "amount_encrypted": "encrypted_value_1"}},
                {{"transaction_id": "TX-002", "amount_encrypted": "encrypted_value_2"}},
            ],
            "parsed_at": datetime.now().isoformat(),
            "mpc_mode": mpc_mode
        }}
        
        return mock_data
    
    @staticmethod
    def write_excel(data: Dict[str, Any], template: str = "Nexus_Audit_Template.xlsx", 
                   mpc_mode: bool = True) -> str:
        """
        Write normalized data to Excel using MCP-Excel-Writer.
        
        In MPC mode, data remains encrypted in intermediate storage.
        """
        mcp_call = {{
            "tool": "MCP-Excel-Writer",
            "params": {{
                "data": data,
                "template": template,
                "mpc_mode": mpc_mode
            }}
        }}
        
        print(f"[MCP] Writing Excel: {{template}} (MPC mode: {{mpc_mode}})")
        
        # Mock output path
        output_path = f"normalized_transactions_{{datetime.now().strftime('%Y%m%d_%H%M%S')}}.xlsx"
        return output_path


class {agent_name}(Agent_Researcher):
    """
    Specialized Researcher Agent for Nexus Financial Assurance Ltd.
    
    Inherits from Agent_Researcher and extends with:
    - MCP tool integration for PDF/Excel processing
    - MPC-aware data normalization
    - Full provenance tracking (C5 compliance)
    """
    
    def __init__(self, agent_name: str = "{agent_name}", 
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
        
        print(f"[{agent_name}] Processing WF-AUDIT-01 Step 1: PDF ingestion")
        
        # Parse PDF via MCP (MPC mode enabled)
        parsed_data = self.mcp_client.parse_pdf(pdf_file, mpc_mode=True)
        
        # Log provenance
        self._log_provenance({{
            "action": "parse_pdf",
            "input_file": pdf_file,
            "mcp_tool": "MCP-PDF-Parser",
            "mpc_mode": True,
            "output_hash": hashlib.sha256(
                json.dumps(parsed_data, sort_keys=True).encode()
            ).hexdigest()[:16]
        }})
        
        return parsed_data
    
    def process_wf_audit_01_step2(self, parsed_data: Dict[str, Any]) -> str:
        """
        Execute Step 2 of WF-AUDIT-01: Normalize data format.
        
        Uses MCP-Excel-Writer to create standardized transaction records.
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot process workflow without signed contract")
        
        print(f"[{agent_name}] Processing WF-AUDIT-01 Step 2: Data normalization")
        
        # Write normalized data to Excel via MCP (MPC mode enabled)
        output_path = self.mcp_client.write_excel(parsed_data, mpc_mode=True)
        
        # Log provenance
        self._log_provenance({{
            "action": "normalize_data",
            "mcp_tool": "MCP-Excel-Writer",
            "mpc_mode": True,
            "output_file": output_path
        }})
        
        return output_path
    
    def get_provenance_log(self) -> List[Dict[str, Any]]:
        """Return full provenance log for C5 compliance."""
        return self.provenance_log


def main():
    """Main execution block for testing {agent_name} agent."""
    agent = {agent_name}("{agent_name}", ["MCP-PDF-Parser", "MCP-Excel-Writer"])
    print(f"[MAIN] Instantiated {{agent.name}} (ID: {{agent.agent_id}})")
    
    # Mock contract for testing
    mock_contract = {{
        "contract_id": "Nexus Financial Assurance Ltd.-RES-01",
        "research_scope": {{
            "workflow_ids": ["WF-AUDIT-01"],
            "approved_sources": ["MCP-PDF-Parser", "MCP-Excel-Writer", "MCP-Web-Search"],
        }},
        "security_protocols": {{
            "mpc_required": True,
            "session_firewall_enabled": True,
        }},
    }}
    
    if agent.sign_contract(mock_contract):
        print(f"[MAIN] Contract signed: {{mock_contract['contract_id']}}")
        
        # Test workflow execution
        print("\\n[MAIN] Testing WF-AUDIT-01 Steps 1-2...")
        step1_result = agent.process_wf_audit_01_step1("transaction_logs.pdf")
        step2_result = agent.process_wf_audit_01_step2(step1_result)
        
        print(f"[MAIN] Step 1 result: {{len(step1_result.get('transactions', []))}} transactions parsed")
        print(f"[MAIN] Step 2 result: Normalized data written to {{step2_result}}")
        print(f"[MAIN] Provenance log entries: {{len(agent.get_provenance_log())}}")
    
    print("\\n[MAIN] {agent_name} agent test completed successfully!")


if __name__ == "__main__":
    main()
'''
        
        try:
            with open(agent_path, "w", encoding="utf-8") as f:
                f.write(code)
            console.print(f"[green][OK] {agent_name} fabricated successfully[/green]")
            return True
        except Exception as e:
            console.print(f"[red]ERROR fabricating {agent_name}: {e}[/red]")
            return False
    
    def _fabricate_pm(self, agent_name: str, file_name: str) -> bool:
        """Generate PM specialized agent (e.g., Apex_Growth_Systems_PM.py)."""
        agent_path = self.nexus_dir / file_name
        
        code = f'''#!/usr/bin/env python3
"""
{agent_name}: Specialized Project Manager Agent for {self.client_name}

This agent implements:
- Supervisor Pattern for workflow orchestration
- Task decomposition and delegation
- Trust Ledger management for subordinate agents
- Full provenance tracking (C5 compliance)
- V1.5 Capabilities: MCP Tools (Data Commons, Rill) and Persistent Mental Model

Reference: {self.client_name} Deployment Plan
"""

import sys
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

# Add repository root to path for imports
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from catalogue.gent_ProjectManager import Agent_ProjectManager


class {agent_name}(Agent_ProjectManager):
    """
    Specialized Project Manager Agent for {self.client_name}
    
    Inherits from Agent_ProjectManager (which inherits from Agent_Base) and extends with:
    - Workflow orchestration for {self.client_name}
    - Trust Ledger tracking for subordinate agents
    - Full provenance tracking (C5 compliance)
    - V1.5 Capabilities: MCP Tools (Google Data Commons, Rill Data) and Persistent Mental Model
    """
    
    def __init__(self, agent_name: str = "{agent_name}", 
                 specialization: str = "Workflow Supervisor"):
        super().__init__(agent_name, specialization)
        self.provenance_log: List[Dict[str, Any]] = []
        self.token_usage = 0
        self.token_budget_max = 100000  # Token budget
        self.subordinate_agent_ids: Dict[str, str] = {{}}  # Track subordinate agents
    
    def _log_provenance(self, event: Dict[str, Any]) -> None:
        """Log provenance information for C5 compliance."""
        event["provenance_id"] = hashlib.sha256(
            json.dumps(event, sort_keys=True).encode()
        ).hexdigest()[:16]
        event["agent_id"] = self.agent_id
        event["timestamp"] = datetime.now().isoformat()
        self.provenance_log.append(event)
    
    def orchestrate_wf_audit_01(self) -> Dict[str, Any]:
        """
        Orchestrate the complete WF-AUDIT-01 workflow.
        
        Supervisor Pattern: Decomposes workflow and delegates to specialized agents.
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot orchestrate workflow without signed contract")
        
        print(f"[{agent_name}] Orchestrating WF-AUDIT-01: Automated Transaction Audit")
        
        # Decompose workflow into steps
        workflow_steps = [
            {{
                "step": 1,
                "agent": "Nexus_Researcher",
                "task": "Ingest raw transaction logs (PDF/CSV) via MCP-PDF-Parser",
                "agent_id": self.nexus_agent_ids.get("researcher", "Nexus_Researcher")
            }},
            {{
                "step": 2,
                "agent": "Nexus_Researcher",
                "task": "Normalize data format via MCP-Excel-Writer",
                "agent_id": self.nexus_agent_ids.get("researcher", "Nexus_Researcher")
            }},
            {{
                "step": 3,
                "agent": "Nexus_Compliance",
                "task": "Cross-reference against Global_Sanctions_List.db (Yao's GC)",
                "agent_id": self.nexus_agent_ids.get("compliance", "Nexus_Compliance")
            }},
            {{
                "step": 4,
                "agent": "Nexus_Compliance",
                "task": "Flag suspicious outliers (> $10k) via Yao's GC",
                "agent_id": self.nexus_agent_ids.get("compliance", "Nexus_Compliance")
            }},
            {{
                "step": 5,
                "agent": "Nexus_Researcher",
                "task": "Generate Summary Report for Human Review",
                "agent_id": self.nexus_agent_ids.get("researcher", "Nexus_Researcher")
            }},
        ]
        
        # Log orchestration start
        self._log_provenance({{
            "action": "orchestrate_workflow",
            "workflow_id": "WF-AUDIT-01",
            "steps": len(workflow_steps),
            "subordinate_agents": list(self.nexus_agent_ids.values())
        }})
        
        # Delegate tasks (in production, this would use A2A Protocol)
        for step in workflow_steps:
            self.delegate(step, step["agent_id"])
            print(f"[{agent_name}] Delegated Step {{step['step']}} to {{step['agent']}}")
        
        return {{
            "workflow_id": "WF-AUDIT-01",
            "status": "ORCHESTRATED",
            "steps_delegated": len(workflow_steps),
            "orchestrated_at": datetime.now().isoformat()
        }}
    
    def register_subordinate_agent(self, role: str, agent_id: str) -> None:
        """Register a subordinate Nexus agent for trust ledger tracking."""
        self.nexus_agent_ids[role] = agent_id
        self.subordinate_swarm.append(agent_id)
        print(f"[{agent_name}] Registered subordinate agent: {{role}} ({{agent_id}})")
    
    def get_provenance_log(self) -> List[Dict[str, Any]]:
        """Return full provenance log for C5 compliance."""
        return self.provenance_log


def main():
    """Main execution block for testing {agent_name} agent."""
    agent = {agent_name}("{agent_name}", "Audit Workflow Supervisor")
    print(f"[MAIN] Instantiated {{agent.name}} (ID: {{agent.agent_id}})")
    
    # Mock contract for testing
    mock_contract = {{
        "contract_id": "Nexus Financial Assurance Ltd.-PM-MASTER",
        "financial_terms": {{
            "token_budget_max": 100000,
        }},
        "deliverables": ["End-to-end coordination of WF-AUDIT-01"],
        "security_protocols": {{
            "mpc_required": True,
            "session_firewall_enabled": True,
        }},
    }}
    
    if agent.sign_contract(mock_contract):
        print(f"[MAIN] Contract signed: {{mock_contract['contract_id']}}")
        
        # Register subordinate agents
        agent.register_subordinate_agent("researcher", "Nexus_Researcher-001")
        agent.register_subordinate_agent("compliance", "Nexus_Compliance-001")
        
        # Test workflow orchestration
        print("\\n[MAIN] Testing WF-AUDIT-01 orchestration...")
        result = agent.orchestrate_wf_audit_01()
        print(f"[MAIN] Orchestration result: {{json.dumps(result, indent=2)}}")
        print(f"[MAIN] Provenance log entries: {{len(agent.get_provenance_log())}}")
    
    print("\\n[MAIN] {agent_name} agent test completed successfully!")


if __name__ == "__main__":
    main()
'''
        
        try:
            with open(agent_path, "w", encoding="utf-8") as f:
                f.write(code)
            console.print(f"[green][OK] {agent_name} fabricated successfully[/green]")
            return True
        except Exception as e:
            console.print(f"[red]ERROR fabricating {agent_name}: {e}[/red]")
            return False
    
    def _fabricate_dba(self, agent_name: str, file_name: str) -> bool:
        """Generate Nexus_DBA.py specialized agent."""
        agent_path = self.nexus_dir / file_name
        
        code = f'''#!/usr/bin/env python3
"""
{agent_name}: Specialized Database Architect Agent for {self.client_name}

This agent implements:
- SQL schema design and optimization
- Vector store (RAG) and Knowledge Graph management
- Blind Indexing (ORAM) for PII protection
- Data migration via MCP

Reference: Specification.md - Pillar 2: Data Sovereignty
"""

import sys
from pathlib import Path
from typing import Dict, Any

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from catalogue.Agent_DBA import Agent_DBA


class {agent_name}(Agent_DBA):
    """
    Specialized Database Architect for {self.client_name}.
    
    Inherits from Agent_DBA and extends with client-specific configurations.
    """
    
    def __init__(self, agent_name: str = "{agent_name}", 
                 db_type: str = "PostgreSQL"):
        super().__init__(agent_name, db_type)  # specialization defaults to "Database Architecture"


def main():
    """Main execution block for testing {agent_name} agent."""
    agent = {agent_name}("{agent_name}")
    print(f"[MAIN] Instantiated {{agent.name}} (ID: {{agent.agent_id}})")
    
    # Mock contract for testing
    mock_contract = {{
        "contract_id": "{self.client_name}-DBA-01",
        "database_spec": {{
            "type": "PostgreSQL",
            "version": "15.0"
        }},
        "security_protocols": {{
            "blind_indexing_required": True,
            "oram_enabled": True,
            "sensitive_fields": ["email", "ssn", "phone"]
        }}
    }}
    
    if agent.sign_contract(mock_contract):
        print(f"[MAIN] Contract signed: {{mock_contract['contract_id']}}")
        print("[MAIN] {agent_name} agent test completed successfully!")


if __name__ == "__main__":
    main()
'''
        
        try:
            with open(agent_path, "w", encoding="utf-8") as f:
                f.write(code)
            console.print(f"[green][OK] {agent_name} fabricated successfully[/green]")
            return True
        except Exception as e:
            console.print(f"[red]ERROR fabricating {agent_name}: {e}[/red]")
            return False
    
    def _fabricate_netsec(self, agent_name: str, file_name: str) -> bool:
        """Generate Nexus_NetSec.py specialized agent."""
        agent_path = self.nexus_dir / file_name
        
        code = f'''#!/usr/bin/env python3
"""
{agent_name}: Specialized Network Security Sentinel Agent for {self.client_name}

This agent implements:
- Active vulnerability scanning
- Automated security patching
- Session-Level Semantic Firewall (C6 protection)

Reference: Specification.md - Pillar 3: Cyber-Infrastructure
"""

import sys
from pathlib import Path
from typing import Dict, Any

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from catalogue.Agent_NetSec import Agent_NetSec


class {agent_name}(Agent_NetSec):
    """
    Specialized Network Security Sentinel for {self.client_name}.
    
    Inherits from Agent_NetSec and extends with client-specific security policies.
    """
    
    def __init__(self, agent_name: str = "{agent_name}",
                 specialization: str = "Network Security"):
        super().__init__(agent_name, specialization)


def main():
    """Main execution block for testing {agent_name} agent."""
    agent = {agent_name}("{agent_name}")
    print(f"[MAIN] Instantiated {{agent.name}} (ID: {{agent.agent_id}})")
    
    # Mock contract for testing
    mock_contract = {{
        "contract_id": "{self.client_name}-NETSEC-01",
        "security_requirements": {{
            "session_firewall_enabled": True,
            "vulnerability_scanning": True
        }},
        "firewall_policy": {{
            "enabled": True,
            "rules": [
                {{
                    "type": "keyword_block",
                    "keywords": ["password", "secret_key", "api_key"]
                }}
            ]
        }}
    }}
    
    if agent.sign_contract(mock_contract):
        print(f"[MAIN] Contract signed: {{mock_contract['contract_id']}}")
        print("[MAIN] {agent_name} agent test completed successfully!")


if __name__ == "__main__":
    main()
'''
        
        try:
            with open(agent_path, "w", encoding="utf-8") as f:
                f.write(code)
            console.print(f"[green][OK] {agent_name} fabricated successfully[/green]")
            return True
        except Exception as e:
            console.print(f"[red]ERROR fabricating {agent_name}: {e}[/red]")
            return False
    
    def _fabricate_marketer(self, agent_name: str, file_name: str) -> bool:
        """Generate Nexus_Marketer.py specialized agent."""
        agent_path = self.nexus_dir / file_name
        
        code = f'''#!/usr/bin/env python3
"""
{agent_name}: Specialized Growth Officer Agent for {self.client_name}

This agent implements:
- Omnichannel marketing automation
- Market trend analysis
- Business Intelligence and ROI calculation

Reference: Specification.md - Pillar 5: Growth Operations
"""

import sys
from pathlib import Path
from typing import Dict, Any

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from catalogue.Agent_Marketer import Agent_Marketer


class {agent_name}(Agent_Marketer):
    """
    Specialized Growth Officer for {self.client_name}.
    
    Inherits from Agent_Marketer and extends with client-specific marketing channels.
    """
    
    def __init__(self, agent_name: str = "{agent_name}",
                 specialization: str = "Growth Marketing"):
        super().__init__(agent_name, specialization)


def main():
    """Main execution block for testing {agent_name} agent."""
    agent = {agent_name}("{agent_name}")
    print(f"[MAIN] Instantiated {{agent.name}} (ID: {{agent.agent_id}})")
    
    # Mock contract for testing
    mock_contract = {{
        "contract_id": "{self.client_name}-MARKETER-01",
        "marketing_channels": ["email", "social", "sms"],
        "bi_requirements": {{
            "metrics": ["ROI", "CAC", "LTV", "conversion_rate"],
            "dashboard_enabled": True
        }}
    }}
    
    if agent.sign_contract(mock_contract):
        print(f"[MAIN] Contract signed: {{mock_contract['contract_id']}}")
        print("[MAIN] {agent_name} agent test completed successfully!")


if __name__ == "__main__":
    main()
'''
        
        try:
            with open(agent_path, "w", encoding="utf-8") as f:
                f.write(code)
            console.print(f"[green][OK] {agent_name} fabricated successfully[/green]")
            return True
        except Exception as e:
            console.print(f"[red]ERROR fabricating {agent_name}: {e}[/red]")
            return False
    
    def _generate_enhanced_econtracts(self) -> Dict[str, Dict[str, Any]]:
        """
        Generate E-Contracts with budget line items for 5-Pillar agents.
        
        Includes specific cost items:
        - DBA: Vector Storage Costs
        - NetSec: Vulnerability Scan Fees
        - Marketer: Campaign Costs
        """
        if not self.client_profile:
            return {}
        
        company = self.client_profile["client_meta"]["company_name"]
        financials = self.client_profile.get("financial_constraints", {})
        base_budget = financials.get("total_token_budget_monthly", 500000)
        
        contracts = {}
        
        # Base contracts (existing)
        base_contracts = generate_econtracts(self.client_profile)
        contracts.update(base_contracts)
        
        # DBA Contract with Vector Storage Costs
        if "DATA" in self.detected_triggers:
            dba_contract = {
                "contract_id": f"{company}-DBA-01",
                "database_spec": {
                    "type": "PostgreSQL",
                    "vector_stores": ["Chroma", "Pinecone"]
                },
                "financial_terms": {
                    "token_budget_max": int(base_budget * 0.15),  # 15% of total
                    "line_items": {
                        "vector_storage_costs": {
                            "description": "Vector store storage and embedding costs (Chroma/Pinecone)",
                            "monthly_estimate": 500,
                            "unit": "USD"
                        },
                        "oram_computation": {
                            "description": "ORAM computation overhead for private data access patterns",
                            "monthly_estimate": 300,
                            "unit": "USD"
                        }
                    },
                    "penalty_clause": financials.get("penalty_clause", "")
                },
                "security_protocols": {
                    "blind_indexing_required": True,
                    "oram_enabled": True,
                    "sensitive_fields": ["email", "ssn", "phone", "name"]
                }
            }
            contracts["dba"] = dba_contract
        
        # NetSec Contract with Vulnerability Scan Fees
        if "SECURITY" in self.detected_triggers:
            netsec_contract = {
                "contract_id": f"{company}-NETSEC-01",
                "security_requirements": {
                    "session_firewall_enabled": True,
                    "vulnerability_scanning": True,
                    "scan_frequency": "daily"
                },
                "financial_terms": {
                    "token_budget_max": int(base_budget * 0.10),  # 10% of total
                    "line_items": {
                        "vulnerability_scan_fees": {
                            "description": "Automated vulnerability scanning, CVE tracking, and security assessments",
                            "monthly_estimate": 400,
                            "unit": "USD"
                        }
                    },
                    "penalty_clause": financials.get("penalty_clause", "")
                },
                "firewall_policy": {
                    "enabled": True,
                    "rules": [
                        {
                            "type": "keyword_block",
                            "keywords": ["password", "secret_key", "api_key", "ssn"]
                        }
                    ]
                }
            }
            contracts["netsec"] = netsec_contract
        
        # Marketer Contract with Campaign Costs
        if "GROWTH" in self.detected_triggers:
            marketer_contract = {
                "contract_id": f"{company}-MARKETER-01",
                "marketing_channels": ["email", "social", "sms", "web"],
                "financial_terms": {
                    "token_budget_max": int(base_budget * 0.20),  # 20% of total
                    "line_items": {
                        "campaign_ad_spend": {
                            "description": "Omnichannel campaign ad spend across email, social, SMS, and web channels",
                            "monthly_estimate": 1000,
                            "unit": "USD"
                        }
                    },
                    "penalty_clause": financials.get("penalty_clause", "")
                },
                "bi_requirements": {
                    "metrics": ["ROI", "CAC", "LTV", "conversion_rate", "ctr"],
                    "dashboard_enabled": True
                }
            }
            contracts["marketer"] = marketer_contract
        
        return contracts
    
    def _display_econtracts_summary(self) -> None:
        """Display E-Contract summary with budget line items for 5-Pillar agents."""
        console.print("\n[bold cyan]===========================================================[/bold cyan]")
        console.print("[bold cyan]E-CONTRACT SUMMARY WITH BUDGET LINE ITEMS[/bold cyan]")
        console.print("[bold cyan]===========================================================[/bold cyan]\n")
        
        contracts = self._generate_enhanced_econtracts()
        
        if not contracts:
            console.print("[dim]No additional contracts generated.[/dim]")
            return
        
        # Display contracts for 5-Pillar agents
        for contract_key, contract in contracts.items():
            if contract_key in ["dba", "netsec", "marketer"]:
                agent_name = contract_key.upper()
                console.print(f"\n[bold yellow]{agent_name} Contract:[/bold yellow]")
                console.print(f"  Contract ID: {contract.get('contract_id', 'N/A')}")
                
                financial_terms = contract.get("financial_terms", {})
                line_items = financial_terms.get("line_items", {})
                
                if line_items:
                    console.print(f"  [bold]Budget Line Items:[/bold]")
                    for item_key, item_data in line_items.items():
                        description = item_data.get("description", "")
                        estimate = item_data.get("monthly_estimate", 0)
                        unit = item_data.get("unit", "USD")
                        console.print(f"    - {item_key.replace('_', ' ').title()}: ${estimate}/{unit} ({description})")
                
                token_budget = financial_terms.get("token_budget_max", 0)
                console.print(f"  Token Budget: {token_budget:,} tokens/month")
    
    def stage_fabrication(self, mapping: Dict[str, Any]) -> bool:
        """Stage 4: Fabrication - Generate specialized agent instances."""
        console.print("\n[bold cyan]===========================================================[/bold cyan]")
        console.print("[bold cyan]STAGE 4: FABRICATION[/bold cyan]")
        console.print("[bold cyan]===========================================================[/bold cyan]\n")
        
        # Skip existing agents
        if mapping["existing_agents"]:
            console.print("[yellow]Skipping existing agents:[/yellow]")
            for agent in mapping["existing_agents"]:
                console.print(f"  [dim]- {agent['name']} (already exists)[/dim]")
        
        # Fabricate new agents
        agents_to_fabricate = mapping["agents_to_fabricate"]
        if not agents_to_fabricate:
            console.print("\n[green]All agents already exist. No fabrication needed.[/green]")
            return True
        
        console.print(f"\n[bold]Fabricating {len(agents_to_fabricate)} agent(s)...[/bold]\n")
        
        success_count = 0
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            for agent_info in agents_to_fabricate:
                task = progress.add_task(f"Fabricating {agent_info['name']}...", total=None)
                if self.fabricate_agent(agent_info):
                    success_count += 1
                progress.update(task, completed=True)
        
        if success_count == len(agents_to_fabricate):
            console.print(f"\n[green][OK] All {success_count} agent(s) fabricated successfully![/green]")
            return True
        else:
            console.print(f"\n[yellow][WARN] Fabricated {success_count}/{len(agents_to_fabricate)} agent(s)[/yellow]")
            return False
    
    def run(self) -> None:
        """Execute the complete factory pipeline."""
        console.print(Panel.fit(
            "[bold cyan]SWARM AGENCY FACTORY PIPELINE[/bold cyan]\n"
            "Prime Orchestrator - Automated Agent Fabrication System",
            border_style="cyan"
        ))
        
        # Stage 1: Intake
        if not self.stage_intake():
            console.print("\n[red]Factory pipeline aborted at Intake stage.[/red]")
            return
        
        # Stage 2: Mapping
        mapping = self.stage_mapping()
        
        # Stage 3: Approval
        if not self.stage_approval(mapping):
            console.print("\n[yellow]Factory pipeline cancelled by user.[/yellow]")
            return
        
        # Stage 4: Fabrication
        if not self.stage_fabrication(mapping):
            console.print("\n[yellow]Factory pipeline completed with warnings.[/yellow]")
            return
        
        # Generate and display E-Contracts with budget line items
        self._display_econtracts_summary()
        
        # Success summary
        console.print("\n[bold green]===========================================================[/bold green]")
        console.print("[bold green]FACTORY PIPELINE COMPLETE[/bold green]")
        console.print("[bold green]===========================================================[/bold green]\n")
        
        # Display final status
        table = Table(title="Agent Status", show_header=True, header_style="bold magenta")
        table.add_column("Agent", style="cyan")
        table.add_column("File", style="yellow")
        table.add_column("Status", style="green")
        
        for agent_name, agent_info in self.agent_templates.items():
            agent_file = self.nexus_dir / agent_info["file"]
            status = "[green]EXISTS[/green]" if agent_file.exists() else "[red]MISSING[/red]"
            table.add_row(agent_name, agent_info["file"], status)
        
        console.print(table)
        
        # Streamlit Dashboard command
        console.print("\n[bold cyan]===========================================================[/bold cyan]")
        console.print("[bold cyan]NEXT STEP: LAUNCH STREAMLIT DASHBOARD[/bold cyan]")
        console.print("[bold cyan]===========================================================[/bold cyan]\n")
        
        dashboard_cmd = "streamlit run dashboard.py"
        console.print(Panel(
            f"[bold yellow]{dashboard_cmd}[/bold yellow]",
            title="Command to Launch Dashboard",
            border_style="green"
        ))
        console.print("\n[dim]Note: Ensure dashboard.py exists in the repository root.[/dim]\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='Swarm Agency Factory Pipeline')
    parser.add_argument('--profile', type=str, help='Path to client profile JSON file', 
                       default=None)
    parser.add_argument('--yes', '-y', action='store_true', 
                       help='Auto-approve fabrication plan (non-interactive mode)')
    args = parser.parse_args()
    
    profile_path = None
    if args.profile:
        profile_path = Path(args.profile)
        if not profile_path.is_absolute():
            profile_path = REPO_ROOT / profile_path
    
    factory = SwarmFactory(profile_path=profile_path, auto_approve=args.yes)
    factory.run()


if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""
BASE CLASS: Agent_NetSec (Network Security Sentinel)
DEPARTMENT: Engineering & Tech (The "Builders")
PILLAR: Cyber-Infrastructure (Pillar 3)

ROLE:
    - IT Security, Network Operations, and Session Firewall enforcement
    - Active vulnerability scanning
    - Automated security patching
    - Session-Level Semantic Firewall to prevent Context Bypass (C6)

SECURITY REFERENCE:
    - Master Data for MAaaS (Security Challenges C6: Cross-domain Context Bypass)
    - Session-Level Semantic Firewall (Source 64)
    - cb-mpc audit compliance (CBS-02-002, side-channel detection)

REFERENCE:
    - Specification.md: Pillar 3 - Cyber-Infrastructure
    - Master Data: Challenge C6 mitigation strategies
"""

import uuid
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Optional, Any
import re

# Placeholder for the A2A Protocol library (to be implemented)
# from protocols.a2a import Message, ProtocolEnum


class SessionFirewall:
    """
    Session-Level Semantic Firewall implementation.
    
    Prevents Cross-domain Context Bypass (C6) by analyzing multi-agent dialogues
    in a sliding window to detect when composite context breaches policy.
    
    Reference: Master Data for MAaaS.pdf - Challenge C6 (Source 64)
    """
    
    def __init__(self, policy_rules: List[Dict[str, Any]]):
        self.policy_rules = policy_rules
        self.dialogue_history: List[Dict[str, Any]] = []
        self.window_size = 10  # Sliding window size
    
    def check_message(self, message_content: str, agent_id: str, 
                     session_id: str) -> Dict[str, Any]:
        """
        Check input against Session-Level Semantic Firewall policy.
        
        Returns:
            {
                "allowed": bool,
                "reason": str,
                "sanitized_content": Optional[str]
            }
        """
        # Add to dialogue history
        self.dialogue_history.append({
            "timestamp": datetime.now().isoformat(),
            "agent_id": agent_id,
            "session_id": session_id,
            "content": message_content
        })
        
        # Maintain sliding window
        if len(self.dialogue_history) > self.window_size:
            self.dialogue_history = self.dialogue_history[-self.window_size:]
        
        # Analyze composite context for policy violations
        composite_context = " ".join([msg["content"] for msg in self.dialogue_history])
        
        violations = []
        
        # Check for PII reconstruction attempts
        pii_patterns = [
            r'\b\d{3}-\d{2}-\d{4}\b',  # SSN pattern
            r'\b\d{3}\.\d{3}\.\d{4}\b',  # Phone pattern
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email
        ]
        
        for pattern in pii_patterns:
            if re.search(pattern, composite_context):
                violations.append("PII pattern detected in composite context")
        
        # Check for incremental query patterns (C6 attack vector)
        if len(self.dialogue_history) >= 3:
            # Detect if multiple seemingly benign queries could reconstruct sensitive data
            query_count = sum(1 for msg in self.dialogue_history if "?" in msg["content"])
            if query_count >= 3:
                violations.append("Potential incremental query pattern (C6 risk)")
        
        # Check policy rules
        for rule in self.policy_rules:
            if rule["type"] == "keyword_block":
                keywords = rule.get("keywords", [])
                for keyword in keywords:
                    if keyword.lower() in composite_context.lower():
                        violations.append(f"Blocked keyword detected: {keyword}")
        
        if violations:
            return {
                "allowed": False,
                "reason": "; ".join(violations),
                "sanitized_content": None,
                "firewall_action": "BLOCK"
            }
        
        # Sanitize if needed (remove potential PII)
        sanitized = message_content
        for pattern in pii_patterns:
            sanitized = re.sub(pattern, "[REDACTED]", sanitized)
        
        return {
            "allowed": True,
            "reason": "Message passed firewall checks",
            "sanitized_content": sanitized if sanitized != message_content else None,
            "firewall_action": "ALLOW"
        }


class MCPClient:
    """
    Model Context Protocol (MCP) client for security tools.
    """
    
    @staticmethod
    def run_vulnerability_scan(target: str) -> Dict[str, Any]:
        """
        Run security vulnerability scan via MCP-Security-Scanner tool.
        """
        mcp_call = {
            "tool": "MCP-Security-Scanner",
            "params": {
                "target": target,
                "scan_type": "vulnerability",
                "intensity": "full"
            }
        }
        
        print(f"[MCP] Running vulnerability scan on {target}...")
        
        # Mock scan results (in production, comes from MCP server)
        return {
            "target": target,
            "scan_timestamp": datetime.now().isoformat(),
            "vulnerabilities": [
                {
                    "id": "CVE-2024-0001",
                    "severity": "HIGH",
                    "description": "SQL Injection vulnerability",
                    "affected_component": "API endpoint /api/users"
                },
                {
                    "id": "CVE-2024-0002",
                    "severity": "MEDIUM",
                    "description": "Missing input validation",
                    "affected_component": "Agent endpoint"
                }
            ],
            "status": "COMPLETE"
        }
    
    @staticmethod
    def check_dependencies() -> List[Dict[str, Any]]:
        """
        Check Python dependencies for known CVEs via MCP-Dependency-Checker.
        """
        mcp_call = {
            "tool": "MCP-Dependency-Checker",
            "params": {
                "package_manager": "pip",
                "check_cves": True
            }
        }
        
        print("[MCP] Checking dependencies for CVEs...")
        
        # Mock CVE results
        return [
            {
                "package": "requests",
                "version": "2.28.0",
                "cve": "CVE-2023-32681",
                "severity": "HIGH",
                "fixed_in": "2.31.0"
            }
        ]


class Agent_NetSec:
    """
    BASE CLASS: Agent_NetSec (Network Security Sentinel)
    
    Handles IT Security, Network Operations, and Session Firewall enforcement.
    """
    
    def __init__(self, agent_name: str, specialization: str = "Network Security"):
        self.agent_id = str(uuid.uuid4())
        self.name = agent_name
        self.specialization = specialization
        self.active_contract: Optional[Dict] = None
        self.mcp_client = MCPClient()
        self.session_firewall: Optional[SessionFirewall] = None
        self.vulnerability_log: List[Dict[str, Any]] = []
        self.patch_history: List[Dict[str, Any]] = []
    
    def sign_contract(self, contract_json: Dict) -> bool:
        """
        Network Security contract pattern:
        - Validates security requirements and firewall policies.
        - Initializes Session-Level Semantic Firewall if required.
        """
        required_keys = ["contract_id", "security_requirements", "firewall_policy"]
        if not all(k in contract_json for k in required_keys):
            print(f"[NETSEC-ERROR] Contract {contract_json.get('contract_id')} rejected: Malformed.")
            return False
        
        firewall_policy = contract_json.get("firewall_policy", {})
        if firewall_policy.get("enabled", False):
            policy_rules = firewall_policy.get("rules", [])
            self.session_firewall = SessionFirewall(policy_rules)
            print(f"[NETSEC-INFO] Session-Level Semantic Firewall initialized")
        
        security = contract_json.get("security_requirements", {})
        if not security.get("session_firewall_enabled", False):
            print(
                f"[NETSEC-WARNING] {self.name} notes missing Session Firewall requirement. "
                f"Risk of cross-domain context bypass (C6) elevated."
            )
        
        self.active_contract = contract_json
        self.active_contract["status"] = "SIGNED"
        self.active_contract["signed_at"] = datetime.now().isoformat()
        
        print(f"[NETSEC-INFO] Agent {self.name} accepted Contract {contract_json['contract_id']}.")
        return True
    
    def delegate(self, task: Dict, target_agent_id: str):
        """
        Network Security delegation pattern:
        - Forwards security tasks to specialized agents (e.g., Compliance, Dev_Backend)
        - Uses A2A Protocol for agent-to-agent communication.
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot delegate without a signed Security Contract.")
        
        message = {
            "from": self.agent_id,
            "to": target_agent_id,
            "type": "SECURITY_TASK",
            "payload": task,
            "context_file": "Client_SOPs.md",
        }
        
        # self.send_a2a_message(message) -> This would interface with the A2A bus
        print(
            f"[NETSEC-DELEGATION] {self.name} delegated security task "
            f"'{task.get('task')}' to Agent {target_agent_id}."
        )
        return message
    
    def scan_vulnerabilities(self, target_ip: str) -> Dict[str, Any]:
        """
        Uses MCP to run security vulnerability checks.
        
        Args:
            target_ip: IP address or hostname to scan
        
        Returns:
            Vulnerability scan report
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot scan vulnerabilities without signed contract")
        
        print(f"[NETSEC] Scanning vulnerabilities on {target_ip}...")
        
        # Run vulnerability scan via MCP
        scan_results = self.mcp_client.run_vulnerability_scan(target_ip)
        
        # Check dependencies for CVEs
        dependency_cves = self.mcp_client.check_dependencies()
        
        # Combine results
        full_report = {
            "target": target_ip,
            "scan_timestamp": datetime.now().isoformat(),
            "vulnerabilities": scan_results.get("vulnerabilities", []),
            "dependency_cves": dependency_cves,
            "total_vulnerabilities": len(scan_results.get("vulnerabilities", [])) + len(dependency_cves),
            "high_severity_count": sum(
                1 for v in scan_results.get("vulnerabilities", []) + dependency_cves
                if v.get("severity") == "HIGH"
            ),
            "status": "COMPLETE"
        }
        
        # Log vulnerabilities
        self.vulnerability_log.append(full_report)
        
        print(f"[NETSEC] Scan complete: {full_report['total_vulnerabilities']} vulnerability(ies) found")
        print(f"[NETSEC] High severity: {full_report['high_severity_count']}")
        
        return full_report
    
    def patch_system(self, vulnerability_id: str) -> Dict[str, Any]:
        """
        Auto-generate hotfixes for identified vulnerabilities.
        
        Args:
            vulnerability_id: CVE ID or vulnerability identifier
        
        Returns:
            Patch generation report
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot patch system without signed contract")
        
        print(f"[NETSEC] Generating patch for {vulnerability_id}...")
        
        # Find vulnerability in log
        vulnerability = None
        for scan in self.vulnerability_log:
            for vuln in scan.get("vulnerabilities", []):
                if vuln.get("id") == vulnerability_id:
                    vulnerability = vuln
                    break
            if vulnerability:
                break
        
        if not vulnerability:
            # Check dependency CVEs
            for scan in self.vulnerability_log:
                for cve in scan.get("dependency_cves", []):
                    if cve.get("cve") == vulnerability_id:
                        vulnerability = cve
                        break
                if vulnerability:
                    break
        
        if not vulnerability:
            raise ValueError(f"Vulnerability {vulnerability_id} not found in scan logs")
        
        # Generate patch based on vulnerability type
        patch_code = self._generate_patch_code(vulnerability)
        
        patch_report = {
            "vulnerability_id": vulnerability_id,
            "patch_timestamp": datetime.now().isoformat(),
            "patch_code": patch_code,
            "severity": vulnerability.get("severity"),
            "status": "GENERATED",
            "requires_review": True  # All auto-generated patches require human review
        }
        
        self.patch_history.append(patch_report)
        
        print(f"[NETSEC] Patch generated for {vulnerability_id}")
        print(f"[NETSEC] Status: {patch_report['status']} (requires review)")
        
        return patch_report
    
    def _generate_patch_code(self, vulnerability: Dict[str, Any]) -> str:
        """
        Generate patch code based on vulnerability description.
        """
        vuln_desc = vulnerability.get("description", "").lower()
        vuln_id = vulnerability.get("id", "")
        
        # Pattern-based patch generation
        if "sql injection" in vuln_desc:
            return f"""
# Patch for {vuln_id}: SQL Injection Prevention
# Add parameterized queries
import psycopg2

def safe_query(query, params):
    conn = psycopg2.connect(...)
    cursor = conn.cursor()
    cursor.execute(query, params)  # Use parameterized queries
    return cursor.fetchall()
"""
        elif "input validation" in vuln_desc:
            return f"""
# Patch for {vuln_id}: Input Validation
def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Input must be string")
    if len(user_input) > 1000:
        raise ValueError("Input too long")
    # Add more validation as needed
    return user_input.strip()
"""
        elif "cve" in vuln_id.lower():
            # Dependency update
            fixed_version = vulnerability.get("fixed_in", "latest")
            package = vulnerability.get("package", "unknown")
            return f"""
# Patch for {vuln_id}: Dependency Update
# Run: pip install {package}=={fixed_version}
# Or update requirements.txt: {package}>={fixed_version}
"""
        else:
            return f"""
# Patch for {vuln_id}: Generic Security Fix
# Review vulnerability description and implement appropriate fix
# Description: {vulnerability.get('description', 'N/A')}
"""
    
    def enforce_firewall(self, message_content: str, agent_id: str, 
                        session_id: str) -> Dict[str, Any]:
        """
        Check input against Session-Level Semantic Firewall policy.
        
        Prevents Context Bypass (C6) by analyzing composite context.
        
        Args:
            message_content: Message content to check
            agent_id: ID of agent sending message
            session_id: Session identifier
        
        Returns:
            Firewall decision with allowed/sanitized content
        """
        if not self.session_firewall:
            # If firewall not initialized, allow by default (with warning)
            print(f"[NETSEC-WARNING] Session Firewall not initialized, allowing message")
            return {
                "allowed": True,
                "reason": "Firewall not initialized",
                "sanitized_content": message_content,
                "firewall_action": "ALLOW"
            }
        
        result = self.session_firewall.check_message(message_content, agent_id, session_id)
        
        if not result["allowed"]:
            print(f"[NETSEC-FIREWALL] Message BLOCKED: {result['reason']}")
        elif result.get("sanitized_content"):
            print(f"[NETSEC-FIREWALL] Message SANITIZED: PII patterns removed")
        
        return result
    
    def to_json(self) -> Dict:
        return {
            "agent_id": self.agent_id,
            "role": "Network Security Sentinel",
            "name": self.name,
            "specialization": self.specialization,
            "status": "ACTIVE" if self.active_contract else "IDLE",
            "firewall_enabled": self.session_firewall is not None,
            "vulnerabilities_scanned": len(self.vulnerability_log),
            "patches_generated": len(self.patch_history)
        }


# Example Usage for Testing
if __name__ == "__main__":
    netsec = Agent_NetSec("NetSec-001", "Security Operations")
    
    sample_contract = {
        "contract_id": "SEC-CONTRACT-001",
        "security_requirements": {
            "session_firewall_enabled": True,
            "vulnerability_scanning": True
        },
        "firewall_policy": {
            "enabled": True,
            "rules": [
                {
                    "type": "keyword_block",
                    "keywords": ["password", "secret_key", "api_key"]
                }
            ]
        }
    }
    
    netsec.sign_contract(sample_contract)
    
    # Test vulnerability scanning
    scan_result = netsec.scan_vulnerabilities("192.168.1.100")
    print("\n=== Vulnerability Scan Result ===")
    print(json.dumps(scan_result, indent=2))
    
    # Test firewall enforcement
    firewall_result = netsec.enforce_firewall(
        "What is the user's email address?",
        "agent-123",
        "session-456"
    )
    print("\n=== Firewall Check Result ===")
    print(json.dumps(firewall_result, indent=2))
    
    # Test patch generation
    if scan_result.get("vulnerabilities"):
        patch = netsec.patch_system(scan_result["vulnerabilities"][0]["id"])
        print("\n=== Generated Patch ===")
        print(patch["patch_code"])


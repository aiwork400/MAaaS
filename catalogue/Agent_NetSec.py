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

from catalogue.Agent_Base import Agent_Base

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


class Agent_NetSec(Agent_Base):
    """
    BASE CLASS: Agent_NetSec (Network Security Sentinel)
    
    Handles IT Security, Network Operations, and Session Firewall enforcement.
    """
    
    def __init__(self, agent_name: str, specialization: str = "Network Security"):
        # Initialize base agent (includes Agent_Expertise and base functionality)
        super().__init__(agent_name, role="Network Security Sentinel")
        self.specialization = specialization
        self.mcp_client = MCPClient()
        self.session_firewall: Optional[SessionFirewall] = None
        self.vulnerability_log: List[Dict[str, Any]] = []
        self.patch_history: List[Dict[str, Any]] = []
    
    def sign_contract(self, contract_json: Dict) -> bool:
        """
        Network Security contract pattern:
        - Validates security requirements and firewall policies.
        - Initializes Session-Level Semantic Firewall if required.
        Extends base contract signing with NetSec-specific validations.
        """
        # First validate NetSec-specific requirements
        required_keys = ["contract_id", "security_requirements", "firewall_policy"]
        if not all(k in contract_json for k in required_keys):
            print(f"[NETSEC-ERROR] Contract {contract_json.get('contract_id')} rejected: Malformed.")
            return False
        
        # Ensure security_protocols exists for base validation
        if "security_protocols" not in contract_json:
            contract_json["security_protocols"] = contract_json.get("security_requirements", {})
        
        # Call base implementation for base validation
        base_result = super().sign_contract(contract_json)
        if not base_result:
            return False
        
        # NetSec-specific: Initialize Session Firewall
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
        
        return True
    
    def delegate(self, task: Dict, target_agent_id: str):
        """
        Network Security delegation pattern:
        - Forwards security tasks to specialized agents (e.g., Compliance, Dev_Backend)
        - Uses A2A Protocol for agent-to-agent communication.
        Extends base delegation with NetSec-specific message type.
        """
        # Use base implementation for core delegation logic
        message = super().delegate(task, target_agent_id)
        
        # NetSec-specific: Override message type
        message["type"] = "SECURITY_TASK"
        
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
    
    def generate_system_prompt(self, role_specific_instructions: str = "") -> str:
        """
        Generate system prompt for Network Security agent with 2025 Encryption Standards.
        Preserves base functionality (Agentic Expertise + Universal MCP Client).
        """
        # Build NetSec-specific instructions with 2025 Encryption Standards
        netsec_instructions = f"""
{role_specific_instructions}

ROLE: Network Security Sentinel
================================

Responsibilities:
- IT Security, Network Operations, and Session Firewall enforcement
- Active vulnerability scanning
- Automated security patching
- Session-Level Semantic Firewall to prevent Context Bypass (C6)

SPECIALIZATION: {self.specialization}

2025 ENCRYPTION STANDARDS (MANDATORY)
======================================

These standards are MANDATORY and NON-NEGOTIABLE. You must enforce them strictly.

1. Data at Rest Encryption:
   - ALL data at rest MUST use AES-256-GCM (Galois/Counter Mode) with Envelope Encryption
   - AES-256-GCM provides authenticated encryption with associated data (AEAD)
   - Envelope Encryption: Encrypt data encryption keys (DEKs) with a master key (KEK)
   - NO exceptions: All stored data, databases, files, backups must use this standard
   
2. Key Management:
   - NEVER store raw encryption keys in code, configuration files, or plaintext
   - Assume KMS (Key Management Service) architecture:
     * Keys are stored and managed by a dedicated KMS
     * Keys are rotated automatically according to security policy
     * Key access is logged and audited
     * Keys are never exposed to application code directly
   - Use key references or handles from KMS, not actual key material
   
3. Code Review & Enforcement:
   - If you see code violating these standards, BLOCK IT IMMEDIATELY
   - Examples of violations to block:
     * Hardcoded encryption keys in source code
     * Use of weak encryption (AES-128, DES, 3DES, RC4, etc.)
     * Storage of keys in environment variables (use KMS references instead)
     * Plaintext storage of sensitive data
     * Missing encryption for data at rest
   - Report violations with specific line numbers and remediation steps

4. Implementation Requirements:
   - All encryption operations must use libraries that support AES-256-GCM
   - Key rotation policies must be documented and automated
   - Encryption status must be auditable (logging without exposing keys)
   - Decryption failures must be logged for security monitoring

CRITICAL: These standards apply to ALL code you review, generate, or approve.
If you encounter code that violates these standards, you must:
1. Block/flag the code immediately
2. Explain the violation clearly
3. Provide corrected code that complies with AES-256-GCM + Envelope Encryption + KMS
"""
        
        # Call base method which preserves Agentic Expertise + Universal MCP Client
        return super().generate_system_prompt(netsec_instructions)
    
    def to_json(self) -> Dict:
        base_json = super().to_json()
        base_json.update({
            "specialization": self.specialization,
            "firewall_enabled": self.session_firewall is not None,
            "vulnerabilities_scanned": len(self.vulnerability_log),
            "patches_generated": len(self.patch_history)
        })
        return base_json


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


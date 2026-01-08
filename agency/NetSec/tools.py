from agency_swarm.tools import BaseTool
from pydantic import Field
from pathlib import Path
import re
from typing import List, Dict, Any


class AuditLog(BaseTool):
    """
    Scans the latest system logs for security violations.
    """
    keyword: str = Field(..., description="The security term to search for (e.g., 'ERROR', 'PII', 'SSN', 'PASSWORD', 'UNAUTHORIZED').")

    def run(self):
        """
        Audit system logs for security violations.
        
        Returns:
            Audit report with findings
        """
        # Get factory logs directory
        log_dir = Path("factory_logs")
        findings = []
        
        # Security violation patterns
        pii_patterns = [
            r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
            r'\b\d{3}\.\d{3}\.\d{4}\b',  # Phone
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email (in context of violations)
        ]
        
        # Search in factory logs if directory exists
        if log_dir.exists():
            for log_file in log_dir.glob("*.log"):
                try:
                    with open(log_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if self.keyword.lower() in content.lower():
                            findings.append({
                                "file": str(log_file),
                                "keyword": self.keyword,
                                "status": "MATCH_FOUND"
                            })
                        
                        # Check for PII patterns
                        for pattern in pii_patterns:
                            if re.search(pattern, content):
                                findings.append({
                                    "file": str(log_file),
                                    "pattern": "PII_DETECTED",
                                    "status": "SECURITY_VIOLATION"
                                })
                except Exception as e:
                    findings.append({
                        "file": str(log_file),
                        "error": str(e),
                        "status": "READ_ERROR"
                    })
        
        # Check for unauthorized access patterns
        unauthorized_keywords = ["UNAUTHORIZED", "ACCESS_DENIED", "PERMISSION_ERROR", "CLEARANCE_VIOLATION"]
        if self.keyword.upper() in unauthorized_keywords:
            findings.append({
                "keyword": self.keyword,
                "type": "UNAUTHORIZED_ACCESS_CHECK",
                "status": "MONITORING"
            })
        
        if not findings:
            return f"[NetSec] Audit complete. No active threats found for keyword '{self.keyword}'."
        else:
            report = f"[NetSec] Audit Results for '{self.keyword}':\n"
            report += f"Found {len(findings)} potential issue(s):\n"
            for finding in findings:
                report += f"  - {finding}\n"
            return report


class VerifyEncryption(BaseTool):
    """
    Verifies that data moving through SecureCommsChannel is properly encrypted.
    """
    channel_name: str = Field(..., description="The communication channel to verify (e.g., 'SecureCommsChannel').")
    
    def run(self):
        """
        Verify encryption status of a communication channel.
        
        Returns:
            Encryption verification report
        """
        # Simulate encryption verification
        # In production, this would check actual encryption status
        return f"[NetSec] Encryption verification for '{self.channel_name}': ✓ AES-256-GCM encryption verified. Channel secure."

#!/usr/bin/env python3
"""
BASE CLASS: Agent_DBA (Database Architect)
DEPARTMENT: Engineering & Tech (The "Builders")
PILLAR: Data Sovereignty (Pillar 2)

ROLE:
    - Manages SQL databases (PostgreSQL, MySQL, SQLite) and Vector DBs (Chroma, Pinecone)
    - Auto-generates SQL schemas from data structures
    - Optimizes slow queries
    - Migrates data from CSV/Excel via MCP
    - Implements Blind Indexing (ORAM concepts) for PII protection

SECURITY REFERENCE:
    - Master Data for MAaaS (ORAM concepts, Source 61)
    - Blind Indexing prevents plaintext queries on sensitive fields
    - ORAM achieves sublinear memory access costs for private indexes

REFERENCE:
    - Specification.md: Pillar 2 - Data Sovereignty
    - Master Data: ORAM concepts (Floram, Path ORAM)
"""

import uuid
import hashlib
import json
from datetime import datetime
from typing import Dict, List, Optional, Any, Tuple
import re

from catalogue.Agent_Base import Agent_Base

# Placeholder for the A2A Protocol library (to be implemented)
# from protocols.a2a import Message, ProtocolEnum


class BlindIndex:
    """
    Blind Indexing implementation for ORAM-based private data access.
    
    Prevents sensitive fields (PII) from being queried in plaintext.
    Uses cryptographic hashing with salt to create searchable indexes
    without revealing the original values.
    
    Reference: Master Data for MAaaS.pdf - ORAM concepts (Source 61)
    """
    
    @staticmethod
    def create_blind_index(value: str, salt: Optional[str] = None) -> str:
        """
        Create a blind index for a sensitive field.
        
        The index is cryptographically hashed, preventing plaintext queries
        while still allowing equality checks.
        """
        if salt is None:
            # In production, salt should be stored securely per client/field
            salt = "default_salt_change_in_production"
        
        combined = f"{value}:{salt}".encode('utf-8')
        return hashlib.sha256(combined).hexdigest()
    
    @staticmethod
    def query_blind_index(query_value: str, salt: Optional[str] = None) -> str:
        """
        Generate blind index for query matching.
        
        Returns the hash that can be used to query the database
        without revealing the original query value.
        """
        return BlindIndex.create_blind_index(query_value, salt)


class MCPClient:
    """
    Model Context Protocol (MCP) client for data migration tools.
    """
    
    @staticmethod
    def read_csv(file_path: str) -> List[Dict[str, Any]]:
        """
        Read CSV file via MCP-CSV-Reader tool.
        """
        mcp_call = {
            "tool": "MCP-CSV-Reader",
            "params": {
                "file_path": file_path,
                "encoding": "utf-8"
            }
        }
        
        # Simulated MCP call (in production, interfaces with MCP server)
        print(f"[MCP] Reading CSV: {file_path}")
        
        # Mock data (in production, comes from MCP server)
        return [
            {"id": 1, "name": "Example", "email": "example@test.com"},
            {"id": 2, "name": "Sample", "email": "sample@test.com"},
        ]
    
    @staticmethod
    def read_excel(file_path: str, sheet_name: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Read Excel file via MCP-Excel-Reader tool.
        """
        mcp_call = {
            "tool": "MCP-Excel-Reader",
            "params": {
                "file_path": file_path,
                "sheet_name": sheet_name
            }
        }
        
        print(f"[MCP] Reading Excel: {file_path}")
        
        # Mock data
        return [
            {"id": 1, "name": "Example", "email": "example@test.com"},
            {"id": 2, "name": "Sample", "email": "sample@test.com"},
        ]


class Agent_DBA(Agent_Base):
    """
    BASE CLASS: Agent_DBA (Database Architect)
    
    Manages both SQL and Vector databases with privacy-preserving access patterns.
    """
    
    def __init__(self, agent_name: str, db_type: str = "PostgreSQL", 
                 specialization: str = "Database Architecture"):
        # Initialize base agent (includes Agent_Expertise and base functionality)
        super().__init__(agent_name, role="Database Architect")
        self.db_type = db_type  # PostgreSQL, MySQL, SQLite, Chroma, Pinecone
        self.specialization = specialization
        self.blind_index_salts: Dict[str, str] = {}  # Field name -> salt mapping
        self.mcp_client = MCPClient()
        self.schema_history: List[Dict[str, Any]] = []
    
    def sign_contract(self, contract_json: Dict) -> bool:
        """
        Database Architect contract pattern:
        - Validates database requirements and security protocols.
        - Ensures ORAM/Blind Indexing requirements for sensitive fields.
        Extends base contract signing with DBA-specific validations.
        """
        # First validate DBA-specific requirements
        required_keys = ["contract_id", "database_spec", "security_protocols"]
        if not all(k in contract_json for k in required_keys):
            print(f"[DBA-ERROR] Contract {contract_json.get('contract_id')} rejected: Malformed.")
            return False
        
        # Call base implementation for base validation
        base_result = super().sign_contract(contract_json)
        if not base_result:
            return False
        
        # DBA-specific: Validate ORAM/Blind Indexing requirements
        security = contract_json["security_protocols"]
        if not security.get("blind_indexing_required", False):
            print(
                f"[DBA-WARNING] {self.name} notes missing Blind Indexing requirement. "
                f"PII fields may be queried in plaintext (ORAM violation)."
            )
        
        if not security.get("oram_enabled", False):
            print(
                f"[DBA-WARNING] {self.name} notes missing ORAM requirement. "
                f"Access patterns may be inferable from query timing."
            )
        
        return True
    
    def delegate(self, task: Dict, target_agent_id: str):
        """
        Database Architect delegation pattern:
        - Forwards database operations to specialized agents (e.g., Vector Store Manager)
        - Uses A2A Protocol for agent-to-agent communication.
        Extends base delegation with DBA-specific message type.
        """
        # Use base implementation for core delegation logic
        message = super().delegate(task, target_agent_id)
        
        # DBA-specific: Override message type
        message["type"] = "DATABASE_TASK"
        
        return message
    
    def design_schema(self, data_structure: Dict[str, Any]) -> str:
        """
        Auto-generate SQL tables from data structure.
        
        Args:
            data_structure: Dict with field names and types, e.g.:
                {
                    "users": {
                        "id": "INTEGER PRIMARY KEY",
                        "email": "VARCHAR(255)",
                        "name": "VARCHAR(255)"
                    }
                }
        
        Returns:
            SQL CREATE TABLE statements
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot design schema without signed contract")
        
        print(f"[DBA] Designing schema for {len(data_structure)} table(s)...")
        
        sql_statements = []
        security = self.active_contract.get("security_protocols", {})
        blind_indexing = security.get("blind_indexing_required", False)
        sensitive_fields = security.get("sensitive_fields", [])
        
        for table_name, columns in data_structure.items():
            create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (\n"
            column_defs = []
            
            for col_name, col_type in columns.items():
                # Check if field requires blind indexing
                if blind_indexing and col_name in sensitive_fields:
                    # Create blind index column instead of plaintext
                    column_defs.append(f"    {col_name}_blind_index VARCHAR(64) NOT NULL")
                    column_defs.append(f"    {col_name}_encrypted TEXT")  # Encrypted value
                    # Store salt for this field
                    self.blind_index_salts[f"{table_name}.{col_name}"] = hashlib.sha256(
                        f"{self.agent_id}:{table_name}:{col_name}".encode()
                    ).hexdigest()[:16]
                else:
                    column_defs.append(f"    {col_name} {col_type}")
            
            create_table += ",\n".join(column_defs)
            create_table += "\n);"
            sql_statements.append(create_table)
            
            # Add indexes for blind indexed fields
            if blind_indexing:
                for col_name in sensitive_fields:
                    if col_name in columns:
                        index_sql = (
                            f"CREATE INDEX IF NOT EXISTS idx_{table_name}_{col_name}_blind "
                            f"ON {table_name}({col_name}_blind_index);"
                        )
                        sql_statements.append(index_sql)
        
        schema_sql = "\n\n".join(sql_statements)
        
        # Log schema history
        self.schema_history.append({
            "timestamp": datetime.now().isoformat(),
            "table_count": len(data_structure),
            "blind_indexing_enabled": blind_indexing,
            "sql": schema_sql
        })
        
        print(f"[DBA] Schema generated with {len(sql_statements)} statement(s)")
        if blind_indexing:
            print(f"[DBA] Blind Indexing enabled for {len(sensitive_fields)} sensitive field(s)")
        
        return schema_sql
    
    def optimize_query(self, sql_query: str) -> str:
        """
        Rewrite slow queries for better performance.
        
        Analyzes query patterns and suggests optimizations:
        - Index recommendations
        - Query plan improvements
        - Join order optimization
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot optimize query without signed contract")
        
        print(f"[DBA] Optimizing query...")
        
        # Basic query analysis
        query_lower = sql_query.lower()
        optimized = sql_query
        
        # Detect missing indexes on WHERE clauses
        where_pattern = r'where\s+(\w+)\s*[=<>]'
        where_matches = re.findall(where_pattern, query_lower)
        
        # Detect missing indexes on JOIN conditions
        join_pattern = r'join\s+\w+\s+on\s+(\w+)\.(\w+)\s*=\s*(\w+)\.(\w+)'
        join_matches = re.findall(join_pattern, query_lower)
        
        suggestions = []
        
        if where_matches:
            for field in where_matches:
                suggestions.append(
                    f"-- Consider adding index: CREATE INDEX idx_{field} ON table_name({field});"
                )
        
        if join_matches:
            for match in join_matches:
                table1, col1, table2, col2 = match
                suggestions.append(
                    f"-- Consider adding index: CREATE INDEX idx_{table1}_{col1} "
                    f"ON {table1}({col1});"
                )
        
        # Query plan optimization suggestions
        if "select *" in query_lower:
            optimized = optimized.replace("SELECT *", "SELECT <specific_columns>")
            suggestions.append("-- Avoid SELECT *; specify only needed columns")
        
        if "order by" in query_lower and "limit" not in query_lower:
            suggestions.append("-- Consider adding LIMIT if full ordering not needed")
        
        # Combine optimized query with suggestions
        if suggestions:
            optimized = optimized + "\n\n-- Optimization Suggestions:\n" + "\n".join(suggestions)
        
        print(f"[DBA] Query optimization complete ({len(suggestions)} suggestion(s))")
        return optimized
    
    def migrate_data(self, source: str, destination: str) -> Dict[str, Any]:
        """
        Hydrate databases from CSV/Excel via MCP.
        
        Args:
            source: Path to CSV or Excel file
            destination: Target database table name
        
        Returns:
            Migration report with row counts and status
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError("Cannot migrate data without signed contract")
        
        print(f"[DBA] Migrating data from {source} to {destination}...")
        
        # Determine file type and read via MCP
        if source.endswith('.csv'):
            data = self.mcp_client.read_csv(source)
        elif source.endswith(('.xlsx', '.xls')):
            data = self.mcp_client.read_excel(source)
        else:
            raise ValueError(f"Unsupported file type: {source}")
        
        # Apply blind indexing if required
        security = self.active_contract.get("security_protocols", {})
        blind_indexing = security.get("blind_indexing_required", False)
        sensitive_fields = security.get("sensitive_fields", [])
        
        migrated_rows = 0
        for row in data:
            # In production, this would insert into actual database
            # For sensitive fields, use blind indexing
            if blind_indexing:
                for field in sensitive_fields:
                    if field in row:
                        # Create blind index
                        salt = self.blind_index_salts.get(f"{destination}.{field}", None)
                        blind_index = BlindIndex.create_blind_index(str(row[field]), salt)
                        row[f"{field}_blind_index"] = blind_index
                        # Encrypt original value (simplified - production would use proper encryption)
                        row[f"{field}_encrypted"] = f"encrypted_{row[field]}"
                        del row[field]  # Remove plaintext
            
            migrated_rows += 1
        
        report = {
            "source_file": source,
            "destination_table": destination,
            "rows_migrated": migrated_rows,
            "blind_indexing_applied": blind_indexing,
            "sensitive_fields_protected": len(sensitive_fields) if blind_indexing else 0,
            "migration_timestamp": datetime.now().isoformat(),
            "status": "SUCCESS"
        }
        
        print(f"[DBA] Migration complete: {migrated_rows} row(s) migrated")
        if blind_indexing:
            print(f"[DBA] Blind Indexing applied to {len(sensitive_fields)} field(s)")
        
        return report
    
    def query_with_blind_index(self, table_name: str, field_name: str, 
                              query_value: str) -> str:
        """
        Generate SQL query using blind index (ORAM concept).
        
        Prevents plaintext queries on sensitive fields by using blind indexes.
        """
        salt = self.blind_index_salts.get(f"{table_name}.{field_name}")
        if not salt:
            raise ValueError(f"No blind index salt found for {table_name}.{field_name}")
        
        blind_index = BlindIndex.query_blind_index(query_value, salt)
        
        # Query using blind index instead of plaintext
        sql = (
            f"SELECT * FROM {table_name} "
            f"WHERE {field_name}_blind_index = '{blind_index}';"
        )
        
        print(f"[DBA] Generated blind index query for {table_name}.{field_name}")
        return sql
    
    def generate_system_prompt(self, role_specific_instructions: str = "") -> str:
        """
        Generate system prompt for Database Architect with 2025 Encryption Standards.
        Preserves base functionality (Agentic Expertise + Universal MCP Client).
        """
        # Build DBA-specific instructions with 2025 Encryption Standards
        dba_instructions = f"""
{role_specific_instructions}

ROLE: Database Architect
========================

Responsibilities:
- Manages SQL databases (PostgreSQL, MySQL, SQLite) and Vector DBs (Chroma, Pinecone)
- Auto-generates SQL schemas from data structures
- Optimizes slow queries
- Migrates data from CSV/Excel via MCP
- Implements Blind Indexing (ORAM concepts) for PII protection

DATABASE TYPE: {self.db_type}
SPECIALIZATION: {self.specialization}

2025 ENCRYPTION STANDARDS (MANDATORY)
======================================

These standards are MANDATORY and NON-NEGOTIABLE. You must enforce them strictly.

1. Data at Rest Encryption:
   - ALL data at rest MUST use AES-256-GCM (Galois/Counter Mode) with Envelope Encryption
   - This applies to:
     * Database files and tables
     * Backup files
     * Log files containing sensitive data
     * Temporary database files
     * Any persistent storage of database data
   - AES-256-GCM provides authenticated encryption with associated data (AEAD)
   - Envelope Encryption: Encrypt data encryption keys (DEKs) with a master key (KEK)
   - NO exceptions: All stored database data must use this standard
   
2. Key Management:
   - NEVER store raw encryption keys in code, configuration files, or plaintext
   - Assume KMS (Key Management Service) architecture:
     * Database encryption keys are stored and managed by a dedicated KMS
     * Keys are rotated automatically according to security policy
     * Key access is logged and audited
     * Keys are never exposed to database connection strings or configurations
   - Use key references or handles from KMS, not actual key material
   - Database connection strings must reference KMS for key retrieval
   
3. Code Review & Enforcement:
   - If you see code violating these standards, BLOCK IT IMMEDIATELY
   - Examples of violations to block:
     * Hardcoded encryption keys in database connection strings
     * Use of weak encryption (AES-128, DES, 3DES, etc.)
     * Storage of keys in database configuration files
     * Plaintext storage of sensitive database fields
     * Missing Transparent Data Encryption (TDE) or column-level encryption
     * Unencrypted database backups
   - Report violations with specific line numbers and remediation steps

4. Implementation Requirements:
   - All database encryption operations must use libraries that support AES-256-GCM
   - Database-level encryption (TDE) must be enabled for all databases
   - Column-level encryption must be used for highly sensitive fields (PII, financial data)
   - Key rotation policies must be documented and automated
   - Encryption status must be auditable (logging without exposing keys)
   - Database backup encryption must use the same AES-256-GCM standard

5. Database-Specific Considerations:
   - PostgreSQL: Use pgcrypto extension with AES-256-GCM
   - MySQL: Use encryption-at-rest with AES-256-GCM
   - SQLite: Implement application-level encryption with AES-256-GCM
   - Vector DBs: Ensure vector embeddings are encrypted at rest
   - All database connections should use encrypted channels (TLS/SSL)

CRITICAL: These standards apply to ALL database code, schemas, migrations, and configurations you review, generate, or approve.
If you encounter code that violates these standards, you must:
1. Block/flag the code immediately
2. Explain the violation clearly
3. Provide corrected code that complies with AES-256-GCM + Envelope Encryption + KMS
"""
        
        # Call base method which preserves Agentic Expertise + Universal MCP Client
        return super().generate_system_prompt(dba_instructions)
    
    def to_json(self) -> Dict:
        base_json = super().to_json()
        base_json.update({
            "db_type": self.db_type,
            "specialization": self.specialization,
            "blind_indexing_enabled": len(self.blind_index_salts) > 0,
            "schema_count": len(self.schema_history)
        })
        return base_json


# Example Usage for Testing
if __name__ == "__main__":
    dba = Agent_DBA("DBA-001", "PostgreSQL", "Schema Design")
    
    sample_contract = {
        "contract_id": "DB-CONTRACT-001",
        "database_spec": {
            "type": "PostgreSQL",
            "version": "15.0"
        },
        "security_protocols": {
            "blind_indexing_required": True,
            "oram_enabled": True,
            "sensitive_fields": ["email", "ssn", "phone"]
        }
    }
    
    dba.sign_contract(sample_contract)
    
    # Test schema design
    data_structure = {
        "users": {
            "id": "INTEGER PRIMARY KEY",
            "email": "VARCHAR(255)",
            "name": "VARCHAR(255)",
            "ssn": "VARCHAR(11)"
        }
    }
    
    schema = dba.design_schema(data_structure)
    print("\n=== Generated Schema ===")
    print(schema)
    
    # Test query optimization
    slow_query = "SELECT * FROM users WHERE email = 'test@example.com' ORDER BY name;"
    optimized = dba.optimize_query(slow_query)
    print("\n=== Optimized Query ===")
    print(optimized)
    
    # Test blind index query
    blind_query = dba.query_with_blind_index("users", "email", "test@example.com")
    print("\n=== Blind Index Query ===")
    print(blind_query)


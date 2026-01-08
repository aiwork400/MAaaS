import json
import hashlib
from datetime import datetime
from core.db_manager import db

class MemoryBridge:
    """
    SCMS Implementation: Connects Agents to the 'agent_memory' and 'audit_logs' tables.
    """

    @staticmethod
    def log_audit(agent_name, action, details, severity="INFO"):
        """
        Compliance Logging: Saves every critical action to the immutable ledger.
        """
        query = """
            INSERT INTO audit_logs (agent_name, action_type, details, severity)
            VALUES (%s, %s, %s, %s)
        """
        db.execute_query(query, (agent_name, action, details, severity))
        print(f"[AUDIT] {agent_name} performed {action}")

    @staticmethod
    def commit_artifact(agent_id, content_dict, artifact_type="strategic"):
        """
        Token Minimization: Saves large data (Artifacts) to DB and returns a small Hash Pointer.
        """
        content_str = json.dumps(content_dict)
        # Create a deterministic hash reference
        ref_hash = hashlib.sha256(content_str.encode()).hexdigest()[:12]
        ref_tag = f"[REF:{ref_hash}]"

        query = """
            INSERT INTO agent_memory (agent_id, memory_type, content, artifact_ref)
            VALUES (%s, %s, %s, %s)
        """
        db.execute_query(query, (agent_id, artifact_type, content_str, ref_tag))

        return ref_tag

    @staticmethod
    def retrieve_artifact(ref_tag):
        """
        Retrieves full data using the Hash Pointer.
        """
        query = "SELECT content FROM agent_memory WHERE artifact_ref = %s"
        conn = db.get_pool().getconn()
        try:
            cur = conn.cursor()
            cur.execute(query, (ref_tag,))
            result = cur.fetchone()
            if result:
                return json.loads(result[0])
            return None
        except Exception as e:
            print(f"[MEMORY] Retrieve failed: {e}")
            return None
        finally:
            db.get_pool().putconn(conn)

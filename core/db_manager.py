import os
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv

# Load secrets
load_dotenv()

class DatabaseManager:
    """
    MAaaS Master Data Vault.
    Handles persistent storage for Agent Artifacts and Memory.
    """
    _connection_pool = None

    @classmethod
    def get_pool(cls):
        if cls._connection_pool is None:
            try:
                cls._connection_pool = psycopg2.pool.SimpleConnectionPool(
                    1, 20,
                    user=os.getenv("POSTGRES_USER"),
                    password=os.getenv("POSTGRES_PASSWORD"),
                    host=os.getenv("POSTGRES_HOST"),
                    port=os.getenv("POSTGRES_PORT"),
                    database=os.getenv("POSTGRES_DB")
                )
                print("[DB] Connection Pool Initialized.")
            except Exception as e:
                print(f"[DB] CRITICAL ERROR: Could not connect to PostgreSQL. {e}")
        return cls._connection_pool

    def execute_query(self, query, params=None):
        conn = self.get_pool().getconn()
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()
            return cur
        except Exception as e:
            print(f"[DB] Query Failed: {e}")
            conn.rollback()
        finally:
            self.get_pool().putconn(conn)

# Singleton
db = DatabaseManager()

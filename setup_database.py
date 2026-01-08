import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv

load_dotenv()

# Config
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")
TARGET_DB = os.getenv("POSTGRES_DB")

def init_db():
    print("--- MAaaS GENESIS SEQUENCE ---")

    # Step 1: Connect to default 'postgres' db to create our target db
    try:
        con = psycopg2.connect(user=DB_USER, password=DB_PASS, host=DB_HOST, dbname='postgres')
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = con.cursor()

        # Check if exists
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{TARGET_DB}'")
        exists = cursor.fetchone()

        if not exists:
            print(f"[GENESIS] Creating Database '{TARGET_DB}'...")
            cursor.execute(f"CREATE DATABASE {TARGET_DB}")
        else:
            print(f"[GENESIS] Database '{TARGET_DB}' already exists.")

        cursor.close()
        con.close()

    except Exception as e:
        print(f"[ERROR] Database Creation Failed: {e}")
        return

    # Step 2: Connect to the new DB and apply Schema
    try:
        print(f"[GENESIS] Applying SCMS Schema to '{TARGET_DB}'...")
        con = psycopg2.connect(user=DB_USER, password=DB_PASS, host=DB_HOST, dbname=TARGET_DB)
        cursor = con.cursor()

        with open('core/schema.sql', 'r') as f:
            schema_sql = f.read()
            cursor.execute(schema_sql)

        con.commit()
        print("[SUCCESS] Tables 'audit_logs' and 'agent_memory' created.")
        print("--- MAaaS PLATFORM READY ---")

    except Exception as e:
        print(f"[ERROR] Schema Application Failed: {e}")
    finally:
        if con: con.close()

if __name__ == "__main__":
    init_db()

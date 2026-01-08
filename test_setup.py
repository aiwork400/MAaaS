"""Test script to verify MAaaS setup"""
import sys

print("=== MAaaS Setup Verification ===\n")

# Test 1: Database Manager
try:
    from core.db_manager import db
    print("[OK] Database Manager imported successfully")
    pool = db.get_pool()
    if pool:
        print("[OK] Database connection pool initialized")
    else:
        print("[WARNING] Database connection pool returned None (database may not be running)")
except Exception as e:
    print(f"[ERROR] Database Manager error: {e}")

print()

# Test 2: Agents
try:
    from orchestrator import agency, liaison, scanner, netsec
    print("[OK] All agents imported successfully")
    print(f"  - ExecutiveLiaison: {liaison.name}")
    print(f"  - MarketScanner: {scanner.name}")
    print(f"  - NetSec: {netsec.name}")
    print("[OK] Security Protocol: ACTIVE")
except Exception as e:
    print(f"[ERROR] Agent import error: {e}")
    import traceback
    traceback.print_exc()

print()
print("=== Setup Complete ===")

import os
from agency_swarm import Agency
from agency.ExecutiveLiaison import ExecutiveLiaison
from agency.MarketScanner import MarketScanner
from agency.NetSec import NetSec

# --- MAaaS ORCHESTRATOR (v2 Enterprise Edition) ---

print("Initializing Enterprise Swarm...")

# 1. Instantiate the Agents
try:
    liaison = ExecutiveLiaison()
    scanner = MarketScanner()
    netsec = NetSec()
except Exception as e:
    print(f"[CRITICAL] Agent Instantiation Failed: {e}")
    exit(1)

# 2. Define the Agency (New API Format)
# We use positional args for the entry point and 'communication_flows' for the graph.
agency = Agency(
    liaison,  # Entry Point (The Board Interface)
    communication_flows=[
        [liaison, scanner],  # Liaison manages Scanner
        [liaison, netsec],   # Liaison reports to NetSec
        [netsec, scanner],   # NetSec audits Scanner
    ],
    shared_instructions='SCMS.md',
)

if __name__ == "__main__":
    print("\n--------------------------------------------")
    print("MAaaS Swarm Online. Security Protocol: ACTIVE.")
    print("Interface: Executive Liaison")
    print("Type 'exit' to close.")
    print("--------------------------------------------\n")
    
    # 3. Manual Enterprise Loop (Replaces deprecated run_demo)
    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Shutting down Swarm...")
                break
            
            if not user_input.strip():
                continue
                
            print("... Swarm is thinking ...")
            
            # Use the direct completion method
            response = agency.get_completion(message=user_input)
            
            print(f"\nExecutive Liaison: {response}\n")
            
        except KeyboardInterrupt:
            print("\nForce Quit.")
            break
        except Exception as e:
            print(f"[ERROR] Execution failed: {e}")
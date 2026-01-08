from agency_swarm import Agency
from agency.ExecutiveLiaison import ExecutiveLiaison
from agency.MarketScanner import MarketScanner
from agency.NetSec import NetSec
import os

# --- MAaaS ORCHESTRATOR ---

# 1. Instantiate the Agents
# These load from the 'agency/' folder structure we just created
liaison = ExecutiveLiaison()
scanner = MarketScanner()
netsec = NetSec()

# 2. Define the Agency Chart (Communication Flow)
# - User talks to Liaison.
# - Liaison manages Scanner.
# - NetSec monitors EVERYONE (Top of the Pyramid).
agency = Agency(
    liaison,  # Entry Point (The Board Interface)
    communication_flows=[
        [liaison, scanner],   # Liaison -> manages -> Scanner
        [liaison, netsec],    # Liaison can report breaches to NetSec
        [netsec, scanner],    # NetSec can audit Scanner
    ],
    shared_instructions='SCMS.md', # The Root Constitution (Must exist in root)
)

if __name__ == "__main__":
    # Terminal Demo Mode for Oira/Ario testing
    print("MAaaS Swarm Online. Security Protocol: ACTIVE.")
    print("Interface: Executive Liaison.")
    print("\nYou can now interact with the Executive Liaison agent.")
    print("Type your message or command below:")
    print("(Example: 'Scan the coffee market in Irvine, CA. I need a strategic summary for the Board.')\n")
    
    try:
        agency.terminal_demo()
    except (UnicodeEncodeError, SystemError, KeyboardInterrupt) as e:
        # Fallback for Windows console encoding issues or user interruption
        if isinstance(e, KeyboardInterrupt):
            print("\n\nExiting...")
        else:
            print(f"\n[Note: Terminal encoding issue detected. Using programmatic interface instead.]")
            print("\nAgency is ready. Example usage:")
            print("  from orchestrator import agency")
            print("  response = agency.get_response_sync('Scan the coffee market in Irvine, CA. I need a strategic summary for the Board.')")
            print("  print(response)")
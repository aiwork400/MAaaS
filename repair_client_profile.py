#!/usr/bin/env python3
"""
Temporary script to repair clients/nexus_financial_assurance.json
Handles BOM characters, encoding mismatches, and rewrites as clean UTF-8.
"""

import json
from pathlib import Path
import sys

def read_json_with_encoding(file_path: Path) -> tuple:
    """Read JSON file trying multiple encodings."""
    encodings = ["utf-8-sig", "utf-8", "utf-16", "utf-16-le", "utf-16-be", "latin-1"]
    
    # Check file size
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    file_size = file_path.stat().st_size
    print(f"File size: {file_size} bytes")
    
    if file_size == 0:
        raise ValueError("File is empty")
    
    # Read first bytes to detect BOM
    with open(file_path, "rb") as f:
        first_bytes = f.read(4)
        print(f"First 4 bytes (hex): {first_bytes.hex()}")
    
    last_error = None
    
    for encoding in encodings:
        try:
            print(f"\nTrying encoding: {encoding}")
            with open(file_path, "r", encoding=encoding) as f:
                content = f.read().strip()
                if not content:
                    print(f"  -> Content is empty after reading")
                    continue
                print(f"  -> Successfully read {len(content)} characters")
                parsed = json.loads(content)
                print(f"  -> Successfully parsed JSON with {encoding} encoding")
                return parsed, encoding
        except UnicodeDecodeError as e:
            print(f"  -> UnicodeDecodeError: {e}")
            last_error = e
            continue
        except json.JSONDecodeError as e:
            print(f"  -> JSONDecodeError: {e.msg} at position {e.pos}")
            last_error = e
            continue
        except Exception as e:
            print(f"  -> Unexpected error: {type(e).__name__}: {e}")
            last_error = e
            continue
    
    raise ValueError(f"Could not read file with any encoding. Last error: {last_error}")

def repair_json_file(file_path: Path):
    """Repair JSON file by reading with robust encoding and rewriting as clean UTF-8."""
    print(f"Repairing: {file_path}")
    print("=" * 60)
    
    try:
        # Read the file with robust encoding handling
        data, used_encoding = read_json_with_encoding(file_path)
        
        print(f"\n[OK] Successfully read file using encoding: {used_encoding}")
        print(f"[OK] JSON structure is valid")
        
        # Create backup
        backup_path = file_path.with_suffix('.json.backup')
        print(f"\nCreating backup: {backup_path}")
        with open(backup_path, "wb") as f:
            with open(file_path, "rb") as original:
                f.write(original.read())
        print(f"[OK] Backup created")
        
        # Rewrite as clean UTF-8
        print(f"\nRewriting as clean UTF-8...")
        with open(file_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"[OK] File rewritten as clean UTF-8")
        
        # Verify the rewritten file
        print(f"\nVerifying rewritten file...")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            verified = json.loads(content)
        
        print(f"[OK] Verification successful")
        print(f"\n{'=' * 60}")
        print(f"SUCCESS: File repaired and saved as clean UTF-8")
        print(f"Backup saved to: {backup_path}")
        
    except Exception as e:
        print(f"\n{'=' * 60}")
        print(f"ERROR: Failed to repair file")
        print(f"Error: {type(e).__name__}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parent
    client_profile_path = repo_root / "clients" / "nexus_financial_assurance.json"
    
    repair_json_file(client_profile_path)


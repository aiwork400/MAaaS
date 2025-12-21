#!/usr/bin/env python3
"""
File Doctor - JSON Encoding Repair Utility
Fixes BOM characters, encoding mismatches, and rewrites JSON files as clean UTF-8.

Usage:
    python file_doctor.py <file_path>
    python file_doctor.py --all  # Fix all JSON files in clients/
    python file_doctor.py --check  # Check files without fixing
"""

import json
from pathlib import Path
import sys
import argparse
from typing import Tuple, Optional

def diagnose_file(file_path: Path) -> Tuple[bool, Optional[str], Optional[dict]]:
    """
    Diagnose a JSON file's encoding and validity.
    
    Returns:
        (is_valid, encoding_used, parsed_data)
    """
    if not file_path.exists():
        return False, None, None
    
    file_size = file_path.stat().st_size
    if file_size == 0:
        return False, "EMPTY", None
    
    # Read first bytes to detect BOM
    with open(file_path, "rb") as f:
        first_bytes = f.read(4)
    
    # Try encodings in priority order
    encodings = [
        "utf-8-sig",  # UTF-8 with BOM (most common issue)
        "utf-8",      # Standard UTF-8
        "utf-16",     # UTF-16 (auto-detect LE/BE)
        "utf-16-le",  # UTF-16 Little Endian
        "utf-16-be",  # UTF-16 Big Endian
        "latin-1"     # Fallback
    ]
    
    for encoding in encodings:
        try:
            with open(file_path, "r", encoding=encoding) as f:
                content = f.read().strip()
                if not content:
                    continue
                parsed = json.loads(content)
                return True, encoding, parsed
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
        except Exception:
            continue
    
    return False, "UNKNOWN", None

def repair_file(file_path: Path, create_backup: bool = True) -> Tuple[bool, str]:
    """
    Repair a JSON file by reading with robust encoding and rewriting as clean UTF-8.
    
    Returns:
        (success, message)
    """
    if not file_path.exists():
        return False, f"File not found: {file_path}"
    
    # Diagnose the file
    is_valid, encoding_used, data = diagnose_file(file_path)
    
    if not is_valid:
        return False, f"File is not valid JSON or cannot be decoded. Encoding detected: {encoding_used}"
    
    if encoding_used == "utf-8" and not file_path.read_bytes().startswith(b'\xef\xbb\xbf'):
        # File is already clean UTF-8, no repair needed
        return True, f"File is already clean UTF-8. No repair needed."
    
    try:
        # Create backup if requested
        if create_backup:
            backup_path = file_path.with_suffix('.json.backup')
            with open(backup_path, "wb") as f:
                with open(file_path, "rb") as original:
                    f.write(original.read())
            backup_msg = f"Backup created: {backup_path.name}"
        else:
            backup_msg = "No backup created (--no-backup flag)"
        
        # Rewrite as clean UTF-8
        with open(file_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        # Verify the rewritten file
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            json.loads(content)  # Verify it's valid JSON
        
        return True, f"File repaired successfully. Original encoding: {encoding_used}. {backup_msg}"
        
    except Exception as e:
        return False, f"Error during repair: {type(e).__name__}: {e}"

def check_all_json_files(directory: Path) -> dict:
    """Check all JSON files in a directory."""
    results = {}
    
    for json_file in directory.rglob("*.json"):
        # Skip backup files
        if json_file.name.endswith(".backup"):
            continue
        
        is_valid, encoding, _ = diagnose_file(json_file)
        results[str(json_file.relative_to(directory))] = {
            "valid": is_valid,
            "encoding": encoding,
            "needs_repair": encoding not in ("utf-8", None) or not is_valid
        }
    
    return results

def main():
    parser = argparse.ArgumentParser(
        description="File Doctor - JSON Encoding Repair Utility",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python file_doctor.py clients/nexus_deployment_plan.json
  python file_doctor.py --all
  python file_doctor.py --check
  python file_doctor.py clients/*.json --no-backup
        """
    )
    
    parser.add_argument(
        "files",
        nargs="*",
        help="JSON file(s) to repair (or use --all to repair all in clients/)"
    )
    
    parser.add_argument(
        "--all",
        action="store_true",
        help="Repair all JSON files in clients/ directory"
    )
    
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check files without repairing them"
    )
    
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Don't create backup files"
    )
    
    parser.add_argument(
        "--directory",
        type=str,
        default="clients",
        help="Directory to scan when using --all (default: clients)"
    )
    
    args = parser.parse_args()
    
    # Determine which files to process
    files_to_process = []
    
    if args.all:
        directory = Path(args.directory)
        if not directory.exists():
            print(f"ERROR: Directory not found: {directory}")
            sys.exit(1)
        
        for json_file in directory.rglob("*.json"):
            if not json_file.name.endswith(".backup"):
                files_to_process.append(json_file)
        
        if not files_to_process:
            print(f"No JSON files found in {directory}")
            sys.exit(0)
    elif args.files:
        for file_pattern in args.files:
            file_path = Path(file_pattern)
            if file_path.is_file():
                files_to_process.append(file_path)
            elif file_path.is_dir():
                for json_file in file_path.rglob("*.json"):
                    if not json_file.name.endswith(".backup"):
                        files_to_process.append(json_file)
            else:
                # Try glob pattern
                import glob
                for matched_file in glob.glob(file_pattern):
                    file_path = Path(matched_file)
                    if file_path.is_file() and file_path.suffix == ".json":
                        files_to_process.append(file_path)
    else:
        parser.print_help()
        sys.exit(1)
    
    if not files_to_process:
        print("No files to process.")
        sys.exit(0)
    
    # Process files
    print("=" * 70)
    print("FILE DOCTOR - JSON Encoding Repair Utility")
    print("=" * 70)
    print()
    
    if args.check:
        print("CHECK MODE: Diagnosing files (no repairs will be made)")
        print()
        
        for file_path in files_to_process:
            is_valid, encoding, _ = diagnose_file(file_path)
            status = "[OK] VALID" if is_valid else "[ERR] INVALID"
            encoding_display = encoding if encoding else "UNKNOWN"
            
            print(f"{status:15} | Encoding: {encoding_display:15} | {file_path}")
        
        print()
        print("=" * 70)
        print("Check complete. Use without --check to repair files.")
        
    else:
        print("REPAIR MODE: Fixing files and rewriting as clean UTF-8")
        print()
        
        success_count = 0
        fail_count = 0
        
        for file_path in files_to_process:
            print(f"Processing: {file_path}")
            
            success, message = repair_file(file_path, create_backup=not args.no_backup)
            
            if success:
                print(f"  [OK] {message}")
                success_count += 1
            else:
                print(f"  [ERR] {message}")
                fail_count += 1
            
            print()
        
        print("=" * 70)
        print(f"SUMMARY: {success_count} file(s) repaired, {fail_count} file(s) failed")
        
        if fail_count > 0:
            sys.exit(1)

if __name__ == "__main__":
    main()


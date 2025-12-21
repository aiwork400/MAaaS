#!/usr/bin/env python3
"""
Shared File Utilities for MAaaS
Provides robust JSON/JSONL reading functions used by both dashboard and API server.
"""

import json
from pathlib import Path
from typing import Dict, List, Any


def read_json_file_robust(file_path: Path) -> Dict[str, Any]:
    """
    Robust JSON file reader that handles various encodings.
    
    Tries encodings in order:
    1. utf-8-sig (handles BOM)
    2. utf-8 (standard)
    3. utf-16 (auto-detect LE/BE)
    4. latin-1 (fallback for any byte sequence)
    
    Raises exception if all encodings fail.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check if file is empty
    if file_path.stat().st_size == 0:
        raise ValueError(f"File is empty: {file_path}")
    
    # Detect encoding by reading first bytes (BOM detection)
    with open(file_path, "rb") as f:
        first_bytes = f.read(4)
    
    # Determine encoding based on BOM or first bytes
    # Priority: UTF-8 BOM first (most common), then UTF-16, then standard UTF-8
    encodings = []
    if first_bytes.startswith(b'\xef\xbb\xbf'):
        # UTF-8 BOM - most common, try this first
        encodings = ["utf-8-sig", "utf-8"]
    elif first_bytes.startswith(b'\xff\xfe'):
        # UTF-16 LE BOM
        encodings = ["utf-16-le", "utf-16", "utf-8-sig", "utf-8"]
    elif first_bytes.startswith(b'\xfe\xff'):
        # UTF-16 BE BOM
        encodings = ["utf-16-be", "utf-16", "utf-8-sig", "utf-8"]
    elif first_bytes.startswith(b'\xff') or (len(first_bytes) > 1 and first_bytes[1] == 0):
        # Likely UTF-16 without BOM (starts with 0xff or has null bytes)
        encodings = ["utf-16", "utf-16-le", "utf-16-be", "utf-8-sig", "utf-8"]
    else:
        # Standard UTF encodings (try UTF-8 BOM first, then standard)
        encodings = ["utf-8-sig", "utf-8", "latin-1"]
    
    last_error = None
    
    for encoding in encodings:
        try:
            with open(file_path, "r", encoding=encoding) as f:
                content = f.read().strip()
                if not content:
                    raise ValueError(f"File appears empty after reading: {file_path}")
                return json.loads(content)
        except UnicodeDecodeError as e:
            last_error = e
            continue
        except json.JSONDecodeError as e:
            # If we get JSON decode error, the file was read but isn't valid JSON
            raise json.JSONDecodeError(
                f"Invalid JSON in {file_path} (tried encoding: {encoding}): {e.msg}",
                e.doc,
                e.pos
            )
        except Exception as e:
            last_error = e
            continue
    
    # If all encodings failed, raise the last error
    raise ValueError(f"Could not decode file {file_path} with any encoding. Last error: {last_error}")


def read_jsonl_file_robust(file_path: Path) -> List[Dict[str, Any]]:
    """
    Robust JSONL file reader that handles various encodings.
    
    Tries encodings in order:
    1. utf-8-sig (handles BOM)
    2. utf-8 (standard)
    3. utf-16 (auto-detect)
    4. latin-1 (fallback)
    
    Returns list of parsed JSON objects, skipping invalid lines.
    """
    if not file_path.exists():
        return []
    
    encodings = ["utf-8-sig", "utf-8", "utf-16", "utf-16-le", "utf-16-be", "latin-1"]
    logs = []
    
    for encoding in encodings:
        try:
            with open(file_path, "r", encoding=encoding) as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            logs.append(json.loads(line))
                        except json.JSONDecodeError:
                            continue
                return logs  # Successfully read all lines
        except UnicodeDecodeError:
            continue
    
    # If all encodings failed, return empty list
    return []


# File Doctor - JSON Encoding Repair Utility

## Overview

The **File Doctor** is a comprehensive utility that fixes JSON file encoding issues (BOM characters, encoding mismatches) and ensures all JSON files are stored as clean, standard UTF-8. This prevents encoding errors in both the Streamlit Dashboard and the FastAPI API Server.

## Why File Doctor?

**Root Cause Fix:** JSON files with BOM (Byte Order Mark) characters or incorrect encodings (UTF-16, etc.) cause both the Dashboard and API Server to fail when reading them. File Doctor scrubs files on disk to ensure they're clean UTF-8.

**Improved Observability:** The Dashboard and API Server now use shared robust file reading utilities (`file_utils.py`) that provide detailed error messages when encoding issues occur.

## Usage

### Check Files (No Repairs)

```powershell
# Check all JSON files in clients/ directory
python file_doctor.py --all --check

# Check specific files
python file_doctor.py clients/nexus_deployment_plan.json --check
```

### Repair Files

```powershell
# Repair all JSON files in clients/ directory
python file_doctor.py --all

# Repair specific files
python file_doctor.py clients/nexus_deployment_plan.json
python file_doctor.py clients/nexus_financial_assurance.json

# Repair without creating backups
python file_doctor.py --all --no-backup
```

### Examples

```powershell
# Check status of all JSON files
python file_doctor.py --all --check

# Repair all files (creates backups automatically)
python file_doctor.py --all

# Repair specific file
python file_doctor.py clients/nexus_deployment_plan.json

# Repair files in custom directory
python file_doctor.py --all --directory factory_logs
```

## What It Does

1. **Diagnoses** JSON files to detect encoding issues:
   - UTF-8 BOM (`\xef\xbb\xbf`)
   - UTF-16 LE/BE BOM (`\xff\xfe` or `\xfe\xff`)
   - Other encoding mismatches

2. **Repairs** files by:
   - Reading with robust encoding detection
   - Parsing JSON to validate structure
   - Rewriting as clean UTF-8 (no BOM)
   - Creating automatic backups (`.json.backup`)

3. **Verifies** repaired files are valid JSON

## Architecture

### Shared Utilities (`file_utils.py`)

Both `dashboard.py` and `api_server.py` now use the same robust file reading functions:

- `read_json_file_robust()` - Handles UTF-8, UTF-8 BOM, UTF-16, and fallback encodings
- `read_jsonl_file_robust()` - Same for JSONL (line-delimited) files

### Error Messages

The Dashboard now provides detailed error messages:
- `JSONDecodeError`: Shows exact position and encoding attempted
- `UnicodeDecodeError`: Shows encoding failure details
- File existence and size information

## Files Repaired

The following files have been cleaned:
- ✅ `clients/nexus_deployment_plan.json` → Clean UTF-8
- ✅ `clients/nexus_financial_assurance.json` → Clean UTF-8

Backups are saved as:
- `clients/nexus_deployment_plan.json.backup`
- `clients/nexus_financial_assurance.json.backup`

## Integration

### Dashboard (`dashboard.py`)
- Uses `file_utils.read_json_file_robust()` for all JSON loading
- Provides detailed error messages for debugging
- Handles encoding issues gracefully

### API Server (`api_server.py`)
- Uses `file_utils.read_json_file_robust()` for all JSON loading
- Same robust error handling as Dashboard
- Consistent behavior across both interfaces

## Best Practices

1. **Run File Doctor** after importing new JSON files
2. **Check files** before committing to version control
3. **Use `--check`** mode to diagnose issues without modifying files
4. **Keep backups** (default behavior) when repairing files

## Troubleshooting

If you see encoding errors:

1. Run `python file_doctor.py --all --check` to diagnose
2. Run `python file_doctor.py --all` to repair
3. Refresh your Dashboard/API Server
4. Check error messages for specific file issues

## Technical Details

### Supported Encodings (in priority order)
1. `utf-8-sig` - UTF-8 with BOM (most common issue)
2. `utf-8` - Standard UTF-8
3. `utf-16` - UTF-16 (auto-detect LE/BE)
4. `utf-16-le` - UTF-16 Little Endian
5. `utf-16-be` - UTF-16 Big Endian
6. `latin-1` - Fallback (can decode any byte sequence)

### BOM Detection

File Doctor detects BOMs by reading the first 4 bytes:
- `\xef\xbb\xbf` → UTF-8 BOM
- `\xff\xfe` → UTF-16 LE BOM
- `\xfe\xff` → UTF-16 BE BOM


#!/usr/bin/env python3
"""
Factory Reset Script for MAaaS Platform
========================================

This script safely archives the current active client deployment and resets
the factory to an IDLE state, ready for the next client intake.

SAFETY: This script requires explicit user confirmation before proceeding.
"""

import os
import shutil
import zipfile
from datetime import datetime
from pathlib import Path


def confirm_reset():
    """Ask user for explicit confirmation before proceeding."""
    print("\n" + "="*70)
    print("⚠️  FACTORY RESET WARNING ⚠️")
    print("="*70)
    print("\nThis will archive the current active client deployment.")
    print("The following will be archived:")
    print("  - clients/Nexus/ (all client-specific agents)")
    print("  - clients/*nexus* files (deployment plans, mappings, etc.)")
    print("  - factory_logs/ (all provenance logs)")
    print("\nThe factory will be reset to IDLE state.")
    print("\n" + "-"*70)
    
    response = input("\nAre you sure you want to archive the current active client? (Y/N): ").strip().upper()
    
    if response != 'Y':
        print("\n❌ Factory reset cancelled. No changes made.")
        return False
    
    # Double confirmation
    print("\n⚠️  FINAL CONFIRMATION REQUIRED ⚠️")
    response2 = input("Type 'ARCHIVE' to proceed, or anything else to cancel: ").strip()
    
    if response2 != 'ARCHIVE':
        print("\n❌ Factory reset cancelled. No changes made.")
        return False
    
    return True


def create_archive_directory():
    """Create archives/ directory if it doesn't exist."""
    archives_dir = Path("archives")
    archives_dir.mkdir(exist_ok=True)
    print(f"✓ Archives directory ready: {archives_dir.absolute()}")
    return archives_dir


def archive_client_data(archives_dir):
    """
    Archive all client-specific data:
    - clients/Nexus/ folder
    - All nexus-related files in clients/
    - factory_logs/ folder
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_name = f"Nexus_Financial_{timestamp}"
    archive_path = archives_dir / f"{archive_name}.zip"
    
    print(f"\n📦 Creating archive: {archive_name}.zip")
    
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Archive clients/Nexus/ folder
        nexus_dir = Path("clients/Nexus")
        if nexus_dir.exists():
            print(f"  → Archiving {nexus_dir}/")
            for root, dirs, files in os.walk(nexus_dir):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(Path("clients"))
                    zipf.write(file_path, f"clients/{arcname}")
                    print(f"    ✓ {arcname}")
        
        # Archive nexus-related files in clients/ directory
        clients_dir = Path("clients")
        nexus_files = [
            "nexus_deployment_plan.json",
            "nexus_deployment_plan.json.backup",
            "nexus_deployment_plan.md",
            "nexus_financial_assurance.json",
            "nexus_financial_assurance.json.backup",
            "nexus_mapping.py",
        ]
        
        for filename in nexus_files:
            file_path = clients_dir / filename
            if file_path.exists():
                print(f"  → Archiving {file_path}")
                zipf.write(file_path, f"clients/{filename}")
                print(f"    ✓ {filename}")
        
        # Archive factory_logs/ folder
        factory_logs_dir = Path("factory_logs")
        if factory_logs_dir.exists():
            print(f"  → Archiving {factory_logs_dir}/")
            for root, dirs, files in os.walk(factory_logs_dir):
                for file in files:
                    file_path = Path(root) / file
                    arcname = file_path.relative_to(factory_logs_dir)
                    zipf.write(file_path, f"factory_logs/{arcname}")
                    print(f"    ✓ factory_logs/{arcname}")
    
    print(f"\n✓ Archive created: {archive_path.absolute()}")
    return archive_path


def sanitize_directories():
    """
    Clean up directories after archiving:
    - Remove clients/Nexus/ folder
    - Remove nexus-related files from clients/
    - Clear factory_logs/ folder
    - Keep the directories themselves
    """
    print("\n🧹 Sanitizing directories...")
    
    # Remove clients/Nexus/ folder
    nexus_dir = Path("clients/Nexus")
    if nexus_dir.exists():
        print(f"  → Removing {nexus_dir}/")
        shutil.rmtree(nexus_dir)
        print(f"    ✓ Removed")
    
    # Remove nexus-related files from clients/
    clients_dir = Path("clients")
    nexus_files = [
        "nexus_deployment_plan.json",
        "nexus_deployment_plan.json.backup",
        "nexus_deployment_plan.md",
        "nexus_financial_assurance.json",
        "nexus_financial_assurance.json.backup",
        "nexus_mapping.py",
    ]
    
    for filename in nexus_files:
        file_path = clients_dir / filename
        if file_path.exists():
            print(f"  → Removing {file_path}")
            file_path.unlink()
            print(f"    ✓ Removed")
    
    # Clear factory_logs/ folder (but keep the directory)
    factory_logs_dir = Path("factory_logs")
    if factory_logs_dir.exists():
        print(f"  → Clearing {factory_logs_dir}/")
        for item in factory_logs_dir.iterdir():
            if item.is_file():
                item.unlink()
                print(f"    ✓ Removed {item.name}")
            elif item.is_dir():
                shutil.rmtree(item)
                print(f"    ✓ Removed {item.name}/")
        print(f"    ✓ Directory cleared (kept for future use)")
    
    # Ensure clients/ directory exists (should already exist, but just in case)
    clients_dir.mkdir(exist_ok=True)
    
    print("\n✓ Sanitization complete")


def reset_project_status():
    """Reset project_status.md to clean IDLE state."""
    status_file = Path("clients/project_status.md")
    
    print(f"\n📝 Resetting {status_file}")
    
    clean_status = """# PROJECT STATUS

**Status:** IDLE

**Active Client:** None

**Message:** System ready for new intake.

---
*Last reset: {timestamp}*
""".format(timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    status_file.write_text(clean_status, encoding='utf-8')
    print(f"  ✓ Project status reset to IDLE")


def main():
    """Main execution flow."""
    print("\n" + "="*70)
    print("🏭 MAaaS FACTORY RESET SCRIPT")
    print("="*70)
    
    # Safety check: Confirm user wants to proceed
    if not confirm_reset():
        return
    
    try:
        # Step 1: Create archives directory
        archives_dir = create_archive_directory()
        
        # Step 2: Archive client data
        archive_path = archive_client_data(archives_dir)
        
        # Step 3: Sanitize directories
        sanitize_directories()
        
        # Step 4: Reset project status
        reset_project_status()
        
        # Success message
        print("\n" + "="*70)
        print("✅ FACTORY RESET COMPLETE")
        print("="*70)
        print(f"\n✓ Client data archived to: {archive_path.name}")
        print("✓ Directories sanitized")
        print("✓ Project status reset to IDLE")
        print("\n🏭 Factory is now ready for new client intake.")
        print("\n")
        
    except Exception as e:
        print("\n" + "="*70)
        print("❌ ERROR DURING FACTORY RESET")
        print("="*70)
        print(f"\nAn error occurred: {str(e)}")
        print("\n⚠️  Please review the error and try again.")
        print("⚠️  If the archive was partially created, check the archives/ directory.")
        raise


if __name__ == "__main__":
    main()


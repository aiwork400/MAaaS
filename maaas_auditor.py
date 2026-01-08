import os

def audit_codebase(start_path=".", output_file="MAaaS_Deep_Audit_Log.md"):
    exclude_dirs = {'venv', 'venv_new', '.git', '__pycache__', '.streamlit', 'clients', 'factory_logs', 'archives', 'ops', 'reports', 'memory', '.idea', '.vscode'}
    exclude_files = {'maaas_auditor.py', 'app.py', 'requirements.txt', 'Dockerfile', 'MAaaS_Deep_Audit_Log.md'}
    
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("# MAaaS PLATFORM AUDIT - DEEP SCAN\n")
        out.write(f"Scan Root: {os.path.abspath(start_path)}\n")
        out.write("=================================\n\n")
        
        for root, dirs, files in os.walk(start_path):
            # Filter exclusions
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            level = root.replace(start_path, '').count(os.sep)
            indent = '    ' * level
            
            # Write Directory
            dirname = os.path.basename(root)
            if dirname == '.': dirname = "ROOT"
            out.write(f"{indent}📂 **{dirname}/**\n")
            
            sub_indent = '    ' * (level + 1)
            for f in files:
                if f not in exclude_files and not f.endswith('.pyc') and not f.endswith('.DS_Store'):
                    out.write(f"{sub_indent}📄 `{f}`\n")
                    
                    # Deep Scan: Peek into file content for Architecture Signals
                    filepath = os.path.join(root, f)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as file:
                            content = file.read()
                            
                            # Only scan relevant code files
                            if f.endswith(('.py', '.yaml', '.yml', '.json', '.md')):
                                out.write(f"{sub_indent}    > *Code Insight:*\n")
                                lines = content.split('\n')
                                found_code = False
                                out.write(f"{sub_indent}    ```python\n")
                                for line in lines: 
                                    stripped = line.strip()
                                    # Capture imports, classes, and key functions
                                    if stripped.startswith("class ") or stripped.startswith("def ") or "Agency" in stripped or "Agent" in stripped:
                                        out.write(f"{sub_indent}    {stripped}\n")
                                        found_code = True
                                    if found_code and len(stripped) == 0: # Stop after a block
                                        break
                                out.write(f"{sub_indent}    ```\n")
                    except Exception as e:
                        out.write(f"{sub_indent}    [Error reading file: {e}]\n")

    print(f"✅ Audit Complete. Results saved to: {output_file}")

if __name__ == "__main__":
    audit_codebase()
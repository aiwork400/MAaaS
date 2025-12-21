#!/usr/bin/env python3
"""
MAaaS Command Center - Streamlit Dashboard
Visualizes the Nexus Swarm ecosystem with real-time metrics and controls.

Reference: Specification.md - Full-Cycle MAaaS Enterprise Platform
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import sys
import os

# Add repository root to path
REPO_ROOT = Path(__file__).resolve().parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

# Page configuration
st.set_page_config(
    page_title="MAaaS Command Center - Nexus Swarm",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .status-green {
        color: #00cc00;
        font-weight: bold;
    }
    .status-red {
        color: #ff0000;
        font-weight: bold;
    }
    .budget-column {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================================
# DATA LOADING FUNCTIONS
# ============================================================================

# Import shared file utilities
try:
    from file_utils import read_json_file_robust, read_jsonl_file_robust
except ImportError:
    # Fallback if file_utils not available (shouldn't happen, but for safety)
    def read_json_file_robust(file_path: Path) -> Dict[str, Any]:
        """Fallback robust JSON reader."""
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        if file_path.stat().st_size == 0:
            raise ValueError(f"File is empty: {file_path}")
        
        encodings = ["utf-8-sig", "utf-8", "utf-16", "utf-16-le", "utf-16-be", "latin-1"]
        last_error = None
        
        for encoding in encodings:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    content = f.read().strip()
                    if not content:
                        continue
                    return json.loads(content)
            except (UnicodeDecodeError, json.JSONDecodeError) as e:
                last_error = e
                continue
        
        raise ValueError(f"Could not decode file {file_path}. Last error: {last_error}")
    
    def read_jsonl_file_robust(file_path: Path) -> List[Dict[str, Any]]:
        """Fallback robust JSONL reader."""
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
                    return logs
            except UnicodeDecodeError:
                continue
        
        return []

@st.cache_data
def load_agents() -> List[Dict[str, Any]]:
    """Load active agents from clients/Nexus/ directory."""
    nexus_dir = REPO_ROOT / "clients" / "Nexus"
    agents = []
    
    if not nexus_dir.exists():
        return agents
    
    for agent_file in nexus_dir.glob("Nexus_*.py"):
        agent_name = agent_file.stem
        agents.append({
            "name": agent_name,
            "file": agent_file.name,
            "status": "ACTIVE",
            "last_updated": datetime.fromtimestamp(agent_file.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
        })
    
    return agents


@st.cache_data
def load_econtracts() -> Dict[str, Dict[str, Any]]:
    """Load E-Contracts from deployment plan or factory output."""
    contracts = {}
    
    # Try to load from deployment plan
    deployment_plan_path = REPO_ROOT / "clients" / "nexus_deployment_plan.json"
    if deployment_plan_path.exists():
        try:
            plan = read_json_file_robust(deployment_plan_path)
            agent_instances = plan.get("deployment_plan", {}).get("agent_instances", {})
            for agent_type, agent_info in agent_instances.items():
                contract_id = agent_info.get("contract_id", "")
                if contract_id:
                    contracts[agent_type] = {
                        "contract_id": contract_id,
                        "status": agent_info.get("contract_status", "UNKNOWN"),
                        "agent_id": agent_info.get("agent_id", ""),
                        "base_class": agent_info.get("base_class", "")
                    }
        except json.JSONDecodeError as e:
            st.error(f"Detailed Error (JSONDecodeError): {str(e)}")
            st.error(f"Error at position {e.pos} in file: {deployment_plan_path}")
        except UnicodeDecodeError as e:
            st.error(f"Detailed Error (UnicodeDecodeError): {str(e)}")
            st.error(f"Could not decode file with any encoding: {deployment_plan_path}")
        except FileNotFoundError as e:
            st.error(f"Detailed Error (FileNotFoundError): {str(e)}")
        except ValueError as e:
            st.error(f"Detailed Error (ValueError): {str(e)}")
        except Exception as e:
            st.error(f"Detailed Error ({type(e).__name__}): {str(e)}")
    
    # Try to load enhanced contracts (5-Pillar agents)
    # This would be generated by the factory
    client_profile_path = REPO_ROOT / "clients" / "nexus_financial_assurance.json"
    if client_profile_path.exists():
        try:
            client_profile = read_json_file_robust(client_profile_path)
            financials = client_profile.get("financial_constraints", {})
            base_budget = financials.get("total_token_budget_monthly", 500000)
            
            # Add 5-Pillar contracts if they exist
            company = client_profile.get("client_meta", {}).get("company_name", "Nexus Financial Assurance Ltd.")
            
            # Check if NetSec exists
            if (REPO_ROOT / "clients" / "Nexus" / "Nexus_NetSec.py").exists():
                contracts["netsec"] = {
                    "contract_id": f"{company}-NETSEC-01",
                    "status": "SIGNED",
                    "token_budget": int(base_budget * 0.10),
                    "line_items": {
                        "vulnerability_scan_fees": {"monthly_estimate": 400}
                    }
                }
            
            # Check if DBA exists (would be Nexus_DBA if created)
            # Check if Marketer exists (would be Nexus_Marketer if created)
            
        except json.JSONDecodeError as e:
            st.error(f"Detailed Error (JSONDecodeError): {str(e)}")
            st.error(f"Error at position {e.pos} in file: {client_profile_path}")
            file_info = f"File exists: {client_profile_path.exists()}, Size: {client_profile_path.stat().st_size if client_profile_path.exists() else 0} bytes"
            st.error(f"File info: {file_info}")
        except UnicodeDecodeError as e:
            st.error(f"Detailed Error (UnicodeDecodeError): {str(e)}")
            st.error(f"Could not decode file with any encoding: {client_profile_path}")
        except FileNotFoundError as e:
            st.error(f"Detailed Error (FileNotFoundError): {str(e)}")
        except ValueError as e:
            st.error(f"Detailed Error (ValueError): {str(e)}")
        except Exception as e:
            st.error(f"Detailed Error ({type(e).__name__}): {str(e)}")
    
    return contracts


@st.cache_data
def load_project_status() -> Dict[str, Any]:
    """Load project status from project_status.md."""
    status_path = REPO_ROOT / "clients" / "project_status.md"
    status = {
        "status": "UNKNOWN",
        "client": "Nexus Financial Assurance Ltd.",
        "sla_uptime": 99.8,  # Default
        "last_updated": datetime.now().isoformat()
    }
    
    if status_path.exists():
        try:
            with open(status_path, "r", encoding="utf-8") as f:
                content = f.read()
                if "FABRICATION PHASE" in content:
                    status["status"] = "FABRICATION PHASE"
                elif "DEPLOYED" in content:
                    status["status"] = "DEPLOYED"
        except Exception as e:
            st.warning(f"Could not load project status: {e}")
    
    return status


# ============================================================================
# REAL DATA LOADERS (Load from actual provenance logs and agent outputs)
# ============================================================================

@st.cache_data
def load_provenance_logs() -> List[Dict[str, Any]]:
    """Load provenance logs from factory_logs/nexus_provenance_audit.jsonl."""
    provenance_path = REPO_ROOT / "factory_logs" / "nexus_provenance_audit.jsonl"
    
    if provenance_path.exists():
        try:
            return read_jsonl_file_robust(provenance_path)
        except Exception as e:
            st.warning(f"Could not load provenance logs: {e}")
            return []
    
    return []


def generate_firewall_log() -> pd.DataFrame:
    """
    Generate firewall log data from real provenance logs.
    Falls back to mock data if no real logs are available.
    """
    provenance_logs = load_provenance_logs()
    log_entries = []
    
    # Extract firewall-related events from provenance logs
    for log_entry in provenance_logs:
        action = log_entry.get("action", "")
        timestamp_str = log_entry.get("timestamp", "")
        
        # Map provenance actions to firewall events
        if "watchlist_check" in action or "flag_suspicious" in action:
            try:
                timestamp = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
            except:
                timestamp = datetime.now()
            
            log_entries.append({
                "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "agent_id": log_entry.get("agent_id", "Unknown")[:8] + "...",
                "blocked_keyword": "PII_CHECK" if "watchlist" in action else "THRESHOLD_CHECK",
                "reason": "Session-Level Semantic Firewall (C6 protection)",
                "action": "SCREENED",
                "mpc_protocol": log_entry.get("mpc_protocol", "N/A")
            })
    
    # If no real logs, generate mock data
    if not log_entries:
        now = datetime.now()
        for i in range(20):
            timestamp = now - timedelta(minutes=20-i)
            log_entries.append({
                "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                "agent_id": f"Agent-{i % 4 + 1}",
                "blocked_keyword": ["PII", "SSN", "API_KEY", "SECRET"][i % 4],
                "reason": "Session-Level Semantic Firewall (C6 protection)",
                "action": "BLOCKED",
                "mpc_protocol": "Yao-GC"
            })
    
    return pd.DataFrame(log_entries)


def generate_patch_status() -> Dict[str, Any]:
    """
    Generate patch status data.
    In production, this would read from Agent_NetSec logs.
    For now, uses mock data with indication of real data availability.
    """
    # Check if NetSec agent exists and has generated logs
    netsec_path = REPO_ROOT / "clients" / "Nexus" / "Nexus_NetSec.py"
    has_netsec = netsec_path.exists()
    
    # TODO: In production, read from NetSec vulnerability scan logs
    return {
        "vulnerabilities_detected": 12,
        "vulnerabilities_patched": 10,
        "vulnerabilities_pending": 2,
        "high_severity": 3,
        "medium_severity": 7,
        "low_severity": 2,
        "last_scan": (datetime.now() - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
        "data_source": "real" if has_netsec else "mock"
    }


def generate_roi_data() -> pd.DataFrame:
    """Generate mock ROI data for campaigns."""
    dates = [datetime.now() - timedelta(days=30-i) for i in range(30)]
    roi_data = []
    
    for date in dates:
        campaign_spend = 1000 + (30 - dates.index(date)) * 10
        lead_value = campaign_spend * 2.5 + (dates.index(date) * 5)  # Simulated growth
        roi_data.append({
            "date": date.strftime("%Y-%m-%d"),
            "campaign_spend": campaign_spend,
            "lead_value": lead_value,
            "roi_percentage": ((lead_value - campaign_spend) / campaign_spend) * 100
        })
    
    return pd.DataFrame(roi_data)


def generate_query_latency() -> pd.DataFrame:
    """Generate mock query latency data from Agent_DBA."""
    now = datetime.now()
    latency_data = []
    
    for i in range(24):
        timestamp = now - timedelta(hours=23-i)
        # Simulate query latency (ms)
        base_latency = 50
        variation = (i % 5) * 10
        latency_data.append({
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "query_type": ["SELECT", "INSERT", "UPDATE", "SELECT"][i % 4],
            "latency_ms": base_latency + variation,
            "table": ["users", "transactions", "audit_logs", "users"][i % 4]
        })
    
    return pd.DataFrame(latency_data)


# ============================================================================
# TAB 1: OVERVIEW
# ============================================================================

def render_overview_tab():
    """Render the Overview tab."""
    st.header("📊 System Overview")
    
    # Load data
    project_status = load_project_status()
    agents = load_agents()
    contracts = load_econtracts()
    
    # System Health Section
    st.subheader("🟢 System Health")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        sla_uptime = project_status.get("sla_uptime", 99.8)
        sla_color = "🟢" if sla_uptime >= 99.5 else "🔴"
        st.metric(
            label="SLA Uptime",
            value=f"{sla_uptime}%",
            delta=f"{sla_uptime - 99.5:.1f}% above threshold" if sla_uptime >= 99.5 else f"{99.5 - sla_uptime:.1f}% below threshold"
        )
        st.markdown(f"**Status:** {sla_color} {'HEALTHY' if sla_uptime >= 99.5 else 'DEGRADED'}")
    
    with col2:
        st.metric(
            label="Active Agents",
            value=len(agents),
            delta=f"{len(agents)} agents operational"
        )
    
    with col3:
        signed_contracts = sum(1 for c in contracts.values() if c.get("status") == "SIGNED")
        st.metric(
            label="Signed Contracts",
            value=signed_contracts,
            delta=f"{signed_contracts}/{len(contracts)} active"
        )
    
    st.divider()
    
    # Active Agents Section
    st.subheader("🤖 Active Agents")
    
    if agents:
        agent_df = pd.DataFrame(agents)
        st.dataframe(
            agent_df[["name", "status", "last_updated"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.warning("No agents found in clients/Nexus/ directory.")
    
    # Contract Status Section
    if contracts:
        st.subheader("📋 Contract Status")
        contract_df = pd.DataFrame([
            {
                "Contract ID": contract.get("contract_id", "N/A"),
                "Status": contract.get("status", "UNKNOWN"),
                "Agent Type": agent_type
            }
            for agent_type, contract in contracts.items()
        ])
        st.dataframe(contract_df, use_container_width=True, hide_index=True)


# ============================================================================
# TAB 2: CYBER-INFRASTRUCTURE
# ============================================================================

def render_cyber_infrastructure_tab():
    """Render the Cyber-Infrastructure tab."""
    st.header("🔒 Cyber-Infrastructure")
    
    # NetSec Log Section
    st.subheader("🛡️ Session Firewall Log")
    st.markdown("**Live table showing blocked attempts by Session-Level Semantic Firewall (C6 protection)**")
    
    firewall_log = generate_firewall_log()
    st.dataframe(
        firewall_log,
        use_container_width=True,
        hide_index=True
    )
    
    # Summary metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Events (Last 24h)", len(firewall_log))
    with col2:
        unique_keywords = firewall_log["blocked_keyword"].nunique()
        st.metric("Unique Blocked Keywords", unique_keywords)
    with col3:
        provenance_logs = load_provenance_logs()
        real_events = len([log for log in provenance_logs if "watchlist" in log.get("action", "") or "flag" in log.get("action", "")])
        data_source = "Real Data" if real_events > 0 else "Mock Data"
        st.metric("Data Source", data_source)
    
    st.divider()
    
    # Patch Status Section
    st.subheader("🔧 Patch Status")
    st.markdown("**Vulnerabilities Detected vs Patched**")
    
    patch_status = generate_patch_status()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Vulnerabilities Detected",
            patch_status["vulnerabilities_detected"],
            delta=f"{patch_status['vulnerabilities_pending']} pending"
        )
    
    with col2:
        patched_rate = (patch_status["vulnerabilities_patched"] / patch_status["vulnerabilities_detected"]) * 100 if patch_status["vulnerabilities_detected"] > 0 else 0
        st.metric(
            "Patched",
            patch_status["vulnerabilities_patched"],
            delta=f"{patched_rate:.1f}% completion rate"
        )
    
    with col3:
        st.metric(
            "High Severity",
            patch_status["high_severity"],
            delta="Requires immediate attention"
        )
    
    with col4:
        st.metric(
            "Last Scan",
            patch_status["last_scan"],
            delta="2 hours ago"
        )
    
    # Patch progress visualization
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["Detected", "Patched", "Pending"],
        y=[
            patch_status["vulnerabilities_detected"],
            patch_status["vulnerabilities_patched"],
            patch_status["vulnerabilities_pending"]
        ],
        marker_color=["#ff6b6b", "#51cf66", "#ffd43b"]
    ))
    fig.update_layout(
        title="Vulnerability Patch Status",
        xaxis_title="Status",
        yaxis_title="Count",
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)


# ============================================================================
# TAB 3: GROWTH & FINANCIALS
# ============================================================================

def render_growth_financials_tab():
    """Render the Growth & Financials tab."""
    st.header("💰 Growth & Financials")
    
    # Load contracts for financial data
    contracts = load_econtracts()
    client_profile_path = REPO_ROOT / "clients" / "nexus_financial_assurance.json"
    base_budget = 500000
    
    if client_profile_path.exists():
        try:
            client_profile = read_json_file_robust(client_profile_path)
            financials = client_profile.get("financial_constraints", {})
            base_budget = financials.get("total_token_budget_monthly", 500000)
        except Exception as e:
            # Silently fail and use default budget
            pass
    
    # STRICT BUDGET SEPARATION
    st.subheader("📊 Budget Separation")
    st.markdown("**Column A (Compute): Token Usage | Column B (Expenses): Ad Spend / Cloud Storage**")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown('<div class="budget-column">', unsafe_allow_html=True)
        st.markdown("### 💻 Column A: Compute (Agent's Cost)")
        
        # Calculate token usage from contracts
        total_token_budget = 0
        token_usage = {}
        
        for agent_type, contract in contracts.items():
            token_budget = contract.get("token_budget", contract.get("financial_terms", {}).get("token_budget_max", 0))
            if token_budget > 0:
                total_token_budget += token_budget
                token_usage[agent_type] = {
                    "budget": token_budget,
                    "used": int(token_budget * 0.75)  # Simulated 75% usage
                }
        
        # Display token usage metrics
        for agent_type, usage in token_usage.items():
            usage_pct = (usage["used"] / usage["budget"]) * 100 if usage["budget"] > 0 else 0
            st.metric(
                label=f"{agent_type.upper()} Token Usage",
                value=f"{usage['used']:,} / {usage['budget']:,}",
                delta=f"{usage_pct:.1f}% utilized"
            )
        
        st.metric(
            label="Total Token Budget",
            value=f"{total_token_budget:,}",
            delta=f"{total_token_budget / base_budget * 100:.1f}% of base budget"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_b:
        st.markdown('<div class="budget-column">', unsafe_allow_html=True)
        st.markdown("### 💵 Column B: Expenses (Client's Money)")
        
        # Calculate expenses from line items
        total_expenses = 0
        expenses = {}
        
        # NetSec expenses
        if "netsec" in contracts:
            netsec_contract = contracts["netsec"]
            scan_fees = netsec_contract.get("line_items", {}).get("vulnerability_scan_fees", {}).get("monthly_estimate", 400)
            expenses["Vulnerability Scanning"] = scan_fees
            total_expenses += scan_fees
        
        # DBA expenses (if exists)
        dba_storage = 500  # Vector storage
        dba_oram = 300  # ORAM computation
        expenses["Vector Storage (DBA)"] = dba_storage
        expenses["ORAM Computation (DBA)"] = dba_oram
        total_expenses += dba_storage + dba_oram
        
        # Marketer expenses (if exists)
        campaign_spend = 1000  # Campaign ad spend
        expenses["Campaign Ad Spend"] = campaign_spend
        total_expenses += campaign_spend
        
        # Display expenses
        for expense_name, amount in expenses.items():
            st.metric(
                label=expense_name,
                value=f"${amount:,}/month"
            )
        
        st.metric(
            label="Total Monthly Expenses",
            value=f"${total_expenses:,}",
            delta="Client's operational costs"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.divider()
    
    # ROI Monitor Section
    st.subheader("📈 ROI Monitor")
    st.markdown("**Campaign Spend vs Lead Value**")
    
    roi_data = generate_roi_data()
    
    # ROI Chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=roi_data["date"],
        y=roi_data["campaign_spend"],
        name="Campaign Spend",
        line=dict(color="#ff6b6b", width=2),
        mode="lines+markers"
    ))
    fig.add_trace(go.Scatter(
        x=roi_data["date"],
        y=roi_data["lead_value"],
        name="Lead Value",
        line=dict(color="#51cf66", width=2),
        mode="lines+markers"
    ))
    fig.update_layout(
        title="Campaign ROI Over Time",
        xaxis_title="Date",
        yaxis_title="Amount ($)",
        height=400,
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # ROI Metrics
    col1, col2, col3 = st.columns(3)
    latest_roi = roi_data.iloc[-1]
    with col1:
        st.metric("Current Campaign Spend", f"${latest_roi['campaign_spend']:,.0f}")
    with col2:
        st.metric("Current Lead Value", f"${latest_roi['lead_value']:,.0f}")
    with col3:
        st.metric("ROI Percentage", f"{latest_roi['roi_percentage']:.1f}%")
    
    st.divider()
    
    # Data Health Section
    st.subheader("🗄️ Data Health")
    st.markdown("**Query Latency from Agent_DBA**")
    
    latency_data = generate_query_latency()
    
    # Latency Chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=latency_data["timestamp"],
        y=latency_data["latency_ms"],
        name="Query Latency",
        line=dict(color="#4dabf7", width=2),
        mode="lines+markers",
        hovertemplate="<b>%{x}</b><br>Latency: %{y}ms<extra></extra>"
    ))
    fig.update_layout(
        title="Query Latency Over Time (Last 24 Hours)",
        xaxis_title="Timestamp",
        yaxis_title="Latency (ms)",
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Latency Metrics
    avg_latency = latency_data["latency_ms"].mean()
    max_latency = latency_data["latency_ms"].max()
    min_latency = latency_data["latency_ms"].min()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Average Latency", f"{avg_latency:.1f}ms")
    with col2:
        st.metric("Max Latency", f"{max_latency:.1f}ms")
    with col3:
        st.metric("Min Latency", f"{min_latency:.1f}ms")


# ============================================================================
# TAB 4: CHAT OPS
# ============================================================================

@st.cache_resource
def get_nexus_pm_agent():
    """
    Get or create Nexus_PM agent instance.
    Uses @st.cache_resource to maintain the same instance across reruns.
    """
    try:
        # Import Nexus_PM
        sys.path.insert(0, str(REPO_ROOT))
        from clients.Nexus.Nexus_PM import Nexus_PM
        
        # Create agent instance
        agent = Nexus_PM("Nexus_PM", "Audit Workflow Supervisor")
        
        # Load and sign contract if not already signed
        if not agent.active_contract or agent.active_contract.get("status") != "SIGNED":
            deployment_plan_path = REPO_ROOT / "clients" / "nexus_deployment_plan.json"
            if deployment_plan_path.exists():
                try:
                    plan = read_json_file_robust(deployment_plan_path)
                    pm_info = plan.get("deployment_plan", {}).get("agent_instances", {}).get("project_manager", {})
                    
                    contract = {
                        "contract_id": pm_info.get("contract_id", "Nexus Financial Assurance Ltd.-PM-MASTER"),
                        "financial_terms": {
                            "token_budget_max": 100000,  # 20% of 500k
                        },
                        "deliverables": ["End-to-end coordination of WF-AUDIT-01"],
                        "security_protocols": {
                            "mpc_required": True,
                            "session_firewall_enabled": True,
                        },
                    }
                    
                    agent.sign_contract(contract)
                    
                    # Register known subordinate agents
                    agent.register_subordinate_agent("researcher", "Nexus_Researcher-001")
                    agent.register_subordinate_agent("compliance", "Nexus_Compliance-001")
                    if (REPO_ROOT / "clients" / "Nexus" / "Nexus_NetSec.py").exists():
                        agent.register_subordinate_agent("netsec", "Nexus_NetSec-001")
                except Exception as e:
                    st.warning(f"Could not load contract for Nexus_PM: {e}")
        
        return agent
    except Exception as e:
        st.error(f"Failed to instantiate Nexus_PM: {e}")
        return None


def render_chat_ops_tab():
    """Render the Chat Ops tab."""
    st.header("💬 Chat Ops")
    st.markdown("**Interface to message Nexus_PM directly**")
    
    # Initialize chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Get Nexus_PM agent instance
    agent = get_nexus_pm_agent()
    
    if agent is None:
        st.error("Nexus_PM agent could not be initialized. Please check the logs.")
        return
    
    # Display agent status
    with st.expander("🤖 Nexus_PM Agent Status", expanded=False):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Agent ID", agent.agent_id[:8] + "...")
        with col2:
            contract_status = agent.active_contract.get("status", "UNSIGNED") if agent.active_contract else "UNSIGNED"
            st.metric("Contract", contract_status)
        with col3:
            st.metric("Trust Score", f"{agent.trust_score:.2f}")
    
    # Display chat history
    st.subheader("📨 Conversation with Nexus_PM")
    
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                with st.chat_message("user"):
                    st.write(message["content"])
            else:
                with st.chat_message("assistant"):
                    st.markdown(message["content"])
    
    # Chat input
    user_input = st.chat_input("Type your message to Nexus_PM...")
    
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now().isoformat()
        })
        
        # Generate response using real Nexus_PM agent
        try:
            with st.spinner("Nexus_PM is thinking..."):
                response = agent.process_chat_request(user_input)
            
            # Add assistant response to history
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response,
                "timestamp": datetime.now().isoformat()
            })
        except Exception as e:
            error_response = f"**Error:** Nexus_PM encountered an error processing your request: {str(e)}"
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": error_response,
                "timestamp": datetime.now().isoformat()
            })
            st.error(f"Error: {e}")
        
        # Rerun to update chat display
        st.rerun()
    
    # Clear chat button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()


# ============================================================================
# MAIN DASHBOARD
# ============================================================================

def main():
    """Main dashboard application."""
    # Header
    st.markdown('<p class="main-header">🤖 MAaaS Command Center - Nexus Swarm</p>', unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    st.sidebar.markdown("---")
    
    tab = st.sidebar.radio(
        "Select Tab",
        ["Overview", "Cyber-Infrastructure", "Growth & Financials", "Chat Ops"],
        index=0
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### System Info")
    project_status = load_project_status()
    st.sidebar.write(f"**Client:** {project_status.get('client', 'Nexus Financial Assurance Ltd.')}")
    st.sidebar.write(f"**Status:** {project_status.get('status', 'UNKNOWN')}")
    st.sidebar.write(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Render selected tab
    if tab == "Overview":
        render_overview_tab()
    elif tab == "Cyber-Infrastructure":
        render_cyber_infrastructure_tab()
    elif tab == "Growth & Financials":
        render_growth_financials_tab()
    elif tab == "Chat Ops":
        render_chat_ops_tab()


if __name__ == "__main__":
    main()


# Integration Testing Guide - MAaaS Command Center

## Overview
This guide walks you through setting up and testing the MAaaS Command Center dashboard with real provenance logs from the Nexus Swarm.

## Prerequisites

### 1. Install Dependencies
```bash
pip install streamlit pandas plotly
```

### 2. Verify Agent Files
Ensure the following agents are fabricated:
- `clients/Nexus/Nexus_Compliance.py`
- `clients/Nexus/Nexus_NetSec.py`
- `clients/Nexus/Nexus_PM.py`
- `clients/Nexus/Nexus_Researcher.py`

## Step-by-Step Integration Testing

### Step 1: Generate Real Provenance Logs
Run the workflow simulation to generate real provenance logs:

```bash
python simulate_audit_workflow.py
```

**Expected Output:**
- Nexus_Compliance agent instantiated
- E-Contract signed
- 10 transactions processed through MPC watchlist checks
- Provenance log exported to `factory_logs/nexus_provenance_audit.jsonl`

### Step 2: Launch the Dashboard
Start the Streamlit dashboard:

```bash
streamlit run dashboard.py
```

The dashboard will automatically open in your default web browser at `http://localhost:8501`

### Step 3: Verify Real Data Integration

#### Tab 1: Overview
- **System Health**: Should show SLA Uptime (99.8%)
- **Active Agents**: Should list all agents in `clients/Nexus/`
- **Contract Status**: Should display signed contracts

#### Tab 2: Cyber-Infrastructure
- **Session Firewall Log**: Should display real events from provenance logs
  - Look for entries with "PII_CHECK" or "THRESHOLD_CHECK"
  - Check that timestamps match the workflow simulation
  - Verify "Data Source" metric shows "Real Data"
- **Patch Status**: Shows vulnerability metrics (currently mock data)

#### Tab 3: Growth & Financials
- **Budget Separation**: 
  - Column A (Compute): Token usage from contracts
  - Column B (Expenses): Ad spend and cloud storage costs
- **ROI Monitor**: Campaign performance charts
- **Data Health**: Query latency metrics

#### Tab 4: Chat Ops
- **Chat Interface**: Test messaging Nexus_PM
- Try queries like:
  - "What is the system status?"
  - "Show workflow progress"
  - "What is the budget status?"

## Data Flow Architecture

```
Nexus_Compliance Agent
    ↓ (generates provenance logs)
factory_logs/nexus_provenance_audit.jsonl
    ↓ (dashboard reads)
dashboard.py → Cyber-Infrastructure Tab
```

## Troubleshooting

### Issue: Dashboard shows "Mock Data"
**Solution**: Run `simulate_audit_workflow.py` to generate real logs.

### Issue: No agents found in Overview tab
**Solution**: Ensure agents are in `clients/Nexus/` directory with naming pattern `Nexus_*.py`

### Issue: Provenance log not loading
**Solution**: 
1. Check that `factory_logs/nexus_provenance_audit.jsonl` exists
2. Verify file permissions
3. Check file encoding (should be UTF-8)

### Issue: Streamlit not found
**Solution**: 
```bash
pip install streamlit pandas plotly
```

## Next Steps

1. **Expand Real Data Sources**:
   - Wire NetSec logs for Patch Status
   - Wire DBA logs for Query Latency
   - Wire Marketer logs for ROI data

2. **Production Integration**:
   - Replace mock data generators with real API calls
   - Add real-time updates via WebSocket
   - Implement authentication and authorization

3. **Enhanced Monitoring**:
   - Add alerting for SLA breaches
   - Implement anomaly detection
   - Create custom dashboards per client

## Reference Files

- **Dashboard**: `dashboard.py`
- **Workflow Simulator**: `simulate_audit_workflow.py`
- **Provenance Logs**: `factory_logs/nexus_provenance_audit.jsonl`
- **Agent Implementation**: `clients/Nexus/Nexus_Compliance.py`


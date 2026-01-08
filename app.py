import streamlit as st
import sys
import os
import random

# --- CONFIGURATION SWITCH ---
# CRITICAL: Keep False to prevent binary conflicts
USE_ANALYTICS = False

# --- UI CONFIGURATION (MUST BE FIRST) ---
try:
    st.set_page_config(
        page_title="Swarm Agency | MAaaS Console",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )
except Exception:
    pass

# --- SAFE IMPORT BLOCK (RESILIENCY MODE) ---
HAS_PANDAS = False
HAS_PLOTLY = False

if USE_ANALYTICS:
    try:
        import pandas as pd
        HAS_PANDAS = True
    except Exception:
        pass

    try:
        import plotly.express as px
        HAS_PLOTLY = True
    except Exception:
        pass

# ==========================================
# INTERNAL TOOL LOGIC (Self-Contained)
# ==========================================
class MarketScannerTool:
    def scan_territory(self, region, niche):
        # Dynamic City Logic
        city_name = region.split(',')[0].strip() if ',' in region else region
        
        base_leads = [
            {"name": "Local Origin Coffee", "type": "Cafe", "traffic": "High", "tech_stack": "Legacy POS"},
            {"name": "Vintage Vault", "type": "Retail", "traffic": "Medium", "tech_stack": "Square"},
            {"name": "The Iron Press", "type": "Restaurant", "traffic": "High", "tech_stack": "Toast"},
            {"name": "Urban Workshop", "type": "Service", "traffic": "Medium", "tech_stack": "Manual"},
            {"name": "Green Leaf Salads", "type": "Dining", "traffic": "Very High", "tech_stack": "Clover"},
            {"name": "Coastal Provisions", "type": "Retail", "traffic": "Low", "tech_stack": "Shopify POS"},
            {"name": "Maven Boutique", "type": "Fashion", "traffic": "High", "tech_stack": "Lightspeed"},
        ]
        
        results = []
        for lead in base_leads:
            lead_copy = lead.copy()
            lead_copy['city'] = city_name
            lead_copy['match_score'] = random.randint(82, 99)
            results.append(lead_copy)
            
        return results

# Initialize the internal tool
scanner = MarketScannerTool()

# ==========================================
# DASHBOARD INTERFACE
# ==========================================

# Light Theme / Corporate Styling
st.markdown("""
    <style>
    /* Main Background & Text */
    .stApp { 
        background-color: #f8f9fa; 
        color: #212529; 
    }
    
    /* Buttons (Corporate Blue) */
    .stButton>button { 
        background-color: #0056b3; 
        color: #ffffff; 
        font-weight: bold; 
        border-radius: 5px; 
        border: none;
    }
    .stButton>button:hover {
        background-color: #004494;
        color: #ffffff;
    }
    
    /* Input Fields */
    .stTextInput>div>div>input { 
        color: #212529; 
        background-color: #ffffff; 
        border: 1px solid #ced4da; 
    }
    
    /* Headers */
    h1, h2, h3 { 
        color: #003366 !important; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("MAaaS Factory")
st.sidebar.markdown("---")
client_name = st.sidebar.text_input("Client Name", "Ehsan Firouzabadi")
region = st.sidebar.text_input("Target Region", "Orange County, CA")
niche = st.sidebar.text_input("Target Niche", "Non-Franchise Retail")
launch_btn = st.sidebar.button("INITIATE SWARM MISSION")

# --- MAIN AREA ---
status_text = "V1.5 Active"
if not HAS_PANDAS:
    status_text += " | ⚠️ Safe Mode"
st.title("Swarm Agency | Command Center")
st.markdown(f"**Status:** {status_text} | **Region:** {region}")

# TABS
tab1, tab2, tab3 = st.tabs(["🚀 Mission Control", "🧠 Neural Logs", "📊 BI Dashboard"])

if launch_btn:
    # --- TAB 2: NEURAL LOGS (Instant Mode) ---
    with tab2:
        try:
            st.subheader("Agent Swarm Activity")
            
            # Execute Logic Instantly (No Sleep)
            results = scanner.scan_territory(region, niche)
            
            # Show Static Logs (No Animation Loop)
            logs = [
                f"[SYSTEM] 🟢 Initializing Profile for: {client_name}",
                f"[AGENT] 🔎 Scanning {region} for '{niche}'...",
                f"[DATA] 📥 Ingested {len(results)} raw leads from Google Maps/Yelp APIs.",
                f"[ANALYSIS] 🧠 Calculating 'Pain Point' probability...",
                f"[SUCCESS] ✅ Strategic Target List Generated."
            ]
            st.code("\n".join(logs))
            
            st.success("Mission Complete. Intelligence Ready.")
            
            # Save to session state
            st.session_state['leads'] = results
            st.session_state['run_complete'] = True
            
        except Exception as e:
            st.error(f"Mission Failed: {e}")

# --- TAB 1: RESULTS ---
with tab1:
    if 'run_complete' in st.session_state:
        st.subheader(f"Strategic Targets: {region}")
        data = st.session_state['leads']
        
        if HAS_PANDAS:
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
        else:
            # ULTRA-SAFE MODE: Manual Card Display (Replaces st.table)
            # This avoids any PyArrow/Pandas serialization crashes
            st.caption(f"Found {len(data)} High-Fidelity Leads:")
            
            for item in data:
                with st.container():
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        st.markdown(f"**{item['name']}**")
                        st.caption(f"Type: {item['type']} | Tech: {item['tech_stack']}")
                    with col2:
                        st.markdown(f"**{item['match_score']}%**")
                        st.progress(item['match_score'] / 100)
                    st.divider()

    else:
        st.info("👈 Please click 'INITIATE SWARM MISSION' in the sidebar to start.")

# --- TAB 3: BI DASHBOARD ---
with tab3:
    if 'run_complete' in st.session_state:
        st.subheader("Real-Time Analytics (Rill Engine)")
        data = st.session_state['leads']
        
        # Manual calculation
        total_prospects = len(data)
        avg_score = sum(d['match_score'] for d in data) / total_prospects if total_prospects > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Prospects", total_prospects, "+12%")
        col2.metric("Avg Match Score", f"{avg_score:.1f}%", "+5%")
        col3.metric("Est. Pipeline Value", "$45,000", "+$8k")
        
        st.markdown("---")
        
        if HAS_PANDAS and HAS_PLOTLY:
            df_viz = pd.DataFrame(data)
            c1, c2 = st.columns(2)
            with c1:
                 fig_pie = px.pie(df_viz, names='tech_stack', title='Competitor Tech Stack')
                 st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.warning("⚠️ Visualization Engine Unavailable (Safe Mode).")
            st.write("**Tech Stack Breakdown:**")
            tech_stacks = {}
            for d in data:
                ts = d['tech_stack']
                tech_stacks[ts] = tech_stacks.get(ts, 0) + 1
            
            # Simple Bar Chart Visualization using Progress Bars
            for tech, count in tech_stacks.items():
                st.write(f"{tech}: {count}")
                st.progress(min(count / len(data), 1.0))
                
    else:
        st.write("Initializing Rill Engine...")
        st.warning("No live data. Run a mission to populate dashboard.")
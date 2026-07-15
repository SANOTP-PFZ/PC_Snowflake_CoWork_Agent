import streamlit as st

from components.header import render_header
from screens import landing, ta_grid, tad_grid, agent_detail

st.set_page_config(
    page_title="Cortex Agent Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS
st.markdown(
    """
    <style>
    /* ===== Global palette ===== */
    :root {
        --surface-0: #f0efe9;
        --surface-1: #f6f5f0;
        --surface-2: #f0efe9;
        --text-primary: #1b1b19;
        --text-secondary: #5f5e5a;
        --text-muted: #8a8982;
        --border: rgba(0,0,0,0.10);
        --border-strong: rgba(0,0,0,0.20);
        --accent-bg: #e6f1fb;
        --accent-text: #185fa5;
        --teal-bg: #e1f5ee;
        --teal-text: #0f6e56;
        --success-bg: #eaf3de;
        --success-text: #3b6d11;
        --danger-bg: #fcebeb;
        --danger-text: #a32d2d;
    }

    /* Hide default Streamlit elements for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Force consistent app background */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: var(--surface-0) !important;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 1rem;
        background-color: var(--surface-0) !important;
    }

    /* Make all Streamlit containers/cards match palette */
    [data-testid="stVerticalBlock"],
    [data-testid="stHorizontalBlock"] {
        background-color: transparent !important;
    }

    /* Bordered containers (st.container(border=True)) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: var(--surface-1) !important;
        border: 2px solid #c5c4bf !important;
        border-radius: 12px !important;
    }

    /* Buttons */
    .stButton > button,
    .stLinkButton > a {
        background-color: var(--surface-1) !important;
        border: 1px solid var(--border-strong) !important;
        border-radius: 999px !important;
        color: var(--text-primary) !important;
        padding: 3px 12px !important;
        font-size: 12px !important;
        min-height: unset !important;
        line-height: 1.4 !important;
    }
    .stButton > button:hover,
    .stLinkButton > a:hover {
        background-color: var(--surface-0) !important;
        border-color: var(--accent-text) !important;
        color: var(--accent-text) !important;
    }
    .stLinkButton > a:visited,
    .stLinkButton > a:active {
        color: var(--text-primary) !important;
    }
    /* Active/primary filter chip button */
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"] {
        background-color: #eaf3de !important;
        color: #3b6d11 !important;
        border-color: #3b6d11 !important;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background-color: var(--surface-1);
        border-radius: 8px;
        padding: 14px 16px;
    }

    /* Pills / filter chips - st.pills */
    [data-testid="stPills"] button {
        border-radius: 999px !important;
        background-color: #f6f5f0 !important;
        color: #1b1b19 !important;
        border: 1.5px solid rgba(0,0,0,0.20) !important;
    }
    [data-testid="stPills"] button:hover {
        background-color: #e6f1fb !important;
        color: #185fa5 !important;
        border-color: #185fa5 !important;
    }
    [data-testid="stPills"] button[aria-checked="true"],
    [data-testid="stPills"] button[data-selected="true"],
    [data-testid="stPills"] button[aria-pressed="true"] {
        background-color: #eaf3de !important;
        color: #3b6d11 !important;
        border-color: #3b6d11 !important;
    }
    [data-testid="stPills"] button span,
    [data-testid="stPills"] button p,
    [data-testid="stPills"] button div {
        color: inherit !important;
    }


    /* Header bar */
    .hub-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 28px;
        border: 1px solid var(--border);
        border-radius: 14px;
        background: var(--surface-1);
        margin-bottom: 28px;
        margin-left: -2rem;
        margin-right: -2rem;
    }
    .hub-header-left {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    .hub-logo {
        width: 44px;
        height: 44px;
        border-radius: 11px;
        background: var(--accent-bg);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 22px;
    }
    .hub-title {
        font-weight: 700;
        font-size: 20px;
        color: var(--text-primary);
        letter-spacing: -0.3px;
    }
    .hub-subtitle {
        font-size: 13px;
        color: var(--text-muted);
        margin-top: 2px;
    }

    /* Chips */
    .chip {
        font-size: 12px;
        padding: 4px 11px;
        border-radius: 999px;
        display: inline-flex;
        align-items: center;
        gap: 5px;
        font-weight: 500;
    }
    .chip-blue { background: var(--accent-bg); color: var(--accent-text); }
    .chip-teal { background: var(--teal-bg); color: var(--teal-text); }
    .chip-green { background: var(--success-bg); color: var(--success-text); }
    .chip-red { background: var(--danger-bg); color: var(--danger-text); }

    /* Agent cards */
    .agent-card {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .ta-agent-card {
        background: var(--surface-1);
        border: 1.5px solid var(--border-strong);
        border-radius: 16px;
        padding: 28px 24px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        gap: 14px;
        min-height: 140px;
        transition: border-color 0.2s, box-shadow 0.2s, transform 0.15s;
    }
    .ta-agent-card:hover {
        border-color: var(--accent-text);
        box-shadow: 0 4px 16px rgba(24, 95, 165, 0.12);
        transform: translateY(-2px);
    }
    .ta-card-link {
        text-decoration: none;
        display: block;
    }
    .ta-agent-name {
        font-size: 16px;
        font-weight: 600;
        color: var(--text-primary);
    }
    .ta-launch-text {
        font-size: 12px;
        font-weight: 500;
        color: var(--accent-text);
        background: var(--accent-bg);
        padding: 5px 14px;
        border-radius: 999px;
    }
    .ta-agent-card-highlight {
        border-color: var(--accent-text) !important;
        box-shadow: 0 4px 16px rgba(24, 95, 165, 0.12);
    }
    .tad-filter-active .ta-agent-card:not(.ta-agent-card-highlight) {
        opacity: 0.4;
    }
    .agent-card-header {
        display: flex;
        align-items: center;
        gap: 11px;
    }
    .agent-icon {
        width: 36px;
        height: 36px;
        border-radius: 9px;
        background: var(--accent-bg);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 18px;
    }
    .agent-name {
        font-weight: 600;
        font-size: 14px;
        color: var(--text-primary);
    }
    .agent-chips {
        display: flex;
        gap: 6px;
        flex-wrap: wrap;
    }

    /* Brand cards */
    .brand-card {
        margin-bottom: -10px;
    }
    .brand-name {
        font-weight: 600;
        font-size: 13px;
        color: var(--text-primary);
    }
    .brand-category {
        font-size: 11px;
        color: var(--text-muted);
    }

    /* Stat tiles */
    .stat-tile {
        background: var(--surface-1);
        border-radius: 8px;
        padding: 14px 16px;
    }
    .stat-label {
        font-size: 13px;
        color: var(--text-secondary);
    }
    .stat-value {
        font-size: 26px;
        font-weight: 600;
        color: var(--text-primary);
    }

    /* Chat */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 12px;
        min-height: 200px;
        margin-bottom: 16px;
    }
    .chat-bubble {
        border-radius: 12px;
        padding: 11px 15px;
        font-size: 14px;
        max-width: 78%;
    }
    .chat-bot {
        align-self: flex-start;
        background: var(--surface-1);
        color: var(--text-secondary);
    }
    .chat-user {
        align-self: flex-end;
        background: var(--accent-bg);
        color: var(--accent-text);
    }
    .chat-ref {
        color: var(--accent-text);
    }

    /* Streamlit text colors for consistency */
    .stMarkdown, .stText, p, h1, h2, h3, h4 {
        color: var(--text-primary) !important;
    }
    .stCaption, [data-testid="stCaptionContainer"] {
        color: var(--text-muted) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state
if "screen" not in st.session_state:
    st.session_state["screen"] = "landing"

# Render header
render_header()

# Route to the active screen
screen = st.session_state["screen"]

if screen == "landing":
    landing.render()
elif screen == "ta":
    ta_grid.render()
elif screen == "tad":
    tad_grid.render()
elif screen == "agent":
    agent_detail.render()

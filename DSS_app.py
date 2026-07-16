import streamlit as st

from components.header import render_header
from screens import landing, ta_grid, tad_grid, agent_detail

st.set_page_config(
    page_title="Cortex Agent Hub",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS
st.markdown(
    """
    <style>
    /* ===== Clean & Minimal — Pfizer palette ===== */
    :root {
        --bg: #f0f6fc;
        --surface: #ffffff;
        --text-1: #002F6C;
        --text-2: #1a5296;
        --text-3: #5a8abf;
        --border: rgba(0, 47, 108, 0.06);
        --border-hover: rgba(0, 147, 208, 0.4);
        --accent: #0093D0;
        --accent-soft: #eaf6fd;
        --shadow-sm: 0 1px 3px rgba(0, 47, 108, 0.04);
        --shadow-md: 0 4px 16px rgba(0, 47, 108, 0.06);
        --shadow-lg: 0 12px 40px rgba(0, 47, 108, 0.1);
        --radius: 12px;
        --radius-lg: 16px;
    }

    * { transition: all 0.15s ease; }

    /* Hide Streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }

    /* App background */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: var(--bg) !important;
    }
    .block-container {
        max-width: 100%;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
        padding-left: 3rem;
        padding-right: 3rem;
        background-color: var(--bg) !important;
    }

    /* Transparent layout blocks */
    [data-testid="stVerticalBlock"],
    [data-testid="stHorizontalBlock"] {
        background-color: transparent !important;
    }

    /* Bordered containers */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-lg) !important;
        box-shadow: var(--shadow-sm) !important;
    }
    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        box-shadow: var(--shadow-md) !important;
    }

    /* ===== Buttons ===== */
    .stButton > button,
    .stLinkButton > a {
        background: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: 999px !important;
        color: var(--text-2) !important;
        padding: 6px 16px !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        min-height: unset !important;
        line-height: 1.5 !important;
        box-shadow: var(--shadow-sm) !important;
        white-space: nowrap !important;
    }
    .stButton > button:hover,
    .stLinkButton > a:hover {
        background: var(--accent-soft) !important;
        border-color: var(--border-hover) !important;
        color: var(--accent) !important;
        box-shadow: var(--shadow-md) !important;
        transform: translateY(-1px);
    }
    .stLinkButton > a:visited,
    .stLinkButton > a:active {
        color: var(--text-2) !important;
    }

    /* Active filter button */
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"] {
        background: var(--accent-soft) !important;
        color: var(--accent) !important;
        border-color: rgba(0, 147, 208, 0.3) !important;
        box-shadow: none !important;
    }

    /* Hidden nav buttons (for category card navigation) */
    .nav-btn-hidden .stButton {
        height: 0;
        overflow: hidden;
        margin: 0;
        padding: 0;
    }

    /* Category cards — equal height, hide the navigation button below */
    .category-card {
        min-height: 200px;
        cursor: pointer;
    }
    /* Target the stElementContainer that contains the button AFTER a category card */
    [data-testid="stVerticalBlock"]:has(.category-card) > [data-testid="stElementContainer"]:has(.stButton) {
        height: 0 !important;
        overflow: hidden !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Metrics */
    [data-testid="stMetric"] {
        background-color: var(--surface);
        border-radius: var(--radius);
        padding: 16px;
        box-shadow: var(--shadow-sm);
    }

    /* Pills */
    [data-testid="stPills"] button {
        border-radius: 8px !important;
        background-color: var(--surface) !important;
        color: var(--text-2) !important;
        border: 1px solid var(--border) !important;
        box-shadow: var(--shadow-sm) !important;
    }
    [data-testid="stPills"] button:hover {
        background-color: var(--accent-soft) !important;
        color: var(--accent) !important;
        border-color: var(--border-hover) !important;
    }
    [data-testid="stPills"] button[aria-checked="true"],
    [data-testid="stPills"] button[data-selected="true"],
    [data-testid="stPills"] button[aria-pressed="true"] {
        background-color: var(--accent) !important;
        color: #ffffff !important;
        border-color: var(--accent) !important;
    }
    [data-testid="stPills"] button span,
    [data-testid="stPills"] button p,
    [data-testid="stPills"] button div {
        color: inherit !important;
    }

    /* ===== Header ===== */
    .hub-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px 24px;
        border-radius: var(--radius-lg);
        background: var(--surface);
        margin-bottom: 32px;
        margin-left: -2rem;
        margin-right: -2rem;
        box-shadow: var(--shadow-sm);
        border: 1px solid var(--border);
    }
    .hub-header-left {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .hub-logo {
        display: flex;
        align-items: center;
    }
    .hub-title {
        font-weight: 600;
        font-size: 17px;
        color: var(--text-1);
        letter-spacing: -0.3px;
    }

    /* ===== Chips ===== */
    .chip {
        font-size: 11px;
        padding: 3px 10px;
        border-radius: 6px;
        display: inline-flex;
        align-items: center;
        gap: 4px;
        font-weight: 500;
    }
    .chip-blue { background: var(--accent-soft); color: var(--accent); }
    .chip-teal { background: var(--accent-soft); color: var(--text-1); }
    .chip-green { background: #edf9f0; color: #1a8a4a; }
    .chip-red { background: #fdf0f0; color: #c53030; }

    /* ===== Agent Cards (wireframe style) ===== */
    .ta-agent-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 22px 24px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        min-height: 160px;
        box-shadow: var(--shadow-sm);
        transition: all 0.2s ease;
        text-align: left;
    }
    .ta-agent-card:hover {
        border-color: var(--border-hover);
        box-shadow: var(--shadow-lg);
        transform: translateY(-2px);
    }
    .ta-card-link {
        text-decoration: none !important;
        display: block;
    }
    .ta-card-link:hover {
        text-decoration: none !important;
    }
    .ta-card-icon {
        width: 36px;
        height: 36px;
        border-radius: 10px;
        background: var(--accent-soft);
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .ta-card-icon svg {
        width: 18px;
        height: 18px;
        stroke: var(--accent);
    }
    .ta-card-title {
        font-size: 15px;
        font-weight: 600;
        color: var(--text-2);
        line-height: 1.3;
        margin-top: 4px;
    }
    .ta-card-desc {
        font-size: 13px;
        color: var(--text-3);
        line-height: 1.4;
        flex-grow: 1;
    }
    .ta-card-chip {
        font-size: 11px;
        color: var(--text-3);
        display: flex;
        align-items: center;
        gap: 6px;
        margin-top: auto;
    }
    .ta-card-chip::before {
        content: "";
        width: 8px;
        height: 8px;
        border-radius: 2px;
        background: var(--accent);
        display: inline-block;
    }
    .ta-agent-card-highlight {
        border-color: var(--accent) !important;
        background: var(--accent-soft) !important;
        box-shadow: 0 8px 24px rgba(0, 147, 208, 0.15) !important;
        transform: translateY(-2px);
    }

    .agent-card-header {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .agent-icon {
        width: 32px;
        height: 32px;
        border-radius: 8px;
        background: var(--accent-soft);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
    }
    .agent-name {
        font-weight: 600;
        font-size: 13px;
        color: var(--text-1);
    }
    .agent-chips {
        display: flex;
        gap: 6px;
        flex-wrap: wrap;
    }

    /* ===== Brand trend cards ===== */
    .brand-trend-box {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 16px 14px;
        display: flex;
        flex-direction: column;
        gap: 6px;
        box-shadow: var(--shadow-sm);
        transition: all 0.2s ease;
    }
    .brand-trend-box:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }
    .brand-card {
        margin-bottom: 0;
    }
    .brand-name {
        font-weight: 600;
        font-size: 13px;
        color: var(--text-1);
    }
    .brand-category {
        font-size: 11px;
        color: var(--text-3);
    }

    /* ===== Streamlit overrides ===== */
    .stMarkdown, .stText, p, h1, h2, h3, h4 {
        color: var(--text-1) !important;
    }
    h1 { font-weight: 700 !important; letter-spacing: -0.5px !important; }
    h2 { font-weight: 600 !important; letter-spacing: -0.3px !important; }
    .stCaption, [data-testid="stCaptionContainer"] {
        color: var(--text-3) !important;
    }
    .stDivider { opacity: 0.4 !important; }

    /* Warning banner */
    [data-testid="stAlert"] {
        border-radius: var(--radius) !important;
        border: 1px solid var(--border) !important;
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

# Footer (fixed to bottom)
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        text-align: center;
        color: #8a9ab5;
        font-size: 11px;
        font-weight: 400;
        padding: 8px 0;
        background: rgba(240, 246, 252, 0.9);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-top: 1px solid rgba(0, 47, 108, 0.04);
        z-index: 999;
    }
    </style>
    <div class="footer">Developed by ZS Primary Care Team</div>
    """,
    unsafe_allow_html=True,
)

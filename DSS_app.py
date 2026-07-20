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
    /* ===== Migraine Hub Inspired — Navy palette ===== */
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');

    :root {
        --bg: #EEF3FB;
        --bg-2: #E3EBF7;
        --surface: #FFFFFF;
        --surface-2: #F8FAFD;
        --text-1: #0F172A;
        --text-2: #1C4FC0;
        --text-3: #64748B;
        --text-soft: #475569;
        --border: rgba(15, 23, 42, 0.08);
        --border-hover: rgba(28, 79, 192, 0.35);
        --accent: #41B6E6;
        --accent-soft: rgba(65, 182, 230, 0.10);
        --navy-700: #163990;
        --navy-800: #102A5C;
        --navy-900: #0A1A3D;
        --shadow-xs: 0 1px 2px rgba(15, 23, 42, 0.04);
        --shadow-sm: 0 2px 8px rgba(15, 23, 42, 0.05), 0 1px 2px rgba(15, 23, 42, 0.04);
        --shadow-md: 0 6px 16px rgba(15, 23, 42, 0.07), 0 2px 4px rgba(15, 23, 42, 0.04);
        --shadow-lg: 0 18px 40px rgba(15, 23, 42, 0.10), 0 6px 12px rgba(15, 23, 42, 0.06);
        --shadow-panel: 0 8px 24px rgba(15, 23, 42, 0.07), 0 2px 6px rgba(15, 23, 42, 0.04);
        --radius: 14px;
        --radius-lg: 18px;
        --ease: cubic-bezier(0.4, 0, 0.2, 1);
        --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }
    body, .stApp { font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif; -webkit-font-smoothing: antialiased; }
    h1, h2, h3, h4 { font-family: 'Manrope', 'Inter', system-ui, sans-serif; letter-spacing: -0.015em; }

    /* Hide Streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }

    /* App background — layered radial gradients */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background:
            radial-gradient(ellipse 80% 60% at 0% 0%, rgba(28,79,192,0.06) 0%, transparent 60%),
            radial-gradient(ellipse 70% 50% at 100% 0%, rgba(65,182,230,0.05) 0%, transparent 55%),
            radial-gradient(ellipse 60% 50% at 50% 100%, rgba(124,58,237,0.03) 0%, transparent 60%),
            var(--bg) !important;
    }
    .block-container {
        max-width: 100%;
        padding-top: 1rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        background: transparent !important;
    }

    /* No-scroll mode for landing and TA pages */
    .stApp:has(.no-scroll-marker) [data-testid="stMain"] {
        overflow: hidden !important;
    }
    .stApp:has(.no-scroll-marker) [data-testid="stMainBlockContainer"] {
        overflow: hidden !important;
        max-height: 100vh !important;
    }
    .stApp:has(.no-scroll-marker) .block-container {
        overflow: hidden !important;
        padding-bottom: 0 !important;
    }

    /* Transparent layout blocks */
    [data-testid="stVerticalBlock"],
    [data-testid="stHorizontalBlock"] {
        background-color: transparent !important;
    }

    /* Bordered containers — glassmorphism */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.55) !important;
        backdrop-filter: saturate(180%) blur(14px) !important;
        -webkit-backdrop-filter: saturate(180%) blur(14px) !important;
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
        background: rgba(255, 255, 255, 0.7) !important;
        border: 1px solid var(--border) !important;
        border-radius: 999px !important;
        color: var(--text-soft) !important;
        padding: 6px 16px !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        min-height: unset !important;
        line-height: 1.5 !important;
        box-shadow: var(--shadow-xs) !important;
        white-space: nowrap !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.18s var(--ease) !important;
    }
    .stButton > button:hover,
    .stLinkButton > a:hover {
        background: #fff !important;
        border-color: var(--border-hover) !important;
        color: var(--navy-700) !important;
        box-shadow: var(--shadow-sm) !important;
        transform: translateY(-1px);
    }
    .stLinkButton > a:visited,
    .stLinkButton > a:active {
        color: var(--text-2) !important;
    }

    /* Active filter button */
    .stButton > button[kind="primary"],
    .stButton > button[data-testid="stBaseButton-primary"] {
        background: rgba(28, 79, 192, 0.10) !important;
        color: var(--navy-700) !important;
        border-color: rgba(28, 79, 192, 0.25) !important;
        box-shadow: none !important;
    }

    /* Hidden nav buttons (for category card navigation) */
    .nav-btn-hidden .stButton {
        height: 0;
        overflow: hidden;
        margin: 0;
        padding: 0;
    }

    /* Category cards — equal height + hover pop effect */
    .category-card {
        min-height: 160px;
        height: 160px;
        cursor: pointer;
        transition: transform 0.28s var(--ease-out), box-shadow 0.28s var(--ease), border-color 0.18s var(--ease);
    }
    .category-card:hover {
        transform: translateY(-4px) scale(1.02);
        box-shadow: var(--shadow-lg);
        border-color: var(--border-hover);
    }
    /* Invisible button overlay for seamless navigation */
    [data-testid="stColumn"]:has(.category-card) > [data-testid="stVerticalBlock"] > [data-testid="stElementContainer"]:has(.stButton) {
        margin-top: -168px !important;
        position: relative;
        z-index: 10;
        pointer-events: none;
    }
    [data-testid="stColumn"]:has(.category-card) .stButton > button {
        height: 168px !important;
        opacity: 0 !important;
        cursor: pointer !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 !important;
        border-radius: var(--radius) !important;
        pointer-events: auto;
    }
    /* Pop effect scoped to individual column hover */
    [data-testid="stColumn"]:has(.category-card):hover .category-card {
        transform: translateY(-4px) scale(1.02);
        box-shadow: var(--shadow-lg);
        border-color: var(--border-hover);
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
        background: rgba(255, 255, 255, 0.7) !important;
        color: var(--text-soft) !important;
        border: 1px solid var(--border) !important;
        box-shadow: var(--shadow-xs) !important;
        transition: all 0.18s var(--ease) !important;
    }
    [data-testid="stPills"] button:hover {
        background: #fff !important;
        color: var(--navy-700) !important;
        border-color: var(--border-hover) !important;
    }
    [data-testid="stPills"] button[aria-checked="true"],
    [data-testid="stPills"] button[data-selected="true"],
    [data-testid="stPills"] button[aria-pressed="true"] {
        background: linear-gradient(90deg, var(--navy-700), var(--accent)) !important;
        color: #ffffff !important;
        border-color: transparent !important;
        box-shadow: 0 2px 8px rgba(22, 57, 144, 0.25) !important;
    }
    [data-testid="stPills"] button span,
    [data-testid="stPills"] button p,
    [data-testid="stPills"] button div {
        color: inherit !important;
    }

    /* ===== Header — Glassmorphism ===== */
    .hub-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 24px;
        border-radius: var(--radius-lg);
        background: rgba(255, 255, 255, 0.62);
        backdrop-filter: saturate(180%) blur(22px);
        -webkit-backdrop-filter: saturate(180%) blur(22px);
        margin-bottom: 16px;
        margin-left: -2rem;
        margin-right: -2rem;
        box-shadow: var(--shadow-panel);
        border: 1px solid var(--border);
    }
    .hub-header-left {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .hub-title {
        font-family: 'Manrope', sans-serif;
        font-weight: 800;
        font-size: 22px;
        color: var(--navy-900);
        letter-spacing: -0.025em;
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

    /* ===== Agent Cards — Hub style ===== */
    .ta-agent-card {
        position: relative;
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 18px 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 8px;
        min-height: 150px;
        height: 150px;
        box-shadow: var(--shadow-sm);
        transition: transform 0.28s var(--ease-out), box-shadow 0.28s var(--ease);
        text-align: center;
        overflow: hidden;
        cursor: pointer;
    }
    .ta-agent-card::after {
        content: '';
        position: absolute;
        inset: 0;
        border-radius: inherit;
        background: linear-gradient(135deg, rgba(255,255,255,0) 55%, rgba(65,182,230,0.05) 80%, rgba(28,79,192,0.07) 100%);
        opacity: 0;
        transition: opacity 0.28s var(--ease);
        pointer-events: none;
    }
    .ta-agent-card:hover {
        transform: translateY(-3px);
        box-shadow: var(--shadow-lg);
        border-color: var(--border-hover);
    }
    .ta-agent-card:hover::after {
        opacity: 1;
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
        font-family: 'Manrope', sans-serif;
        font-size: 15px;
        font-weight: 700;
        color: var(--navy-900);
        line-height: 1.25;
        margin-top: 4px;
        text-align: center;
    }
    .ta-card-desc {
        font-size: 0.8rem;
        color: var(--text-3);
        line-height: 1.5;
        text-align: center;
    }
    .ta-card-chip {
        font-size: 11px;
        color: var(--text-3);
        display: flex;
        align-items: center;
        justify-content: center;
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
        border-color: var(--navy-700) !important;
        background: rgba(28, 79, 192, 0.06) !important;
        box-shadow: 0 8px 24px rgba(22, 57, 144, 0.15) !important;
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

    /* ===== Brand trend cards — glassmorphism ===== */
    .brand-trend-box {
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid var(--border);
        border-radius: var(--radius);
        padding: 12px 12px;
        display: flex;
        flex-direction: column;
        gap: 4px;
        box-shadow: var(--shadow-sm);
        transition: transform 0.25s var(--ease-out), box-shadow 0.25s var(--ease);
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
    h1 { font-family: 'Manrope', sans-serif !important; font-weight: 800 !important; letter-spacing: -0.025em !important; color: var(--navy-900) !important; }
    h2 { font-family: 'Manrope', sans-serif !important; font-weight: 700 !important; letter-spacing: -0.02em !important; color: var(--navy-900) !important; }
    .stCaption, [data-testid="stCaptionContainer"] {
        color: var(--text-3) !important;
    }
    .stDivider { opacity: 0.3 !important; }

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

# Handle query param navigation (from category card onclick)
params = st.query_params
if "screen" in params:
    st.session_state["screen"] = params["screen"]
    st.query_params.clear()

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

# Disable scrolling on landing and TA pages
if screen in ("landing", "ta"):
    st.markdown('<div class="no-scroll-marker" style="display:none"></div>', unsafe_allow_html=True)

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
        color: var(--text-3);
        font-size: 11px;
        font-weight: 500;
        padding: 8px 0;
        background: rgba(238, 243, 251, 0.85);
        backdrop-filter: saturate(180%) blur(16px);
        -webkit-backdrop-filter: saturate(180%) blur(16px);
        border-top: 1px solid var(--border);
        z-index: 999;
    }
    </style>
    <div class="footer">Developed by ZS Primary Care Team</div>
    """,
    unsafe_allow_html=True,
)

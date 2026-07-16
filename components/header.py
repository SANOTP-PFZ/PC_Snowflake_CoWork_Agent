import streamlit as st
import base64
from pathlib import Path


def render_header():
    logo_path = Path(__file__).parent.parent / "logo.png"
    try:
        logo_b64 = base64.b64encode(logo_path.read_bytes()).decode()
        logo_html = f'<img src="data:image/png;base64,{logo_b64}" height="36" style="object-fit:contain"/>'
    except Exception:
        logo_html = ""

    show_home = st.session_state.get("screen", "landing") != "landing"

    home_html = ""
    if show_home:
        home_html = """
        <div class="hub-home-link">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                <polyline points="9 22 9 12 15 12 15 22"/>
            </svg>
            <span>Home</span>
        </div>
        """

    st.markdown(
        f"""
        <div class="hub-header">
            <div class="hub-header-left">
                {logo_html}
                <div>
                    <div class="hub-title">Cortex Agent Hub</div>
                </div>
            </div>
            {home_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

    if show_home:
        if st.button("⌂", key="header_home"):
            st.session_state["screen"] = "landing"
            st.rerun()

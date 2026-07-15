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

    st.markdown(
        f"""
        <div class="hub-header">
            <div class="hub-header-left">
                {logo_html}
                <div>
                    <div class="hub-title">Cortex Agent Hub</div>
                    <div class="hub-subtitle">Pfizer CoWork · unified agent workspace</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

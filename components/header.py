import streamlit as st
import base64
import os


def render_header():
    logo_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logo.png")
    with open(logo_path, "rb") as f:
        logo_b64 = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <div class="hub-header">
            <div class="hub-header-left">
                <div class="hub-logo">
                    <img src="data:image/png;base64,{logo_b64}" width="34" height="34" style="border-radius:8px"/>
                </div>
                <div>
                    <div class="hub-title">Cortex Agent Hub</div>
                    <div class="hub-subtitle">Pfizer CoWork · unified agent workspace</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

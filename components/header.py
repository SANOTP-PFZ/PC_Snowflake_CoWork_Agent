import streamlit as st


def render_header():
    st.markdown(
        """
        <div class="hub-header">
            <div class="hub-header-left">
                <div class="hub-logo">❄️</div>
                <div>
                    <div class="hub-title">Cortex Agent Hub</div>
                    <div class="hub-subtitle">Snowflake CoCo · unified agent workspace</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

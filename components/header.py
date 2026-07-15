import streamlit as st


def render_header():
    st.markdown(
        """
        <div class="hub-header">
            <div class="hub-header-left">
                <div class="hub-logo">
                    <svg width="28" height="28" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <circle cx="16" cy="16" r="15" fill="#0093D0"/>
                        <path d="M8 12h3v8H8v-8zm4.5-2h3v12h-3V10zm4.5 4h3v6h-3v-6zm4.5-1h3v8h-3v-8z" fill="white"/>
                    </svg>
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

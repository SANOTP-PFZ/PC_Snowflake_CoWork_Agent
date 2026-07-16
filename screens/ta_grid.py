import streamlit as st

from data.agents import TA_AGENTS
from components.cards import render_agent_card


def render():
    col1, col2 = st.columns([1, 9])
    with col1:
        if st.button("Home", key="ta_home"):
            st.session_state["screen"] = "landing"
            st.rerun()
    with col2:
        st.markdown("<span style='color:var(--text-3);font-size:14px;line-height:2.4'>/ Therapy Area</span>", unsafe_allow_html=True)
    st.markdown("## Therapy Area")
    st.markdown(
        "<p style='color:#1a5296;font-size:14px;margin-top:-8px'>Ask technical and business questions across all available data sources for your therapy area — powered by Cortex AI.</p>",
        unsafe_allow_html=True,
    )

    # AI disclaimer
    st.warning(
        "Answers from these agents are produced by AI and may be incomplete or inaccurate. "
        "For complex or business-critical outputs, please verify with the relevant ZS team to validate the underlying logic and code before making decisions.",
        icon="⚠️",
    )

    # Agent grid
    rows = [TA_AGENTS[i : i + 3] for i in range(0, len(TA_AGENTS), 3)]
    for row in rows:
        cols = st.columns(3)
        for i, agent in enumerate(row):
            with cols[i]:
                render_agent_card(agent, "ta")
        st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)



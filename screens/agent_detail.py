import streamlit as st

from components.chat import render_chat_panel


def render():
    agent = st.session_state.get("current_agent", {"name": "Agent", "brand": "—"})
    category = st.session_state.get("agent_category", "ta")
    cat_label = "Therapy area agents" if category == "ta" else "TA + data source agents"

    # Breadcrumb with back navigation
    cols = st.columns([6, 1])
    with cols[1]:
        if st.button("← Back", key="agent_back"):
            st.session_state["screen"] = category
            st.rerun()

    st.markdown(f"**Home** / {cat_label} / {agent['name']}")

    # Two-column layout: sidebar + chat
    sidebar_col, chat_col = st.columns([1, 3])

    with sidebar_col:
        with st.container(border=True):
            st.markdown("🤖")
            st.markdown(f"### {agent['name']}")
            st.markdown('<span class="chip chip-green">● Active</span>', unsafe_allow_html=True)
            st.markdown("---")
            st.markdown(f"""
**Model:** Cortex LLM  
**Tools:** Search, SQL  
**Owner:** Data Science  
**Updated:** 2 days ago
""")
            st.markdown("---")
            st.caption("Answers questions grounded in the connected therapy-area knowledge base.")

    with chat_col:
        with st.container(border=True):
            render_chat_panel(agent["name"])

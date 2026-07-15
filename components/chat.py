import streamlit as st


def render_chat_panel(agent_name: str):
    st.markdown(
        """
        <div class="chat-container">
            <div class="chat-bubble chat-bot">How can I help you today?</div>
            <div class="chat-bubble chat-user">Summarize the latest trial outcomes for this therapy area.</div>
            <div class="chat-bubble chat-bot">Here is a summary based on the connected source… <span class="chat-ref">[1] [2]</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(2)
    with cols[0]:
        st.button("💡 Efficacy endpoints", key="suggest_1", use_container_width=True)
    with cols[1]:
        st.button("💡 Safety profile", key="suggest_2", use_container_width=True)

    user_input = st.chat_input(f"Ask {agent_name} a question")
    if user_input:
        st.info(f"You asked: {user_input}\n\n*(Agent response would appear here when connected to a live Cortex agent)*")

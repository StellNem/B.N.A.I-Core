import streamlit as st
from core_engine import run_agent_loop

st.set_page_config(
    page_title="B.N.A.I Lite Core",
    page_icon="📡",
    layout="centered"
)

st.title("📡 B.N.A.I Lite Core")
st.caption("Free Local AI Boilerplate Template | Upgrade to Pro on Gumroad")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message["role"] == "system":
        continue
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_prompt := st.chat_input("Communicate with B.N.A.I Lite..."):
    with st.chat_message("user"):
        st.write(user_prompt)
        
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    
    with st.chat_message("assistant"):
        status_box = st.status("Engaging local core...", expanded=True)
        
        try:
            answer = run_agent_loop(st.session_state.messages, status_box.write)
            status_box.update(state="complete", label="Finished!")
            st.write(answer)
        except Exception as e:
            status_box.update(state="error", label="Connection Intercepted")
            st.error(f"Error: {str(e)}")
            st.info("Make sure Ollama is running (`ollama serve`) and your model is downloaded locally.")
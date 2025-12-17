import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from langchain_core.callbacks.base import BaseCallbackHandler
from helper import get_model_list

# -------------------------------------------------
# Custom StreamHandler class
# -------------------------------------------------
class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text
    def on_llm_start(self, serialized, prompts, *, run_id, parent_run_id = None, tags = None, metadata = None, **kwargs):
        with self.container:
            st.write("generating response....")
        return super().on_llm_start(serialized, prompts, run_id=run_id, parent_run_id=parent_run_id, tags=tags, metadata=metadata, **kwargs)
    
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)
# -------------------------------------------------
# LLM setup
# -------------------------------------------------
try:
    if len(get_model_list()) <= 0:
        st.error("please pull a model first. e.g, ollama pull gemma3:1b")
    MODEL = st.sidebar.selectbox(
        "Select any model",
        options=get_model_list(),
        placeholder="select model"
    )
    # st.success("LLM instantiated successfully!")
except Exception as err:   # catch any exception that occurs during initialization
    st.error(f"Error: {err}")

# -------------------------------------------------
# Session state – keep the conversation history
# -------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# -------------------------------------------------
# UI – render the existing chat history
# -------------------------------------------------
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("human"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("ai"):
            st.markdown(msg.content)


# -------------------------------------------------
# Chat - get user prompt and display response
# -------------------------------------------------

if prompt := st.chat_input():
    st.session_state.messages.append(HumanMessage(prompt))
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        llm = ChatOllama(model=MODEL, streaming=True, callbacks=[stream_handler])
        response = llm.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(response.content))
import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama


MODEL="gemma3:1b"
# -------------------------------------------------
# LLM setup
# -------------------------------------------------
try:
    llm = ChatOllama(
        model=MODEL,
        temperature=0.8,
        # You can add other optional arguments here, such as:
        # max_tokens=512,
        # top_p=0.9,
        # streaming=True,
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
# Input box
# -------------------------------------------------
prompt = st.chat_input("Ask any question")

if prompt:
    # Show the user’s message immediately
    with st.chat_message("human"):
        st.markdown(prompt)

    # Add the human message to the history
    st.session_state.messages.append(HumanMessage(prompt))

    # -------------------------------------------------
    # Stream the LLM response
    # -------------------------------------------------
    # Create a placeholder that we’ll update with each new chunk
    with st.chat_message("ai"):
        response_placeholder = st.empty()
        full_msg = ""
        try:
            # `llm.stream()` yields partial `AIMessage` objects (or just the text)
            for chunk in llm.stream(st.session_state.messages):
                # Some adapters return a Message object; others just the text.
                # Guard against both possibilities.
                chunk_text = getattr(chunk, "content", str(chunk))
                full_msg += chunk_text
                response_placeholder.markdown(full_msg)
        except Exception as err:   # catch any exception that occurs during initialization
            st.error(f"Error: {err}")


    # Store the completed AI message in the session state
    st.session_state.messages.append(AIMessage(full_msg))
import streamlit as st

from graph.graph_builder import IntelliAgentGraph


st.set_page_config(
    page_title="IntelliAgent",
    layout="wide"
)

st.title("IntelliAgent")

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

query = st.chat_input(
    "Ask your question"
)
print(st.session_state)

if "graph" not in st.session_state:

    st.session_state.graph = IntelliAgentGraph().compile()

if "history" not in st.session_state:

    st.session_state.history = []

if query and uploaded_files:

    result = st.session_state.graph.invoke({
        "query":query,
        "uploaded_files":uploaded_files,
        "conversation_history":st.session_state.history
    })

    st.session_state.history.append({
        "question":query,
        "answer":result["response"]
    })

    with st.chat_message("user"):

        st.write(query)

    with st.chat_message("assistant"):

        st.write(result["response"])

    with st.expander("Source Citations"):

        for citation in result["citations"]:

            st.write(
                f'''
File:
{citation["filename"]}

Page:
{citation["page"]}

Chunk:
{citation["chunk_id"]}

Content:
{citation["content"]}
'''
            )

    with st.expander("Evaluation"):

        st.write(
            f'''
Score:
{result["evaluation_score"]}

Feedback:
{result["feedback"]}
'''
        )
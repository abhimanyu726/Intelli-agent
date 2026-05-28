# IntelliAgent

Enterprise-grade Multi-Agent RAG Knowledge Assistant built using LangGraph, OpenAI, FAISS, and Streamlit.

## Features

- Multi-Agent LangGraph Workflow
- Conversational Memory
- Strict Grounded Responses
- Retrieval Validation
- FAISS Vector Database
- OpenAI Embeddings
- Streamlit UI
- Source Citations
- Evaluation Agent
- Multi-PDF Support

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Environment Variables

Create `.env` file:

```env
OPENAI_API_KEY=your_key
MODEL_NAME=gpt-4o-mini
```
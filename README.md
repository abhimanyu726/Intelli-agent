# IntelliAgent

Enterprise-grade Multi-Agent Conversational RAG Assistant built using LangGraph, OpenAI, FAISS, and Streamlit.

## Features

* Multi-Agent LangGraph Workflow
* Conversational Memory
* Contextual Query Rewriting
* Strict Grounded Responses
* Retrieval Validation
* FAISS Vector Database
* OpenAI Embeddings
* Streamlit UI
* Source Citations
* Evaluation Agent
* Multi-PDF Support
* Hallucination Prevention
* Semantic Search
* Persistent VectorStore

## Architecture

```text
User Query
    ↓
Memory Node
    ↓
Retrieval Node
    ↓
Validation Node
    ↓
Response Node
    ↓
Evaluation Node
```

## Tech Stack

* LangGraph
* OpenAI GPT-4o-mini
* OpenAI Embeddings
* FAISS
* Streamlit
* PyMuPDF (fitz)
* PydanticOutputParser
* RecursiveCharacterTextSplitter

## Project Structure

```bash
intelliagent/

│── app.py
│── requirements.txt
│── README.md
│── .env.example
│── Dockerfile

│── config/
│   ├── settings.py
│   └── prompts.py

│── graph/
│   ├── state.py
│   └── graph_builder.py

│── nodes/
│   ├── ingestion_node.py
│   ├── memory_node.py
│   ├── retrieval_node.py
│   ├── validation_node.py
│   ├── response_node.py
│   └── evaluator_node.py

│── services/
│   ├── llm_service.py
│   ├── embedding_service.py
│   ├── vectorstore_service.py
│   ├── document_service.py
│   ├── retrieval_service.py
│   └── citation_service.py

│── data/
│   ├── uploads/
│   └── vectorstore/
```

## Workflow

### 1. Ingestion Node

* Loads uploaded PDFs
* Extracts document text
* Chunks documents
* Creates embeddings
* Stores vectors in FAISS

### 2. Memory Node

* Handles conversational memory
* Rewrites follow-up queries
* Resolves ambiguous references

### 3. Retrieval Node

* Performs semantic retrieval
* Fetches top relevant chunks
* Removes duplicate chunks

### 4. Validation Node

* Validates retrieval quality
* Checks evidence sufficiency
* Prevents weak-context answering

### 5. Response Node

* Generates grounded responses
* Uses only retrieved context
* Produces citations

### 6. Evaluation Node

* Evaluates response quality
* Scores grounding accuracy
* Detects hallucination risks

## Conversational Memory

The system supports multi-turn conversations using:

* `st.session_state.history`
* contextual query rewriting
* memory-aware retrieval

Example:

```text
User: What is reinforcement learning?
User: How is it different from supervised learning?
```

The memory node rewrites:

```text
How is it different from supervised learning?
```

into:

```text
How is reinforcement learning different from supervised learning?
```

before retrieval.

## Grounded Response Behavior

The assistant:

* answers ONLY from uploaded documents
* refuses unsupported queries
* avoids hallucinations
* avoids external knowledge usage

If sufficient information is unavailable:

```text
The uploaded documents do not contain sufficient information to answer this query.
```

## VectorStore Persistence

The FAISS vectorstore:

* persists locally on disk
* reloads across Streamlit reruns
* avoids repeated embeddings

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

## Debugging

### Memory Debugging

Add inside `memory_node.py`

```python
print(state["query"])
print(rewritten_query)
```

### Retrieval Debugging

Add inside `retrieval_node.py`

```python
print(doc.page_content[:500])
```

### VectorStore Debugging

Add inside `vectorstore_service.py`

```python
print("CREATING NEW VECTORSTORE")
print("LOADING EXISTING VECTORSTORE")
```

## Future Improvements

* Hybrid Search
* BM25 + Vector Retrieval
* Reranking
* Metadata Filtering
* Streaming Responses
* Docker Deployment
* Cloud Vector Databases
* Redis Caching
* Async Execution

## Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Conversational RAG
* LangGraph Orchestration
* Multi-Agent Workflows
* Prompt Engineering
* Structured Outputs
* Semantic Search
* Hallucination Prevention
* Citation Generation
* Grounded AI Systems
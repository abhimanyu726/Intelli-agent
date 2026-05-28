import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "gpt-4o-mini"
    )

    EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "text-embedding-3-small"
    )

    CHUNK_SIZE = 800

    CHUNK_OVERLAP = 150

    RETRIEVAL_TOP_K = 8

    VECTORSTORE_PATH = "data/vectorstore/faiss_index"

    MAX_CONTEXT_CHUNKS = 4
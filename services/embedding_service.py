from langchain_openai import OpenAIEmbeddings
from config.settings import Settings


class EmbeddingService:

    def __init__(self):

        self.embedding_model = OpenAIEmbeddings(
            api_key=Settings.OPENAI_API_KEY,
            model=Settings.EMBEDDING_MODEL
        )

    def get_embeddings(self):

        return self.embedding_model
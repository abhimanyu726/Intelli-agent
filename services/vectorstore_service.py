import os
import shutil

from langchain_community.vectorstores import FAISS

from services.embedding_service import EmbeddingService

from config.settings import Settings


class VectorStoreService:

    def __init__(self):

        embedding_service = EmbeddingService()

        self.embeddings = embedding_service.get_embeddings()

    def create_vectorstore(self,chunks):

        if os.path.exists(
            Settings.VECTORSTORE_PATH
        ):

            shutil.rmtree(
                Settings.VECTORSTORE_PATH
            )

        vectorstore = FAISS.from_documents(
            documents=chunks,
            embedding=self.embeddings
        )

        vectorstore.save_local(
            Settings.VECTORSTORE_PATH
        )

    def load_vectorstore(self):

        if not os.path.exists(
            Settings.VECTORSTORE_PATH
        ):

            raise ValueError(
                "Vectorstore not found."
            )

        vectorstore = FAISS.load_local(
            Settings.VECTORSTORE_PATH,
            self.embeddings,
            allow_dangerous_deserialization=True
        )

        return vectorstore

    def similarity_search(
        self,
        query,
        k=5
    ):

        vectorstore = self.load_vectorstore()

        return vectorstore.similarity_search(
            query,
            k=k
        )

from services.vectorstore_service import VectorStoreService

from config.settings import Settings


class RetrievalService:

    def __init__(self):

        self.vectorstore_service = VectorStoreService()

    def retrieve(self,query):

        retrieved_docs = self.vectorstore_service.similarity_search(
            query=query,
            k=Settings.RETRIEVAL_TOP_K
        )

        filtered_docs = []

        seen_content = set()

        for doc in retrieved_docs:

            content = doc.page_content[:150]

            if content not in seen_content:

                filtered_docs.append(doc)

                seen_content.add(content)

        return filtered_docs[:Settings.MAX_CONTEXT_CHUNKS]

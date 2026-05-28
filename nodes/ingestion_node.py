from services.document_service import DocumentService
from services.vectorstore_service import VectorStoreService


class IngestionNode:

    def __init__(self):

        self.document_service = DocumentService()

        self.vectorstore_service = VectorStoreService()

    def execute(self,state):

        documents = self.document_service.load_documents(
            state["uploaded_files"]
        )

        chunks = self.document_service.chunk_documents(
            documents
        )

        self.vectorstore_service.create_vectorstore(
            chunks
        )

        state["documents"] = documents

        state["chunks"] = chunks

        return state
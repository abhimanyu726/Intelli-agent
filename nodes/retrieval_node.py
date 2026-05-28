from services.retrieval_service import RetrievalService


class RetrievalNode:

    def __init__(self):

        self.retrieval_service = RetrievalService()

    def execute(self,state):

        retrieved_chunks = self.retrieval_service.retrieve(
            state["contextualized_query"]
        )

        print("\n========== RETRIEVED CHUNKS ==========\n")

        for idx,doc in enumerate(retrieved_chunks):

            print(f"\nCHUNK {idx + 1}\n")

            print(doc.page_content[:500])

            print("\n============================\n")

        state["retrieved_chunks"] = retrieved_chunks

        return state
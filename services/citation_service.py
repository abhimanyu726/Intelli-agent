class CitationService:

    def generate_citations(self,documents):

        citations = []

        for doc in documents:

            citations.append({
                "filename":doc.metadata.get("source"),
                "page":doc.metadata.get("page"),
                "chunk_id":doc.metadata.get("chunk_id"),
                "content":doc.page_content[:300]
            })

        return citations
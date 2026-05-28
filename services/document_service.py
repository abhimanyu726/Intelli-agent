import fitz

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.settings import Settings


class DocumentService:

    def load_documents(self,uploaded_files):

        documents = []

        for file in uploaded_files:

            pdf = fitz.open(
                stream=file.read(),
                filetype="pdf"
            )

            for page_num,page in enumerate(pdf):

                text = page.get_text().strip()

                if not text:
                    continue

                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source":file.name,
                            "page":page_num + 1
                        }
                    )
                )

        return documents

    def chunk_documents(self,documents):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=Settings.CHUNK_SIZE,
            chunk_overlap=Settings.CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

        chunks = splitter.split_documents(documents)

        for idx,chunk in enumerate(chunks):

            chunk.metadata["chunk_id"] = idx

        return chunks
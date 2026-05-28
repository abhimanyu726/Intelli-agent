from typing import List,Optional,Dict,Any
from typing_extensions import TypedDict
from pydantic import BaseModel,Field
from langchain_core.documents import Document


class GraphState(TypedDict):

    query:str
    contextualized_query:str
    uploaded_files:List[Any]
    documents:List[Document]
    chunks:List[Document]
    retrieved_chunks:List[Document]
    filtered_chunks:List[Document]
    response:str
    citations:List[Dict]
    conversation_history:List[Dict]
    evaluation_score:Optional[float]
    feedback:Optional[str]
    retrieval_metadata:Dict
    retrieval_approved:bool
    retrieval_feedback:str

class CitationOutput(BaseModel):

    filename:str
    page:int
    content:str

class ResponseOutput(BaseModel):

    answer:str
    citations:List[CitationOutput]

class EvaluationOutput(BaseModel):

    score:float = Field(
        ge=0,
        le=10
    )
    feedback:str


class RetrievalValidationOutput(BaseModel):

    approved:bool
    feedback:str
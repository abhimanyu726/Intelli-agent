from langchain_core.output_parsers import PydanticOutputParser

from graph.state import ResponseOutput

from config.prompts import RESPONSE_PROMPT

from services.llm_service import LLMService
from services.citation_service import CitationService


class ResponseNode:

    def __init__(self):

        self.llm_service = LLMService()

        self.citation_service = CitationService()

        self.parser = PydanticOutputParser(
            pydantic_object=ResponseOutput
        )

    def execute(self,state):

        if not state["retrieval_approved"]:

            state["response"] = "The uploaded documents do not contain sufficient information to answer this query."

            state["citations"] = []

            return state

        context = "\n\n".join([
            f'''
SOURCE:
{doc.metadata.get("source")}

PAGE:
{doc.metadata.get("page")}

CONTENT:
{doc.page_content}
'''
            for doc in state["retrieved_chunks"]
        ])

        prompt = RESPONSE_PROMPT.format(
            query=state["contextualized_query"],
            context=context,
            format_instructions=self.parser.get_format_instructions()
        )

        response = self.llm_service.generate(prompt)

        parsed_response = self.parser.parse(response)

        citations = self.citation_service.generate_citations(
            state["retrieved_chunks"]
        )

        state["response"] = parsed_response.answer

        state["citations"] = citations

        return state
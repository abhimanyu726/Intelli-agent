from langchain_core.output_parsers import PydanticOutputParser

from graph.state import RetrievalValidationOutput

from config.prompts import RETRIEVAL_VALIDATION_PROMPT

from services.llm_service import LLMService


class ValidationNode:

    def __init__(self):

        self.llm_service = LLMService()

        self.parser = PydanticOutputParser(
            pydantic_object=RetrievalValidationOutput
        )

    def execute(self,state):

        context = "\n\n".join([
            doc.page_content
            for doc in state["retrieved_chunks"]
        ])

        prompt = RETRIEVAL_VALIDATION_PROMPT.format(
            query=state["contextualized_query"],
            context=context,
            format_instructions=self.parser.get_format_instructions()
        )

        response = self.llm_service.generate(prompt)

        parsed_response = self.parser.parse(response)

        state["retrieval_approved"] = parsed_response.approved

        state["retrieval_feedback"] = parsed_response.feedback

        return state
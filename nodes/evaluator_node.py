from langchain_core.output_parsers import PydanticOutputParser

from graph.state import EvaluationOutput

from config.prompts import EVALUATION_PROMPT

from services.llm_service import LLMService


class EvaluatorNode:

    def __init__(self):

        self.llm_service = LLMService()

        self.parser = PydanticOutputParser(
            pydantic_object=EvaluationOutput
        )

    def execute(self,state):

        prompt = EVALUATION_PROMPT.format(
            query=state["query"],
            response=state["response"],
            format_instructions=self.parser.get_format_instructions()
        )

        response = self.llm_service.generate(prompt)

        parsed_response = self.parser.parse(response)

        state["evaluation_score"] = parsed_response.score

        state["feedback"] = parsed_response.feedback

        return state
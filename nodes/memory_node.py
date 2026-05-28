from services.llm_service import LLMService
from config.prompts import MEMORY_PROMPT


class MemoryNode:

    def __init__(self):

        self.llm_service = LLMService()

    def execute(self,state):

        history = state.get(
            "conversation_history",
            []
        )

        if not history:

            state["contextualized_query"] = state["query"]

            return state

        recent_history = history[-3:]

        formatted_history = "\n".join([
            f'''
USER:
{chat["question"]}

ASSISTANT:
{chat["answer"]}
'''
            for chat in recent_history
        ])

        prompt = MEMORY_PROMPT.format(
            conversation_history=formatted_history,
            query=state["query"]
        )

        rewritten_query = self.llm_service.generate(prompt)

        print("\n========== MEMORY DEBUG ==========\n")

        print("ORIGINAL QUERY:\n")
        print(state["query"])

        print("\nREWRITTEN QUERY:\n")
        print(rewritten_query)

        print("\n==================================\n")

        state["contextualized_query"] = rewritten_query

        return state
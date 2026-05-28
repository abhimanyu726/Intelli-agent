from langchain_openai import ChatOpenAI
from config.settings import Settings


class LLMService:

    def __init__(self):

        self.llm = ChatOpenAI(
            api_key=Settings.OPENAI_API_KEY,
            model=Settings.MODEL_NAME,
            temperature=0
        )

    def generate(self,prompt:str):

        response = self.llm.invoke(prompt)

        return response.content
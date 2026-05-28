from langgraph.graph import StateGraph,END

from graph.state import GraphState

from nodes.ingestion_node import IngestionNode
from nodes.memory_node import MemoryNode
from nodes.retrieval_node import RetrievalNode
from nodes.validation_node import ValidationNode
from nodes.response_node import ResponseNode
from nodes.evaluator_node import EvaluatorNode


class IntelliAgentGraph:

    def __init__(self):

        self.workflow = StateGraph(GraphState)

        self.build()

    def build(self):

        self.workflow.add_node("ingestion", IngestionNode().execute)
        self.workflow.add_node("memory", MemoryNode().execute)
        self.workflow.add_node("retrieval", RetrievalNode().execute)
        self.workflow.add_node("validation", ValidationNode().execute)
        self.workflow.add_node("response", ResponseNode().execute)
        self.workflow.add_node("evaluation", EvaluatorNode().execute)

        self.workflow.set_entry_point("ingestion")

        self.workflow.add_edge("ingestion", "memory")
        self.workflow.add_edge("memory", "retrieval")
        self.workflow.add_edge("retrieval", "validation")
        self.workflow.add_edge("validation", "response")
        self.workflow.add_edge("response", "evaluation")
        self.workflow.add_edge("evaluation", END)

    def compile(self):

        return self.workflow.compile()
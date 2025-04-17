import operator
from typing import Annotated, Sequence
from langchain_core.messages import BaseMessage, FunctionMessage, HumanMessage
from langgraph.graph.message import add_messages

from typing_extensions import TypedDict


def merge_dicts(a: dict[str, any], b: dict[str, any]) -> dict[str, any]:
    return {**a, **b}


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

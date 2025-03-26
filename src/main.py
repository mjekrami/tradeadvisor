import operator
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import tool
from typing import TypedDict, Annotated, Union
from langchain_core.agents import AgentAction, AgentFinish
from langchain.agents import create_openai_tools_agent
from langchain_openai import ChatOpenAI

COMPLETE_PROMPT = """Provide a detailed, actionable analysis to determine today's optimal entry point for Bitcoin (BTC). Clearly structure your response with the following components:

1. Technical Analysis:

Identify major support and resistance levels for BTC.

Evaluate critical technical indicators such as RSI, MACD, Moving Averages, and Volume.

Highlight significant chart patterns, candlestick formations, or emerging trendlines that influence today's trading conditions.

2. Market Sentiment & News Analysis:

Summarize current market sentiment by reviewing leading financial news sources, influential analysts' opinions, and social media trends.

Highlight any significant news events or economic announcements that could impact Bitcoin’s price movement within the next 24 hours.

3. Probability Assessment:

Clearly outline the estimated probability of success for both Long and Short positions based on combined technical analysis and market sentiment.

Provide concise reasoning to support these probabilities.

4. Recommended Daily Trading Strategy:

Specify your recommended trading position clearly: either Long or Short.

Provide exact entry price, suggested stop-loss level, and clearly defined profit-taking targets.

Briefly outline potential risks and alternative market scenarios.

Your analysis should be precise, well-structured, and supported by thorough reasoning, ensuring clarity and actionable insights for daily trading decisions.
"""


class AgentState(TypedDict):
    input: str
    agent_out: Union[AgentAction, AgentFinish, None]
    intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]


@tool("search")
def search_tool(query: str):
    """Searches for information on the topic of artificial inteligence (AI).
    Cannot be used to research any other topics. Search query must be provided
    in natural language and be verbose."""
    return COMPLETE_PROMPT


@tool("final_answer")
def final_answer_tool(answer: str, source: str):
    """Returns a natural language response to the user in `answer`, and
    a `source` which provides citation for where this information came from.
    """
    return ""


llm = ChatOpenAI(
    temperature=0,
    api_key="sk-wsSXBy9BTQgVlWzdba2HDw",
    base_url="https://chatapi.akash.network/api/v1",
    model="DeepSeek-R1-Distill-Qwen-32B",
)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ],
)
query_agent_runnable = create_openai_tools_agent(
    llm, [final_answer_tool, search_tool], prompt
)

inputs = {
    "input": "Use search tool to give me the final answer. summarize the search .",
    "agent_scratchpad": [],
    "intermediate_steps": [],
}

print(query_agent_runnable.invoke(inputs))

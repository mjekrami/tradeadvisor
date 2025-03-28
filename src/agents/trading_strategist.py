from llms import akash_llm
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent

TRADING_STRATEGIST_PROMPT = """
You will design a specific, actionable trading strategy based on the analysis.

Tasks:
1. Trading Position:
        Based on the probability analysis: {probability_analysis}, recommend a Long or Short position.
2. Entry Price:
        Provide the optimal entry point for Bitcoin (BTC) based on technical levels and current price action.
3. Stop-Loss Level:
        Define the stop-loss level based on support/resistance or volatility.
4. Profit-Taking Targets:
        Set profit-taking levels based on key resistance levels, Fibonacci retracements, or percentage targets.
5. Risk Assessment:
        Outline potential risks associated with the recommended position (e.g., unexpected news, breakout failure).
Suggest alternative market scenarios (e.g., if the price breaks through a major support level, consider a Short position).
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", TRADING_STRATEGIST_PROMPT),
        ("human", "{probability_analysis}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)


def create_trading_strategist_agent():
    tools = []
    agent = create_tool_calling_agent(akash_llm, tools, prompt)
    return agent

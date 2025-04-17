from config import CONFIG
from llms import get_llm
from agents import get_agent
from .state import AgentState

# Initialize agents with their respective LLMs
market_sentiment = get_agent(
    "market_sentiment", get_llm(CONFIG.agent_config["market_sentiment"]["llm"])
)
technical_analyst = get_agent(
    "technical_analyst", get_llm(CONFIG.agent_config["technical_analyst"]["llm"])
)
probability_assistance = get_agent(
    "probability_assistance",
    get_llm(CONFIG.agent_config["probability_assistance"]["llm"]),
)
trading_strategist = get_agent(
    "trading_strategist", get_llm(CONFIG.agent_config["trading_strategist"]["llm"])
)


# Wrap agent calls for LangGraph
def run_market_sentiment(state: AgentState):
    print(f"Market sentiment: agent with state: {state['messages'][-1]}")
    result = market_sentiment.invoke(
        {"input": state["messages"], "intermediate_steps": []}
    )
    print(f"Market sentiment-> result: {result[-1]}")
    return {"messages": [result]}


def run_technical_analyst(state):
    print(f"Running technical_analyst  agent with state: {state}")
    result = technical_analyst.invoke(
        {"input": state["messages"], "intermediate_steps": []}
    )
    return {"messages": [result]}


def run_probability_assistance(state):
    print(f"Running probability_assistance agent with state: {state}")
    result = probability_assistance.invoke(
        {"input": state["messages"], "intermediate_steps": []}
    )
    return {"messages": [result]}


def run_trading_strategist(state):
    return {"messages": trading_strategist.invoke(state["messages"])}

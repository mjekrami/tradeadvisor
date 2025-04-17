from .state import AgentState
from .nodes import (
    run_market_sentiment,
    run_probability_assistance,
    run_technical_analyst,
    run_trading_strategist,
)
from langgraph.graph import StateGraph, START, END

builder = StateGraph(AgentState)

# Nodes
builder.add_node("market_sentiment", run_market_sentiment)
builder.add_node("technical_analyst", run_technical_analyst)
builder.add_node("probability_assistance", run_probability_assistance)
builder.add_node("trading_strategist", run_trading_strategist)

# Edges
builder.add_edge(START, "market_sentiment")
builder.add_edge("market_sentiment", "technical_analyst")
builder.add_edge("technical_analyst", "probability_assistance")
builder.add_edge("probability_assistance", "trading_strategist")
builder.add_edge("trading_strategist", END)

graph = builder.compile()

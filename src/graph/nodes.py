from langchain_core.messages import HumanMessage

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
    agent_name = "Market Sentiment"
    try:
        print(f"{agent_name}: agent with state: {state['messages'][-1]}")
        result = market_sentiment.invoke(
            {"input": state["messages"], "intermediate_steps": []}
        )

        actual_payload = result[0] if isinstance(result, list) and len(result) > 0 else result

        if hasattr(actual_payload, 'content'):
            message_content = actual_payload.content
        elif isinstance(actual_payload, dict):
            message_content = actual_payload.get("output", "")
        else:
            message_content = str(actual_payload) # Fallback

        if not isinstance(message_content, str):
            message_content = str(message_content) # Ensure it's a string

        print(f"{agent_name} -> result: {message_content}")
        return {"messages": [HumanMessage(content=message_content)]}
    except Exception as e:
        error_message = f"Error in {agent_name} agent: {e}. Input: {state['messages'][-1] if state['messages'] else 'empty'}"
        print(error_message)
        return {"messages": [HumanMessage(content=f"Error in {agent_name}: {e}")]}


def run_technical_analyst(state: AgentState):
    agent_name = "Technical Analyst"
    try:
        print(f"Running {agent_name} agent with state: {state['messages'][-1]}")
        result = technical_analyst.invoke(
            {"input": state["messages"][-1].content, "intermediate_steps": []}
        )

        actual_payload = result[0] if isinstance(result, list) and len(result) > 0 else result

        if hasattr(actual_payload, 'content'):
            message_content = actual_payload.content
        elif isinstance(actual_payload, dict):
            message_content = actual_payload.get("output", "")
        else:
            message_content = str(actual_payload) # Fallback

        if not isinstance(message_content, str):
            message_content = str(message_content) # Ensure it's a string

        print(f"{agent_name} -> result: {message_content}")
        return {"messages": [HumanMessage(content=message_content)]}
    except Exception as e:
        error_message = f"Error in {agent_name} agent: {e}. Input: {state['messages'][-1].content if state['messages'] else 'empty'}"
        print(error_message)
        return {"messages": [HumanMessage(content=f"Error in {agent_name}: {e}")]}


def run_probability_assistance(state: AgentState):
    agent_name = "Probability Assistance"
    try:
        print(f"Running {agent_name} agent with state: {state['messages'][-1]}")
        result = probability_assistance.invoke(
            {"input": state["messages"][-1].content, "intermediate_steps": []}
        )

        actual_payload = result[0] if isinstance(result, list) and len(result) > 0 else result

        if hasattr(actual_payload, 'content'):
            message_content = actual_payload.content
        elif isinstance(actual_payload, dict):
            message_content = actual_payload.get("output", "")
        else:
            message_content = str(actual_payload) # Fallback

        if not isinstance(message_content, str):
            message_content = str(message_content) # Ensure it's a string

        print(f"{agent_name} -> result: {message_content}")
        return {"messages": [HumanMessage(content=message_content)]}
    except Exception as e:
        error_message = f"Error in {agent_name} agent: {e}. Input: {state['messages'][-1].content if state['messages'] else 'empty'}"
        print(error_message)
        return {"messages": [HumanMessage(content=f"Error in {agent_name}: {e}")]}


def run_trading_strategist(state: AgentState):
    agent_name = "Trading Strategist"
    try:
        print(f"Running {agent_name} agent with state: {state['messages'][-1]}")
        # The Trading Strategist agent expects 'asset' and 'probability_analysis'.
        # 'agent_scratchpad' is used by the agent framework.
        invoke_input = {
            "asset": state["asset"], # Get asset from graph state
            "probability_analysis": state["messages"][-1].content,
            "intermediate_steps": [] # Or "agent_scratchpad": [] depending on agent type
        }
        result = trading_strategist.invoke(invoke_input)

        # With the simplified agent (prompt | llm), the result should be an AIMessage
        # and its 'content' attribute should directly be the JSON string from the LLM.
        actual_payload = result[0] if isinstance(result, list) and len(result) > 0 else result

        json_string = ""
        if hasattr(actual_payload, 'content'):
            json_string = actual_payload.content
        elif isinstance(actual_payload, str): # If the payload itself is the string
            json_string = actual_payload
        else:
            # Fallback if the structure is not as expected
            json_string = str(actual_payload)

        if not isinstance(json_string, str):
            json_string = str(json_string) # Ensure it's a string for safety

        print(f"{agent_name} -> result (expected JSON string): {json_string}")
        return {"messages": [HumanMessage(content=json_string)]}
    except Exception as e:
        error_message = f"Error in {agent_name} agent: {e}. Input: {state['messages'][-1].content if state['messages'] else 'empty'}"
        print(error_message)
        return {"messages": [HumanMessage(content=f"Error in {agent_name}: {e}")]}

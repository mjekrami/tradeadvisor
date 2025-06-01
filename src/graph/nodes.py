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
        # The Trading Strategist agent expects the output from Probability Assistance
        # under the key 'probability_analysis'.
        invoke_input = {
            "probability_analysis": state["messages"][-1].content,
            "intermediate_steps": []
        }
        # It might also need the full message history or other specific inputs.
        # For now, let's provide 'input' as well, in case its prompt uses it generally,
        # and 'probability_analysis' for the specific part of its prompt.
        # If the agent only needs 'probability_analysis', 'input' could be removed.
        invoke_input["input"] = state["messages"][-1].content

        result = trading_strategist.invoke(invoke_input)

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

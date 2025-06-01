from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_core.language_models import BaseChatModel

# System prompt defining JSON output structure (remains the same)
TRADING_STRATEGIST_SYSTEM_PROMPT = """
You are an expert trading strategist. Your task is to provide a clear, actionable trading recommendation based on the provided probability analysis for a crypto asset.

Your output MUST be a single, valid JSON object with the following keys:
- "asset": The ticker symbol of the crypto asset (e.g., "BTC").
- "recommendation": Your trading recommendation. Must be one of "BUY", "SELL", or "HOLD".
- "confidence": Your confidence in this recommendation. Must be one of "HIGH", "MEDIUM", or "LOW".
- "entry_price": Suggested entry price (float, or the string "N/A" if not applicable).
- "stop_loss": Suggested stop-loss price (float, or the string "N/A" if not applicable).
- "take_profit_targets": A list of suggested take-profit price targets (list of floats, or a list containing the string "N/A" if not applicable).
- "summary": A concise explanation of the strategy, incorporating the probability analysis and risk assessment.

Ensure the output is only the JSON object and nothing else.
"""

# Updated prompt template, removing placeholder for agent_scratchpad as it's not a tool-calling agent now
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", TRADING_STRATEGIST_SYSTEM_PROMPT),
        ("human", "Asset: {asset}\nProbability Analysis:\n{probability_analysis}"),
    ]
)


def create_trading_strategist_agent(llm: BaseChatModel) -> Runnable:
    """
    Creates a trading strategist agent that directly chains the prompt with the LLM.
    This setup is intended to get a direct response from the LLM, hopefully the JSON string.
    """
    # Chain the prompt directly with the LLM.
    # The output of this chain when invoked should be an AIMessage (or similar),
    # and its 'content' attribute should hold the LLM's generated JSON string.
    return prompt | llm

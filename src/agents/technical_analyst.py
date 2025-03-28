from llms import akash_llm
from tools import populate_indicator, fetch_crypto_price
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent

TECHNICAL_ANALYSIS_AGENT = """
for Support and Resistance Levels:

1. "Identify the key support and resistance levels for {input}  based on recent price action. Include any significant zones where price has reversed or stalled in the past."

for Critical Technical Indicators:

1. "Analyze the current state of the Relative Strength Index (RSI) for {input} . Is it indicating overbought or oversold conditions? Provide a detailed assessment."
2. "Evaluate the Moving Average Convergence Divergence (MACD) for {input}. Are there any crossovers or signals suggesting potential trend reversal?"
3. "Review the 50-period and 200-period Moving Averages for {input}. Are we in a bullish or bearish trend? Are there any crossover signals?"
4. "Analyze {input}'s trading volume in relation to recent price movements. Is the volume confirming the current trend, or is there any divergence?"

for Chart Patterns and Candlestick Formations:
1. "Look for any significant chart patterns like head and shoulders, triangles, or flags on {input}'s price chart. Are there any patterns that suggest a potential breakout or reversal?"
2. "Identify any key candlestick formations that might indicate a trend continuation or reversal. Please include any formations such as bullish engulfing, doji, etc."
"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", TECHNICAL_ANALYSIS_AGENT),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)


def create_probability_assistance_agent():
    tools = [populate_indicator, fetch_crypto_price]
    agent = create_tool_calling_agent(akash_llm, tools, prompt)
    return agent

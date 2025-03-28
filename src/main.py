from config import config
from agents import create_market_sentiment_agent
import operator

from typing import TypedDict, Annotated, Union
from langchain_core.agents import AgentAction, AgentFinish

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


market_sentiment = create_market_sentiment_agent()


class AgentState(TypedDict):
    input: str
    agent_out: Union[AgentAction, AgentFinish, None]
    intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]

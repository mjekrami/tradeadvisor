from .technical_analyst import create_technical_assistance_agent
from .trading_strategist import create_trading_strategist_agent
from .market_sentiment import create_market_sentiment_agent
from .probability_assistance import create_probability_assistance_agent


def get_agent(agent_name, llm):
    if agent_name == "market_sentiment":
        return create_market_sentiment_agent(llm=llm)
    elif agent_name == "probability_assistance":
        return create_probability_assistance_agent(llm)
    elif agent_name == "trading_strategist":
        return create_trading_strategist_agent(llm)
    elif agent_name == "technical_analyst":
        return create_technical_assistance_agent(llm)
    else:
        return None

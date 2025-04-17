import ccxt
import pandas as pd
import logging
from langchain.tools import tool

logger = logging.getLogger(__name__)


@tool("price_fetcher")
def fetch_crypto_price(symbol: str, exchange_name: str, since, limit=10):
    """Fetches price of a cryptocurrency symbol from an exchange with since as time with limit"""
    exchange = getattr(ccxt, exchange_name.lower())
    try:
        data = exchange.fetch_ohlcv(symbol, since, limit)
        df = pd.DataFrame(
            data, columns=["timestamp", "open", "high", "low", "close", "volume"]
        )
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df
    except Exception as e:
        logger.error(f"Error occured: {str(e)}")
        return None


@tool("indicator_populator")
def populate_indicator(df: str):
    """Populates indicator (eg. SMA,EMA) for further analysis"""
    df["sma_20"] = df["close"].rolling(20).mean()
    df["sma_50"] = df["close"].rolling(50).mean()
    df["sma_200"] = df["close"].rolling(200).mean()

    df["ema_20"] = df["close"].ewm(20).mean()
    df["ema_50"] = df["close"].ewm(50).mean()
    df["ema_200"] = df["close"].ewm(200).mean()

    return df

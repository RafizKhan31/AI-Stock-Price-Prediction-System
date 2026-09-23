import yfinance as yf
import pandas as pd
import numpy as np


def download_stock_data(ticker, period="5y"):
    """
    Download historical stock market data using Yahoo Finance.
    """

    print(f"\nDownloading data for {ticker}...")

    data = yf.download(
        ticker,
        period=period,
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    if data.empty:
        raise ValueError(
            f"No data found for {ticker}. "
            f"Please check the ticker symbol."
        )

    # Handle MultiIndex columns from newer yfinance versions
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.reset_index()

    return data


def add_technical_indicators(data):
    """
    Add technical indicators and machine-learning features.
    """

    df = data.copy()

    # Moving averages
    df["SMA_10"] = df["Close"].rolling(window=10).mean()
    df["SMA_20"] = df["Close"].rolling(window=20).mean()
    df["SMA_50"] = df["Close"].rolling(window=50).mean()

    # Exponential moving averages
    df["EMA_10"] = df["Close"].ewm(
        span=10,
        adjust=False
    ).mean()

    df["EMA_20"] = df["Close"].ewm(
        span=20,
        adjust=False
    ).mean()

    # Daily returns
    df["Daily_Return"] = df["Close"].pct_change()

    # Volatility
    df["Volatility_10"] = (
        df["Daily_Return"]
        .rolling(window=10)
        .std()
    )

    # Price momentum
    df["Momentum_5"] = (
        df["Close"] - df["Close"].shift(5)
    )

    df["Momentum_10"] = (
        df["Close"] - df["Close"].shift(10)
    )

    # RSI
    delta = df["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss.replace(0, np.nan)

    df["RSI"] = 100 - (100 / (1 + rs))

    # MACD
    ema_12 = df["Close"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema_26 = df["Close"].ewm(
        span=26,
        adjust=False
    ).mean()

    df["MACD"] = ema_12 - ema_26

    # Average True Range
    high_low = df["High"] - df["Low"]

    high_close = (
        df["High"] - df["Close"].shift(1)
    ).abs()

    low_close = (
        df["Low"] - df["Close"].shift(1)
    ).abs()

    true_range = pd.concat(
        [high_low, high_close, low_close],
        axis=1
    ).max(axis=1)

    df["ATR"] = true_range.rolling(
        window=14
    ).mean()

    # Lag features
    df["Close_Lag_1"] = df["Close"].shift(1)
    df["Close_Lag_2"] = df["Close"].shift(2)
    df["Close_Lag_3"] = df["Close"].shift(3)
    df["Close_Lag_5"] = df["Close"].shift(5)
    df["Close_Lag_10"] = df["Close"].shift(10)

    # Target = next day's closing price
    df["Target"] = df["Close"].shift(-1)

    # Remove missing values
    df = df.dropna().reset_index(drop=True)

    return df


def prepare_data(ticker, period="5y"):
    """
    Complete data preparation pipeline.
    """

    data = download_stock_data(
        ticker,
        period
    )

    data = add_technical_indicators(data)

    return data
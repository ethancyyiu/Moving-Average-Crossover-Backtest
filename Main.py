import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("SPY", start="2015-01-01", end="2025-01-01")

if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

print(data.columns)  

data["price"] = data["Close"]

data["SMA20"] = data["price"].rolling(window=20).mean()
data["SMA50"] = data["price"].rolling(window=50).mean()

print(data[["price", "SMA20", "SMA50"]].head(60))

data["signal"] = 0
data.loc[data["SMA20"] > data["SMA50"], "signal"] = 1



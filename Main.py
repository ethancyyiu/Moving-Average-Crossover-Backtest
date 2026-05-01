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
data["position"] = data["signal"].shift(1).fillna(0)

data["return"] = data["price"].pct_change()
data["strategy_return"] = data["return"] * data["position"]

data["buy_hold"] = (1 + data["return"]).cumprod()
data["strategy"] = (1 + data["strategy_return"]).cumprod()

plt.figure(figsize=(12, 6))
plt.plot(data.index, data["buy_hold"], label="Buy & Hold")
plt.plot(data.index, data["strategy"], label="SMA20/50 Strategy")
plt.legend()
plt.title("Cumulative Returns: Buy & Hold vs SMA Crossover")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.grid(True)
plt.show()



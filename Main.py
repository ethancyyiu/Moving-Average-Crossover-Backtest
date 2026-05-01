import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# 1. Download data
data = yf.download("SPY", start="2015-01-01", end="2025-01-01")

print(data.columns)




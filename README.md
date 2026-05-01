# Moving-Average-Crossover-Backtest

Overview
This is a small project where I tried to understand how a super basic trading strategy works. I’m still new to this stuff, so I wanted something simple enough that I could actually finish it without getting lost. The idea is basically: look at two moving averages, see when they cross, and pretend you bought or sold based on that. Then check if that would’ve made money.

It’s honestly more of a learning project than anything “finance‑y”. I mainly used it to get comfortable with Python, pandas, and working with real data.

What the Strategy Even Is
A “moving average” is literally just the average price over the last N days.

SMA20 = average of the last 20 days

SMA50 = average of the last 50 days

The strategy is basically:

If the short-term line (SMA20) goes above the long-term line (SMA50), that’s a “buy” signal.

If it goes below, that’s a “sell” signal.

It’s like following the trend without thinking too hard.

What a Backtest Means
A backtest is just replaying old price data and pretending you traded using your strategy.
It answers: “If I did this in the past, would I have made money or just embarrassed myself?”

The script simulates:

When I would’ve bought

When I would’ve sold

How my money would’ve grown

Whether this strategy is actually better than just buying SPY and chilling

What I Used

Python 3

pandas

numpy

yfinance

matplotlib

Basically the standard beginner quant stack.

Project Structure
main.py          - The actual code
README.txt       - This file
requirements.txt - Libraries I used

How to Run It

Install the libraries:

pip install pandas numpy yfinance matplotlib

Run the script:

python main.py

It’ll print some stats and show a graph comparing the strategy vs buy-and-hold.

What You Get Out of It
The script prints:

How much buy-and-hold made

How much the strategy made

Sharpe ratio (basically risk-adjusted returns)

Max drawdown (how bad the worst drop was)

And it plots both performance lines so you can see which one did better.

Why I Did This
I’m a first-year student trying to learn quant/data stuff, and this felt like a good starter project. It’s simple enough that I didn’t get overwhelmed, but still “real” enough to put on a resume or talk about in interviews.

I learned how to:

Work with financial time series

Calculate indicators

Generate signals

Simulate a strategy

Plot results

Not panic when pandas throws errors

Possible Future Upgrades
If I ever feel like leveling this up:

Add transaction costs

Try different moving averages

Test other assets

Make it object-oriented

Add optimization

But for now, this is good enough for a first-year project.
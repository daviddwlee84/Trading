# MA Cross

How to write a basic pine script strategy?

To write a basic Pine Script strategy, you can follow these steps:

1. Open the TradingView platform and create a new Pine Script.

2. Start with the basic Pine Script template, which includes the study and plot functions. These functions are used to define the inputs and outputs of the strategy.

```sql
//@version=5
strategy("Basic Strategy", overlay=true)
```

3. Define the inputs for your strategy using the input function. Inputs allow you to change parameters of your strategy without having to edit the code. For example, you may want to create an input for the length of a moving average:

```graphql
Copy code
//@version=5
strategy("Basic Strategy", overlay=true)

length = input(title="MA Length", type=input.integer, defval=20)
```

4. Define the conditions for entering and exiting trades. For example, you may want to enter a long position when the close price crosses above a moving average:

```perl
Copy code
//@version=5
strategy("Basic Strategy", overlay=true)

length = input(title="MA Length", type=input.integer, defval=20)

ma = sma(close, length)

buy = crossover(close, ma)
sell = crossunder(close, ma)

strategy.entry("Long", strategy.long, when=buy)
strategy.close("Long", when=sell)
```

5. Use the strategy.entry function to open trades and the strategy.close function to close them. You can specify the trade direction (long or short), the position size, and the conditions for entering and exiting trades.

6. Add a plot to visualize the strategy's signals on the chart:

```scss
Copy code
//@version=5
strategy("Basic Strategy", overlay=true)

length = input(title="MA Length", type=input.integer, defval=20)

ma = sma(close, length)

buy = crossover(close, ma)
sell = crossunder(close, ma)

strategy.entry("Long", strategy.long, when=buy)
strategy.close("Long", when=sell)

plotshape(buy, style=shape.triangleup, location=location.belowbar, color=color.green)
plotshape(sell, style=shape.triangledown, location=location.abovebar, color=color.red)
```

7. Save and backtest your strategy. Make sure to test it on historical data and adjust the inputs as necessary to optimize the performance of the strategy.

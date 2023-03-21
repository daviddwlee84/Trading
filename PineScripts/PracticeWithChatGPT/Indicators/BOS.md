# Break Of Structure

How to capture break of structure (BOS) with pine script?

Capturing a break of structure (BOS) with Pine Script can be done by comparing the current price to previous price levels to identify a break of support or resistance.

Here is an example of how to capture a break of structure using Pine Script:

```scss
//@version=5
indicator("Break of Structure", overlay=true)

// Define the input variables
src = input(close, title="Source")
lookback = input(title="Lookback", type=input.integer, defval=20)

// Calculate the previous price levels
prevHigh = highest(src, lookback)
prevLow = lowest(src, lookback)

// Determine if the current price breaks the previous high or low
bosUp = src > prevHigh
bosDown = src < prevLow

// Plot the break of structure levels
plot(bosUp ? prevHigh : na, color=color.green, style=plot.style_circles)
plot(bosDown ? prevLow : na, color=color.red, style=plot.style_circles)
```

In this example, we first define the input variables for the source data and the lookback period. The highest and lowest functions are then used to calculate the previous high and low price levels over the specified lookback period.

We then use conditional statements to determine if the current price breaks the previous high or low. If the current price is above the previous high, bosUp is set to true. If the current price is below the previous low, bosDown is set to true.

Finally, we use the plot function to display the break of structure levels on the chart as circles. If the current price does not break a previous high or low, we use the na (not available) value to prevent the plot from displaying any data for that period.

## Resources

* [BOS — Indicators and Signals — TradingView](https://www.tradingview.com/scripts/bos/)


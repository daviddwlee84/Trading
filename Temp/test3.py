import plotly.offline as offline
import plotly.graph_objects as go
from plotly.subplots import make_subplots


import yfinance as yf
from pprint import pprint

ticker = yf.Ticker('MSFT')
pprint(ticker.info)

# Open        High         Low       Close    Volume  Dividends  Stock Splits
data = ticker.history()

import ipdb
ipdb.set_trace()

fig = go.Figure()
fig.add_candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])

fig.show()


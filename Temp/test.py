import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# https://towardsdatascience.com/trading-technical-analysis-with-pandas-43e737a17861
# https://stackoverflow.com/questions/19231871/convert-unix-time-to-readable-date-in-pandas-dataframe
# df = pd.read_csv('CURRENCYCOM_US30, 1.csv', index_col='time', infer_datetime_format=True,
#                  parse_dates=True, usecols=['time', 'open', 'high', 'low', 'close'])

df = pd.read_csv('CURRENCYCOM_US30, 1.csv', index_col='time', date_parser=lambda x: pd.to_datetime(x, unit='s'),
                 parse_dates=True, usecols=['time', 'open', 'high', 'low', 'close'])

# import ipdb
# ipdb.set_trace()

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(go.Candlestick(x=df.index,
                             open=df['open'],
                             high=df['high'],
                             low=df['low'],
                             close=df['close'],
                             ))
fig.show()

# import ipdb
# ipdb.set_trace()


trade = pd.read_csv('export-1651862202.csv', sep=';')

import ipdb
ipdb.set_trace()

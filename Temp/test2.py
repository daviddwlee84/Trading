import pandas as pd
import plotly.offline as offline
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# df = pd.read_csv('CURRENCYCOM_US30, 1.csv', index_col='time', date_parser=lambda x: pd.to_datetime(x, unit='s'),
#                  parse_dates=True, usecols=['time', 'open', 'high', 'low', 'close'])

# # import ipdb
# # ipdb.set_trace()

# fig = make_subplots(specs=[[{"secondary_y": True}]])
# fig.add_trace(go.Candlestick(x=df.index,
#                              open=df['open'],
#                              high=df['high'],
#                              low=df['low'],
#                              close=df['close'],
#                              ))
# fig.show()

# import ipdb
# ipdb.set_trace()


trade = pd.read_csv('export-1651862202.csv', sep=';')


from tvDatafeed import TvDatafeed, Interval

tv = TvDatafeed(
    chromedriver_path='C:\\Users\\daweilee\\Documents\\Program\\Trading\\Temp2\\chromedriver.exe')

symbols = pd.unique(trade['Symbol'])

exchange_mapping = {
    'LTCUSD': 'COINBASE',
    'BTCUSD': 'COINBASE',
    # 'US30.cash': 'Currency.com',
    # 'US30.cash': 'CAPITALCOM',
    'US30.cash': 'GLOBALPRIME',
    'US100.cash': 'GLOBALPRIME',
    'ETHUSD': 'COINBASE',
    'EURUSD': 'OANDA'
}

symbol_mapping = {
    'LTCUSD': 'LTCUSD',
    'BTCUSD': 'BTCUSD',
    'US30.cash': 'US30',
    'US100.cash': 'NAS100',
    'ETHUSD': 'ETHUSD',
    'EURUSD': 'EURUSD'
}


# import ipdb
# ipdb.set_trace()

all_data = {}

for symbol in symbols:
    print(
        f'Parsing {symbol} ({symbol_mapping[symbol]}) on {exchange_mapping[symbol]} exchange')
    all_data[symbol] = tv.get_hist(
        symbol=symbol_mapping[symbol], exchange=exchange_mapping[symbol], interval=Interval.in_1_hour, n_bars=2000)

print(all_data)

# fig = make_subplots(specs=[[{"secondary_y": True}]])
# for symbol, data in all_data.items():
#     print(f'Ploting {symbol}')
#     fig.add_trace(go.Candlestick(x=data.index,
#                                  open=data['open'],
#                                  high=data['high'],
#                                  low=data['low'],
#                                  close=data['close'],
#                                  ))
# fig.show()

html_graphs = open("DASHBOARD.html", 'w')
html_graphs.write("<html><head></head><body>" + "\n")

# https://stackoverflow.com/questions/45577255/plotly-plot-multiple-figures-as-subplots
for symbol, df in all_data.items():
    print(f'Ploting {symbol}')
    trace = go.Candlestick(x=df.index,
                           open=df['open'],
                           high=df['high'],
                           low=df['low'],
                           close=df['close'],
                           )
    data = [trace]
    layout = go.Layout(title=symbol, yaxis={'title': 'Price'})
    fig = go.Figure(data, layout)

    thistrade = trade[trade['Symbol'] == symbol]
    import ipdb
    ipdb.set_trace()
    for i, row in thistrade.iterrows():
        # https://plotly.com/python/shapes/#adding-shapes-to-subplots
        fig.add_vrect(x0=row['Open'], x1=row['Close'], fillcolor='red' if row['Type']
                      == 'sell' else 'green', opacity=0.5, layer='below', line_width=0)

    import ipdb
    ipdb.set_trace()
    offline.plot(fig, filename=f'Chart_{symbol}.html', auto_open=False)
    html_graphs.write("  <object data=\"" +
                      f'Chart_{symbol}' + '.html' + "\" width=\"650\" height=\"500\"></object>" + "\n")

html_graphs.write("</body></html>")
html_graphs.close()

import os
os.system('start DASHBOARD.html')

import ipdb
ipdb.set_trace()

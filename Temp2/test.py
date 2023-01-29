# https://github.com/StreamAlpha/tvdatafeed

from tvDatafeed import TvDatafeed, Interval

username = 'daviddwlee84@gmail.com'
password = 'Dwl@84323'


tv = TvDatafeed(username, password,
                chromedriver_path='C:\\Users\\daweilee\\Documents\\Program\\Trading\\Temp2\\chromedriver.exe')
# tv = TvDatafeed(auto_login=False,
#                 chromedriver_path='C:\\Users\\daweilee\\Documents\\Program\\Trading\\Temp2\\chromedriver.exe')
import ipdb
ipdb.set_trace()

nifty_index_data = tv.get_hist(
    symbol='NIFTY', exchange='NSE', interval=Interval.in_1_hour, n_bars=1000)

import pandas as pd
import pandas_datareader as pdr
import datetime
import numpy as np

start = datetime.date.today() - datetime.timedelta(days=365)
end = datetime.date.today()

symbol = 'qqq'
def get_kline_data(self, ktype='ma200'):
    today=datetime.now().strftime('%Y-%m-%d')
    df = pdr.get_data_yahoo(symbol.upper(),start=start,end=end)
    return (df[[ktype]])

s = pd.Series("High", "Low", "Open", "Close", "Volume", "Adj Close")
print(s.describe())

import getopt,sys,config,os
import pandas_datareader.data as web
import pandas as pd
import pandas_datareader.data as pdr
import datetime
import mysystemd
import os
import getopt
import sys
import config

from telegram import Bot
from pandas_datareader._utils import RemoteDataError

symbols = [["SPY",10,50],["QQQ",13,55,200]]
# symbols = [["SPY",10,50]]
# notifychat = "-1001736291765"
# receiver = "-1001478922081"
ds = ['yahoo']



def cal_symbols_avg_yahoo(symbol:str,avgs:list):
    start = datetime.date.today() - datetime.timedelta(days=365)
    end = datetime.date.today()
    df = web.DataReader(symbol.upper(), ds[1],start=start,end=end)
    message = f"{symbol.upper()}价格: {df['Close'][-1]:0.2f}({df['Low'][-1]:0.2f} - {df['High'][-1]:0.2f}) \n" 
    print(message)
#     for avg in avgs:
#         if df.count()[0] > avg :
#             message += f"{avg} 周期均价：{df.tail(avg)['Adj Close'].mean():0.2f}\n"
#         else:
#             message += f"{avg} 周期均价因周期不足无法得出结果\n"
#         return f"{message}\n"


if __name__ == '__main__':
    message = "🌈🌈🌈当日天相🌈🌈🌈: \n" 
    for symbol in symbols:
         message += cal_symbols_avg_yahoo(symbol[0],symbol[1:])
    
# config.config_file = os.path.join(config.config_path, "config.json")
# CONFIG = config.load_config()
# bot = Bot(token = CONFIG['Token']) 
# bot.send_message(notifychat,message)
# bot.send_message(receiver,f"向{notifychat}发送成功夕阳红:\n{message}")nd


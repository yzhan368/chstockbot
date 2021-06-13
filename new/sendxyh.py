import pandas as pd
import pandas_datareader as pdr
import datetime
import numpy as np
from telegram import Bot
from telegram import Update, ForceReply
from telegram.botcommand import BotCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


start = datetime.date.today() - datetime.timedelta(days=365)
end = datetime.date.today()

symbol = 'QQQ'
df = pdr.get_data_yahoo(symbol.upper(),start=start,end=end)

def get_kline_data(self, ktype='ma50'):
    return (df[[ktype]])
qqq_fifty_average = round{df[].mean()}
bot_reply = f'''
当日交易一览
QQQ今日50周期均价：{qqq_Adj close} ({qqq_low} {qqq_high})
50周期均价：{qqq_fifty_average}
'''

p = df.tail(50)['Adj Close'].mean()
p = df.tail(50)['High'].mean()
p = df.tail(50)['Low'].mean()

def ticker_command(update: Update, _: CallbackContext) -> None:
    update.message.chat.id == -1001250988031
    update.message.reply_text("QQQ的50周期均线为：{p}")

def sendxyh(update: Update, _: CallbackContext) -> None:
        bot = update.effective_message.bot
        update.message.reply_text(update.message.text)

def add_dispatcher(dp):
    dp.add_handler(CommandHandler("ticker", ticker_command))
    dp.add_handler(CommandHandler("QQQ", bot_reply))
    dp.add_handler(CommandHandler("xyh", sendxyh))
    return [BotCommand('spy','获取QQQ50周期价格')]

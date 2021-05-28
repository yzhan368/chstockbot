from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

zero_phrase = [
"负责取经验的机器人熟睡中被牛撞了！ \nThe ExpBot got clubbed by a cow on the way to get experience point!", 
"负责取经验的机器人路上被蜜蜂蛰了！ \nThe ExpBot got stuned by a gigantic bee on the way to get experience point!", 
"负责取经验的机器人走夜路掉沟里了！ \nThe ExpBot drove into a ditch following GPS on the way to get experience point!"]
exp_phrase = [
"负责取经验的机器人接近超神了！ \nThe ExpBot is godlike!", 
"负责取经验的机器人的大刀已经饥渴难耐了！\nThe ExpBot readies its gigantic knive to reap off exp pt!", 
"负责取经验的机器人还有30秒到达战场！碾碎他们！\n30 seconds until ExpBot spawn! Crush them！"]
you_got_phrase = "这把操作您得到了{}点经验！\nThe last move got you {} exp point!"

def rand_command(update: Update, _: CallbackContext) -> None:
    x_exp = random.randrange(0, 210, 10)
    if x_exp == 0:
        update.message.reply_text(
            random.choice(zero_phrase) + "\n\n" + "这次仿佛没有拿到什么经验，下次好运点吧! \nNo experience pt given for this round, better luck next time!")
    else:
        update.message.reply_text(
            random.choice(exp_phrase) + "\n\n" + you_got_phrase.format(x_exp, x_exp)
            )

def add_dispatcher(dp):
    dp.add_handler(CommandHandler("rewards", rand_command))
    return []
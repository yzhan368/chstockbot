from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

<<<<<<< Updated upstream
vio_text = "举报信息"

def report_command(update: Update, _: CallbackContext) -> None:
    if update.message.reply_to_message != None:     #检查举报命令否为回复信息
        if update.message.reply_to_message.text == None:    #检查被举报的信息内容是否为文本信息
            vio_text = "非文本信息" #若被举报信息不含文本则定义举报内容为非文本信息                         
        else:                
            vio_text = update.message.reply_to_message.text #赋值被举报信息
            bot_reply = "User 用户: " + update.message.from_user.full_name + " ID: " + str(update.message.from_user.id) + " Reported 举报了\nUser 用户: " + update.message.reply_to_message.from_user.full_name + " ID: " + str(update.message.reply_to_message.from_user.id) + "\nReported Content 被举报内容:\n" + vio_text
            update.message.reply_text(bot_reply)
    else:   #提示举报命令需要回复另一条信息
        update.message.reply_text("To submit a report, please reply to the message in violation of our policy and type /r in text body" + "\n若举报违规行为，请回复违规信息并在回复信息中键入 /r")

def add_dispatcher(dp):
    dp.add_handler(CommandHandler("r", report_command))
    return []

=======
def rewards(update: Update, _: CallbackContext) -> None:
    """rewards the user message."""
    update.message.reply_text(update.message.text)
    print(update)

def ticker_command(update: Update, _: CallbackContext) -> None:
    update.message.chat.id == -1001478922081
    update.message.reply_text("Welcome to the Game")
    
def random_command(update: Update, _: CallbackContext) -> None:
    import random
    print(random.randrange(1,200))

def ShowMeId_command(update: Update, _: CallbackContext) -> None:
    update.message.reply_text(update.message.chat.id)

def add_dispatcher(dp):
    dp.add_handler(CommandHandler("rewards", ticker_command))
    dp.add_handler(CommandHandler("ShowMeId", ShowMeId_command))
    dp.add_handler(CommandHandler("random", random_command))
    return []


>>>>>>> Stashed changes

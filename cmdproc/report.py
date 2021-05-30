from telegram import Update, ForceReply, error, BotCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re

AdminGroupId = -1001409640737
KickGroupIdList = [-1001478922081, -1001409640737]

"""for i in KickGroupIdList:
    print(i)"""
        

def report_command(update: Update, _: CallbackContext) -> None:
    vio_text = "举报信息"
    ReporteeMsg = update.message.reply_to_message
    ReporterMsg = update.message
    if ReporteeMsg == None: #提示举报命令需要回复另一条信息
        ReporterMsg.reply_text("To submit a report, please reply to the message in violation of our policy and type /r in text body" + "\n若举报违规行为，请回复违规信息并在回复信息中键入 /r")
    else:
        Reporter = update.message.from_user
        Reportee = update.message.reply_to_message.from_user

        if ReporteeMsg.text == None:    #检查被举报的信息内容是否为文本信息
            vio_text = "非文本信息" #若被举报信息不含文本则定义举报内容为非文本信息                         
        else:                
            vio_text = update.message.reply_to_message.text #赋值被举报信息
            #搭建举报信息文本:
        bot_reply = f"""
User 用户: {Reporter.full_name} ID: {Reporter.id} 举报了
User 用户: {Reportee.full_name} ID: {Reportee.id}
Reported Content 被举报内容:
{vio_text}"""
        ReporterMsg.bot.send_message(AdminGroupId, bot_reply) #向管理群发送举报通知
            
def kick_reportee_command(update: Update, _: CallbackContext) -> None:
    if update.message.reply_to_message == None:
        update.message.reply_text("reply to bot reporting message to kick reporter/reportee")
    else:
        MsgStr = update.message.reply_to_message.text
        ReporteeID = MsgStr.split("\n")[1].split(" ID: ")[-1]
        ReporterID = MsgStr.split("\n")[0].split(" ID: ")[-1].split(" 举报了")[0]
        for i in KickGroupIdList:
            try:
                if (update.message.bot.kick_chat_member(i, ReporteeID)):
                    update.message.reply_text("用户 ID: " + format(ReporteeID) + "从群 " + format(i) + "中走远了...")
            except error.BadRequest as err:
                ErrRly = f"""
试图将用户：{ReporteeID} 从群: {i} 中踢出失败！原因:
{err.message}"""
                update.message.reply_text(ErrRly)    

def kick_reporter_command(update: Update, _: CallbackContext) -> None:
    if update.message.reply_to_message == None:
        update.message.reply_text("reply to bot reporting message to kick reporter/reportee")
    else:
        MsgStr = update.message.reply_to_message.text
        ReporteeID = MsgStr.split("\n")[1].split(" ID: ")[-1]
        ReporterID = MsgStr.split("\n")[0].split(" ID: ")[-1].split(" 举报了")[0]
        for i in KickGroupIdList:
            try:
                if (update.message.bot.kick_chat_member(i, ReporterID)):
                    update.message.reply_text("用户 ID: " + format(ReporterID) + "从群 " + format(i) + "中走远了...")
            except error.BadRequest as err:
                ErrRly = f"""
试图将用户：{ReporterID} 从群: {i} 中踢出失败！原因:
{err.message}"""
                update.message.reply_text(ErrRly)    

def add_dispatcher(dp):
    dp.add_handler(CommandHandler("r", report_command))
    return [BotCommand('r','举报一个对话')]

def add_kk(dp):
    dp.add_handler(CommandHandler("kr", kick_reportee_command))
    return [BotCommand('kr','🦶被举报者出群！')]

def add_kr(dp):
    dp.add_handler(CommandHandler("kk", kick_reporter_command))
    return [BotCommand('kk', '🦶举报者出群！')]

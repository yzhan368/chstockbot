from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import re

AdminGroupId = -1001448969389
KickGroupIdList = [-1001448969389, -1001358628526]

for i in KickGroupIdList:
    print(i)
                

"""上节课的report command
def report_command(update: Update, _: CallbackContext) -> None:
    ReporteeMsg = update.message.reply_to_message
    ReporterMsg = update.message

    if update.message.reply_to_message != None:     #检查举报命令否为回复信息
        if update.message.reply_to_message.text == None:    #检查被举报的信息内容是否为文本信息
            vio_text = "非文本信息" #若被举报信息不含文本则定义举报内容为非文本信息                         
        else:                
            vio_text = update.message.reply_to_message.text #赋值被举报信息
        bot_reply = "User 用户: " + update.message.from_user.full_name + " ID: " + str(update.message.from_user.id) + " Reported 举报了\nUser 用户: " + update.message.reply_to_message.from_user.full_name + " ID: " + str(update.message.reply_to_message.from_user.id) + "\nReported Content 被举报内容:\n" + vio_text
        update.message.reply_text(bot_reply)
    else:   #提示举报命令需要回复另一条信息
        update.message.reply_text("To submit a report, please reply to the message in violation of our policy and type /r in text body" + "\n若举报违规行为，请回复违规信息并在回复信息中键入 /r")
"""

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
        ReportList = re.findall(r'ID: \b\d+\b', update.message.reply_to_message.text) #从bot发的举报通知里找出[ID:xxxx, ID:xxxx]的举报人和被举报人ID的string list
        if len(ReportList) != 2:
            update.message.reply_text("failed to extract user ID to kick")
        else:
            ReporteeKickIdStr = re.findall(r'\b\d+\b', ReportList[1]) #把字符串"ID:"从被举报人的ID string里去掉
            ReporteeKickId = ReporteeKickIdStr.pop() #从List中获得单项ID
            print(type(ReporteeKickId), ReporteeKickId)
            for i in KickGroupIdList:
                update.message.bot.kick_chat_member(i, ReporteeKickId) #从群列表中依次踢出被举报人

def kick_reporter_command(update: Update, _: CallbackContext) -> None:
    if update.message.reply_to_message == None:
        update.message.reply_text("reply to bot reporting message to kick reporter/reportee")
    else:
        ReportList = re.findall(r'ID: \b\d+\b', update.message.reply_to_message.text) #从bot发的举报通知里找出[ID:xxxx, ID:xxxx]举报人和被举报人ID的string list
        if len(ReportList) != 2:
            update.message.reply_text("failed to extract user ID to kick")
        else:
            ReporterKickIdStr = re.findall(r'\b\d+\b', ReportList[0]) #把字符串"ID:"从举报人的ID string里去掉
            ReporterKickId = ReporterKickIdStr.pop() #从List中获得单项ID
            print(type(ReporterKickId), ReporterKickId)
            for i in KickGroupIdList:
                update.message.bot.kick_chat_member(i, ReporterKickId) #从群列表中依次踢出举报人
           
def add_dispatcher(dp):
    dp.add_handler(CommandHandler("r", report_command))
    return []

def add_kk(dp):
    dp.add_handler(CommandHandler("kr", kick_reportee_command))
    return []

def add_kr(dp):
    dp.add_handler(CommandHandler("kk", kick_reporter_command))
    return []
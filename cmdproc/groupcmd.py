from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def group_command(update: Update, _: CallbackContext) -> None:
    print(update)
    update.message.reply_text("our group ID is: " + format(update.message.chat.id) + " and our group contains " + format(update.message.chat.get_members_count()) + "  members")

def add_dispatcher(dp):
    dp.add_handler(CommandHandler("group", group_command))
    return []

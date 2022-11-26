import os
import cv2
from telegram import bot
import requests
import Constraints as keys
from telegram.ext import *
import Responses as R

print('Bot Started....')

def start_command(update, context):
    update.message.reply_text('type something to start !')


def help_command(update, context):
    update.message.reply_text('if you need help try asking google !')


def handle_message(update, context):
    text = str(update.message.text).lower()
    print(text)
    response = R.sample_responses(text)
    update.message.reply_text(response)


def error(update, context):
    update.message.reply_text("sorry i don't know its meaning, try a different word")
    print(f"Update{update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()

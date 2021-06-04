import os
import telegram
import responses as r
from telegram.ext import *

global bot
TOKEN = os.environ['key']
bot = telegram.Bot(TOKEN)

PORT = int(os.environ.get('PORT', 8282))

def start(update, context):
    user_name = update.message.from_user
    update.message.reply_text('Hey! {}  This Bot Help You To Check The Status Of Website, Check /help For Input Syntax'.format(user_name['username']))

def help(update, context):
    update.message.reply_text('Type Your Website Name Like example.com')

def handle_messagehost(update, context):
    user_text = str(update.message.text)
    text = str(user_text).lower()
    response = r.sitestatus_responses(text)
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))

    dp.add_handler(MessageHandler(Filters.text, handle_messagehost))

    updater.start_webhook(listen="0.0.0.0",
                       port=int(PORT),
                       url_path=TOKEN,
                       webhook_url='https://isitdown-telegram-bot.herokuapp.com/' + TOKEN)

    updater.idle()

main()

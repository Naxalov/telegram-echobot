from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN = os.environ['TOKEN']


def echo(update, context):
	bot = context.bot
	text = update.message.text
	chat_id = update.message.chat.id
	print(text)
	update.message.reply_text(text)


def start(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'Welcome to our bot')


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))


updater.start_polling()
updater.idle()
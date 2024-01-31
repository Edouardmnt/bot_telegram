import telebot
import json
import os.path
from main import combineAllJson

combineAllJson()


Api_key = "6872663741:AAGVoeIJtnaGoOp_MB7MCaSNFgYA2myNc3I"

bot = telebot.TeleBot(Api_key)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "hello")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message,'ca va ? ')

bot.infinity_polling()

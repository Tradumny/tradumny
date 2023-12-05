import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.BOT_API)

@bot.message_handler(commands=['start'])
def handle_start (message):
    bot.send_message(message.chat.id, "иди нахуй чурка нерусский")
    
bot.polling() 
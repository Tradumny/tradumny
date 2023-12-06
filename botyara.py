import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.BOT_API)

@bot.message_handler(commands=['start'])
def handle_start (message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('12-18', callback_data='/gfg')
    item2 = types.InlineKeyboardButton('18-45', callback_data='/dfg')
    markup.add(item, item2)
    bot.send_message(message.chat.id, 'Привет! Сколько тебе лет?', reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == '/gfg':
            markup2 = types.InlineKeyboardMarkup(row_width=3)
            item3 = types.InlineKeyboardButton('40-50', callback_data='/dfg1')
            item4 = types.InlineKeyboardButton('50-70', callback_data='/dfg2')
            item5 = types.InlineKeyboardButton('70-100', callback_data='/dfg3')
            markup2.add(item3, item4, item5)
            bot.send_message(call.message.chat.id, 'Отлично, сколько вы весите?', reply_markup=markup2)
        elif call.data == '/dfg':
            bot.send_message(call.message.chat.id, 'Отлично, сколько вы весите?')
            markup2 = types.InlineKeyboardMarkup(row_width=3)
            item3 = types.InlineKeyboardButton('40-50', callback_data='/dfg1')
            item4 = types.InlineKeyboardButton('50-70', callback_data='/dfg2')
            item5 = types.InlineKeyboardButton('70-100', callback_data='/dfg3')
            markup2.add(item3, item4, item5)
            bot.send_message(call.message.chat.id, 'Отлично, сколько вы весите?', reply_markup=markup2)

bot.polling()
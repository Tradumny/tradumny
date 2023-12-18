import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.BOT_API)

@bot.message_handler(commands=['start'])
def handle_start (message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item = types.InlineKeyboardButton('12-18', callback_data='/gfg')
    item2 = types.InlineKeyboardButton('19-45', callback_data='/dfg')
    markup.add(item, item2)
    bot.send_message(message.chat.id, 'Привет! Сколько тебе лет?', reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == '/gfg':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item3 = types.InlineKeyboardButton('40-50', callback_data='/gfg1')
            item4 = types.InlineKeyboardButton('50-70', callback_data='/gfg2')
            item5 = types.InlineKeyboardButton('70-100', callback_data='/gfg3')
            markup.add(item3, item4, item5)
            bot.send_message(call.message.chat.id, 'Отлично, сколько вы весите?', reply_markup=markup)
        elif call.data == '/dfg':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item6 = types.InlineKeyboardButton('40-50', callback_data='/dfg1')
            item7 = types.InlineKeyboardButton('50-70', callback_data='/dfg2')
            item8 = types.InlineKeyboardButton('70-100', callback_data='/dfg3')
            markup.add(item6, item7, item8)
            bot.send_message(call.message.chat.id, 'Отлично, сколько вы весите?', reply_markup=markup)
        elif call.data == '/gfg1':
            bot.send_message(call.message.chat.id, 'Вам нужно съедать по 1600 каллорий в день, вот ваше меню: Завтрак - Яичница из трёх яиц. Обед - Суп чечевичный с индейкой и гречанники. Ужин - Морской окунь со стручковой фасолью и салат с фасолью')
        elif call.data == '/gfg2':
            bot.send_message(call.message.chat.id, 'Вам нужно съедать по 1725 каллорий в день, вот ваше меню: Завтрак - Кофе со сгущенным молоком. Ланч - Испанская тортилья. Обед - Сырно-кукурузный суп. Полдник - Арбуз. Ужин - Мясной салат «Мельник»')
        elif call.data == '/gfg3':
              bot.send_message(call.message.chat.id, 'Вам нужно съедать по 2000 каллорий в день, вот ваше меню: Завтрак - Овсяная каша. Ланч - Тост из куриного филе + Апельсин + Маленький сок мультифрукт. Обед - Овощной суп с добавлением 150 граммов отварного куриного мяса. Полдник - 200 грамм творого + 100 грамм свежей клубники. Ужин - 200 грамм куриного филе и запеченого картофеля')
        elif call.data == '/dfg1':
            bot.send_message(call.message.chat.id, 'Вам нужно съедать по 1430 каллорий в день, вот ваше меню: Завтрак - Пшенка со сливочным маслом и стружкой кокоса + Капучино 250мл. Обед - Гречка с овощами 250 гр + мясной хлеб из грудки 300 гр + груша. Ужин - Корюжка в духовке - 250гр')
        elif call.data == '/dfg2':
            bot.send_message(call.message.chat.id, 'Вам нужно съедать по 1650 каллорий в день, вот ваше меню: Завтрак - Омлет с сыром. Ланч - Яблоко 250гр + Тёмный шоколад 2 кусочка. Обед - Запеченное куриное филе 100гр + Рис бурый 200гр. Полдник - Йогурт 150 г. Ужин - Салат с курицей (Куриное филе 100гр + Овощи 200гр)')
        elif call.data == '/dfg3':
             bot.send_message(call.message.chat.id, 'Вам нужно съедать по 1900 каллорий в день, вот ваше меню: Завтрак - Варенники с творогом 250гр + Сметана 15% 20гр. Обед - Шницель в капустных листах + Жареный картофель с луком + салат овощной (Помидор + Огурец + Укроп + Яйцо куриное отварное). Полдник - 2 шницеля в капустных листах + Салат овощной (2 Помидора + Огурец + Укроп). Ужин - 200 грамм куриного филе и запеченого картофеля')
       

bot.polling()
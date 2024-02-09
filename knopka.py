import telebot
from telebot import types

bot = telebot.TeleBot('6444346585:AAHHgp8QYbZbfeRh_sEgvtIP_tPp1C7UWvw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Саламдашуу')
    btn2 = types.KeyboardButton('Суроо беруу')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Кнопкаларды басыныз", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == 'Саламдашуу'):
        bot.send_message(message.chat.id,
                         text='Кош келдиниз, бул БОТ сизди швеянын ичиндеги жумуш оорудары мн камсыздайт')
    elif (message.text == 'Суроо беруу'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сени ким тузду')
        btn2 = types.KeyboardButton('Сен эмне кыла аласын?')
        btn3 = types.KeyboardButton('Башкы бетке чыгуу')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Суроо танданыз", reply_markup=markup)
    elif (message.text == 'Сени ким тузду'):
        bot.send_message(message.chat.id, "Мени тузгон\nАты: Аскат\ntelegram: @askochiik")

    elif message.text == 'Сен эмне кыла аласын?':
        bot.send_message(message.chat.id, 'Мен швеяда иштеген адамдардын тизмесин коргозо алам')
        markup_inline = types.InlineKeyboardMarkup()
        item_yes = types.InlineKeyboardButton(text='Ооба', callback_data='yes')
        item_no = types.InlineKeyboardButton(text='Жок', callback_data='no')
        markup_inline.row(item_yes, item_no)
        bot.send_message(message.chat.id, text='Сизге швеялардын тизмегин коргозойунбу?', reply_markup=markup_inline)

    elif message.text == 'Башкы бетке чыгуу':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton('Саламдашуу')
        bt2 = types.KeyboardButton('Суроо беруу')
        mark.add(bt1, bt2)
        bot.send_message(message.chat.id, text="Сиз башкы менюдасыз", reply_markup=mark)
    else:
        bot.send_message(message.chat.id, text='Сураныч кнопкалар менен иштениз')


@bot.callback_query_handler(func=lambda call: True)
def cal_inline(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, 'Выберите виды работ из списка')
        markup_inline = types.InlineKeyboardMarkup()

        averlok = types.InlineKeyboardButton('Оверлок', callback_data='averlok')
        photo = types.InlineKeyboardButton('photo', callback_data='phot')
        pitlya = types.InlineKeyboardButton('Петля', callback_data='pitlya')
        topchu_mac = types.InlineKeyboardButton('Топчу кадочу машина', callback_data='topchu_mac')

        markup_inline.row(averlok, pitlya, topchu_mac, photo)
        bot.send_message(call.message.chat.id, text='Сиз кандай виде иштиген?', reply_markup=markup_inline)

        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Ойлонуп коруп кайра келиниз')
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    elif call.data == 'averlok':
        bot.send_message(call.message.chat.id, 'Аверлок описание:\n 7кун иштеп 7 кун бош зп:5000🙀🙀🙀')
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    elif call.data == 'pitlya':
        bot.send_message(call.message.chat.id, 'Петля описание:\n 15кун иштеп 10 кун бош зп:15000💀💀💀')
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    elif call.data == 'topchu_mac':
        bot.send_message(call.message.chat.id, 'Топчу:\n 3кун иштеп 3 кун бош зп:3000😎😎😎')
    elif call.data == 'phot':
        ms = open('med/cat.jpeg', 'rb')
        bot.send_photo(call.message.chat.id, ms)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)


bot.polling(none_stop=True)
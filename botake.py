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

        hide_button = types.InlineKeyboardButton('Hide', callback_data='hide')
        markup_inline.row(hide_button)

        bot.send_message(call.message.chat.id, text='Сиз кандай виде иштиген?', reply_markup=markup_inline)
    elif call.data == 'hide':
        # Hide the inline keyboard
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Ойлонуп коруп кайра келиниз')
    elif call.data == 'averlok':
        bot.send_message(call.message.chat.id, 'Аверлок описание:\n 7кун иштеп 7 кун бош зп:5000🙀🙀🙀')
    elif call.data == 'pitlya':
        bot.send_message(call.message.chat.id, 'Петля описание:\n 15кун иштеп 10 кун бош зп:15000💀💀💀')
    elif call.data == 'topchu_mac':
        bot.send_message(call.message.chat.id, 'Топчу:\n 3кун иштеп 3 кун бош зп:3000😎😎😎')
    elif call.data == 'phot':
        ms = open('med/cat.jpeg', 'rb')
        bot.send_photo(call.message.chat.id, ms)


bot.polling(none_stop=True)
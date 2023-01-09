from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#Меню
btn_menu_uz = KeyboardButton("Boshiga🏠")
btn_menu_ru = KeyboardButton("Главное меню🏠")
#Меню

#Узбекское Основное
button_0 = KeyboardButton("Gold Pass🎖")
button_1 = KeyboardButton("Gold🍯")
button_2 = KeyboardButton('Akkauntlar🔥')
button_3 = KeyboardButton('Gruppamiz💬')
button_4 = KeyboardButton('Otzivlar📊')
buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons.row(button_1, button_0).row(button_2, button_3).add(button_4)
#Узбекское Основное

#Узбекское Купить или продать
button_buy = KeyboardButton("Sotib olish📈")
button_sell = KeyboardButton("Sotish📉")
button_buy_sell = ReplyKeyboardMarkup(resize_keyboard=True).row(button_buy, button_sell).add(btn_menu_uz)
#Узбекское Купить или продать


#Узбекское Gold
btn_price_uz = KeyboardButton("Prays list📜")
btn_gold_uz = KeyboardButton('X Gold🍯 - nechi som boladi?')
btn_som_uz = KeyboardButton('X som💸 ga - nechi gold boladi?')
btn_all_uz = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn_all_uz.add(btn_price_uz).add(btn_gold_uz).add(btn_som_uz).add(btn_menu_uz)
#Узбекское Gold


################################################

#Русское Основное
button_1_rus = KeyboardButton("Купить голду🍯")
button_2_rus = KeyboardButton('Аккаунты🔥')
button_3_rus = KeyboardButton('Беседа💬')
button_4_rus = KeyboardButton('Отзывы📊')
buttons_rus = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons_rus.add(button_1_rus).row(button_2_rus, button_3_rus).add(button_4_rus)
#Русское Основное



#Инлайн
inline_uz = InlineKeyboardButton('UZ', callback_data='uz',)
inline_ru = InlineKeyboardButton('RU', callback_data='ru')
Inline_lang = InlineKeyboardMarkup().add(inline_uz, inline_ru)


link_button = InlineKeyboardButton(text = 'Sotib olish', url="https://t.me/jamshid_5878")
Inline_link = InlineKeyboardMarkup().add(link_button)


link_button_RU = InlineKeyboardButton(text = 'Купить', url="https://t.me/jamshid_5878")
inline_link_RU = InlineKeyboardMarkup().add(link_button_RU)


gr_button = InlineKeyboardButton(text = 'Gruppaga kirish', url="https://t.me/standoff2uzbchat")
button_gr = InlineKeyboardMarkup().add(gr_button)


gr_button_RU = InlineKeyboardButton(text = 'Вступить в групу', url="https://t.me/standoff2uzbchat")
button_gr_RU = InlineKeyboardMarkup().add(gr_button_RU)


but_1 = InlineKeyboardButton(text="1500+ Otziv", url='https://t.me/standoff2shopuzb')
but_2 = InlineKeyboardButton(text="200+ Otziv", url='https://t.me/standoff2shopuzbotzv')
buttons_otzv = InlineKeyboardMarkup().add(but_1).add(but_2)


but_3 = InlineKeyboardButton(text="1500+ Отзывов", url='https://t.me/standoff2shopuzb')
but_4 = InlineKeyboardButton(text="200+ Отзывов", url='https://t.me/standoff2shopuzbotzv')
buttons_otzv_RU = InlineKeyboardMarkup().add(but_3).add(but_4)


#Назад
button_6 = KeyboardButton("Bekor qilish❌")
button_back = ReplyKeyboardMarkup(resize_keyboard=True).add(button_6)

button_7 = KeyboardButton("Отмена❌")
button_back_RU = ReplyKeyboardMarkup(resize_keyboard=True).add(button_7)

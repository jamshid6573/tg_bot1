from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#Меню
btn_menu_uz = KeyboardButton("Boshiga🏠")
btn_menu_ru = KeyboardButton("Главное меню🏠")
btn_boshiga = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_menu_uz)
btn_boshiga_ru = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_menu_ru)
#Меню

#Узбекское Основное
button_0 = KeyboardButton("Gold Pass🎖")
button_1 = KeyboardButton("Gold🍯")
button_2 = KeyboardButton('Akkauntlar🔥')
button_3 = KeyboardButton('Gruppamiz💬')
button_4 = KeyboardButton('Otzivlar📊')
buttons = ReplyKeyboardMarkup(resize_keyboard=True)
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


#Узбекское Аккаунт
btn1 = KeyboardButton("Sotmoqchiman📉")
btn2 = KeyboardButton("Sotib olmoqchiman📈")
btn_acc_uz = ReplyKeyboardMarkup(resize_keyboard=True).row(btn1, btn2).add(btn_menu_uz)

btn3 = InlineKeyboardButton('HA✔️', callback_data="ha")
btn_ha = InlineKeyboardMarkup().add(btn3)
#Узбекское Аккаунт

#Русское Аккаунт
btn1_ru = KeyboardButton("Хочу продать📉")
btn2_ru = KeyboardButton("Хочу купить📈")
btn_acc_ru = ReplyKeyboardMarkup(resize_keyboard=True).row(btn1_ru, btn2_ru).add(btn_menu_ru)

btn3_ru = InlineKeyboardButton('ДА✔️', callback_data="да")
btn_ha_ru = InlineKeyboardMarkup().add(btn3_ru)
#Русское Аккаунт


################################################

#Русское Основное
button_0_rus = KeyboardButton("Голд Пасс🎖")
button_1_rus = KeyboardButton("Голд🍯")
button_2_rus = KeyboardButton('Аккаунты🔥')
button_3_rus = KeyboardButton('Беседа💬')
button_4_rus = KeyboardButton('Отзывы📊')
buttons_rus = ReplyKeyboardMarkup(resize_keyboard=True)
buttons_rus.row(button_1_rus, button_0_rus).row(button_2_rus, button_3_rus).add(button_4_rus)
#Русское Основное

#Русское Купить или продать
button_buy_ru = KeyboardButton("Купить📈")
button_sell_ru = KeyboardButton("Продать📉")
button_buy_sell_ru = ReplyKeyboardMarkup(resize_keyboard=True).row(button_buy_ru, button_sell_ru).add(btn_menu_ru)
#Русское Купить или продать

#Узбекское Gold
btn_price_ru = KeyboardButton("Прайс лист📜")
btn_gold_ru = KeyboardButton('Сколько будет стоить Х-Голды🍯')
btn_som_ru = KeyboardButton('Сколько голды будет на Х сум💸')
btn_all_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn_all_ru.add(btn_price_ru).add(btn_gold_ru).add(btn_som_ru).add(btn_menu_ru)
#Узбекское Gold



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


gr_button_RU = InlineKeyboardButton(text = 'Присоединиться к беседе', url="https://t.me/standoff2uzbchat")
button_gr_RU = InlineKeyboardMarkup().add(gr_button_RU)


but_1 = InlineKeyboardButton(text="2000+ Otziv", url='https://t.me/standoff2shopuzb')
but_2 = InlineKeyboardButton(text="500+ Otziv", url='https://t.me/standoff2shopuzbotzv')
buttons_otzv = InlineKeyboardMarkup().row(but_1, but_2)


but_3 = InlineKeyboardButton(text="1500+ Отзывов", url='https://t.me/standoff2shopuzb')
but_4 = InlineKeyboardButton(text="500+ Отзывов", url='https://t.me/standoff2shopuzbotzv')
buttons_otzv_RU = InlineKeyboardMarkup().add(but_3).add(but_4)

btn_4 = InlineKeyboardButton(text='Jonatish📥', url='https://t.me/jamshid_5878')
btn_send = InlineKeyboardMarkup().add(btn_4)

btn_6 = InlineKeyboardButton(text='Отправить📥', url='https://t.me/jamshid_5878')
btn_send_ru = InlineKeyboardMarkup().add(btn_6)

btn_5 = InlineKeyboardButton(text='Kanalga kirish⬅️', url='https://t.me/standoff2akkauntbozor')
btn_kirish = InlineKeyboardMarkup().add(btn_5)

btn_5_ru = InlineKeyboardButton(text='Присоединиться на канал⬅️', url='https://t.me/standoff2akkauntbozor')
btn_kirish_ru = InlineKeyboardMarkup().add(btn_5_ru)


#Назад
button_6 = KeyboardButton("Bekor qilish❌")
button_back = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_6)

button_7 = KeyboardButton("Отмена❌")
button_back_RU = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_7)

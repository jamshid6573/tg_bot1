from aiogram import Dispatcher
from aiogram import types
from tgbot.keyboards.inline import *
from aiogram import Bot
from tgbot.misc.states import FSMrus, FSMuz, FSMsom, FSMsomRU
from aiogram.dispatcher import FSMContext
from functions.func import get_info_sum, get_info, sum_correct, info

bot = Bot(token='5226272322:AAEZsPMW68-W9Hx7UkmtfkA-qUI1A9NTrQw', parse_mode='HTML')
#5226272322:AAEZsPMW68-W9Hx7UkmtfkA-qUI1A9NTrQw

async def user_start(message: types.Message):
    global start_
    start_ = await message.reply(f'👋🏻Salom {message.from_user.first_name}, bot ga hush kelibsiz, tilni tanlang. \n \n👋🏻Привет {message.from_user.first_name}, добро пожалововать в бот, выберите язык.', reply_markup=Inline_lang)


#Узб язык
async def uzb(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    if start_:
        await start_.delete()    
        await bot.send_message(call.from_user.id, "Uzbek tili tanlandi!", reply_markup=buttons)
    else:
        await bot.send_message(call.from_user.id, "Uzbek tili tanlandi!", reply_markup=buttons)

async def gold_uz(message: types.Message):
    await message.answer("Operatsiyani tanlang:", reply_markup = btn_all_uz)

#GOLD PASS
async def goldpass(message: types.Message):
    await message.answer(f'''
        Season 5 Gold Pass

Gold Pass - 119.000 som

+1 - 15.000 som
+10 - 45.000 som
+25 - 259.000 som
+75 - 629.000 som

Sizgan faqatkina ID va NIK kerak boladi🤝

❗️Sotib olish uchun @jamshid_5878 ga Tolov cheki bilan ID va NIK tashlaysiz.
    ''', reply_markup=Inline_link)
    await message.answer("💳Tolov usullari: \nhttps://t.me/jamacards", reply_markup=buttons)
#GOLD PASS

async def gold_buy_sell(message: types.Message):
    await message.answer("Operatsiyani tanlang:", reply_markup=button_buy_sell)

async def menu_uz(message: types.Message):
    await message.answer('Bosh sahifaga qaytdingiz✔️', reply_markup=buttons)

async def price_uz(message: types.Message):
    await message.answer(f'📉1G dan 999G gacha - 1G={info["1g"]} som \n\n📉1000G dan 2999G gacha - 1G={info["1000g"]} som \n\n📉3000G dan ∞ gacha - 1G={info["3000g"]} som', reply_markup = btn_all_uz)

#GOLD SOTISH
async def gold_sell(message: types.Message):
    await message.answer('Goldingizni sotmoqchimisiz?🤔 \n \n@jamshid_5878 - bilan boglaning, yaxshi narhda sotib olamiz😉')
#GOLD SOTISH

# FSM GOLD UZ
async def gold_start_uz(message: types.Message):
    await message.answer('⬇️Gold sonini kiriting:', reply_markup=button_back)
    await FSMuz.gold.set()

async def gold_stop_uz(message: types.Message, state: FSMContext):
    text1 = message.text
    if text1.isnumeric():
        gold = int(text1)
        if gold > 99 and gold < 1000000:
            info = get_info(gold)
            price = info['price']
            commission = info['commission']
            main_som = sum_correct(price)
            skin = open("media/skin.jpg", 'rb')
            await bot.send_photo(message.from_user.id, skin, caption=f'{gold} Gold🍯 - {main_som} som boladi.\n \n ❗️Sotib olish uchun - Graffiti "Explosion Warning" ni  {commission} ga qoyib, @jamshid_5878 ga skrinwot jonating!', reply_markup=Inline_link)
            skin.close()
            await message.answer("💳Tolov usullari: \nhttps://t.me/jamacards", reply_markup=buttons)
            await bot.send_message(-1001666478836, f'Klient:  @{message.from_user.username}\nGold: {gold}  \nNarhi: {sum_correct(price)} som \nKomissiya: {commission} ')
            await state.finish()
        elif gold < 99:
            await message.answer('Minimum 100 GOLD❗️', reply_markup=button_back)
        elif gold > 1000000:
            await message.answer('Oyin qimen, puliz yetmidi😂🤣', reply_markup=button_back)
    elif message.text == "Bekor qilish❌":
        await message.answer('Bekor qilindi✔️', reply_markup=buttons)
        await state.finish()
    else:
        await message.answer("🛑Hato! Iltimos butun son kiriting! \n Harflar va simvollar bolmasligi kerak!")
# FSM GOLD UZ


# FSM SOM UZ
async def som_start_uz(message: types.Message):
    await message.answer('⬇️Pul sonini kiriting:', reply_markup=button_back)
    await FSMsom.som.set()

async def som_stop_uz(message: types.Message, state: FSMContext):
    text1 = message.text
    if text1.isnumeric():
        som = int(text1)
        if som > 16999 and som < 9999999:
            info = get_info_sum(som)
            gold = info['gold']
            commission = info['commission']
            main_som = sum_correct(som)
            skin = open("media/skin.jpg", 'rb')
            await bot.send_photo(message.from_user.id, skin, caption=f'{main_som} som ga {gold} Gold🍯 boladi. \n \n  ❗️Sotib olish uchun - Graffiti "Explosion Warning" ni  {commission} ga qoyib, @jamshid_5878 ga skrinwot jonating!', reply_markup=Inline_link)
            skin.close()
            await message.answer("💳Tolov usullari: \nhttps://t.me/jamacards", reply_markup=buttons)
            await bot.send_message(-1001666478836, f'Klient:  @{message.from_user.username}\nGold: {gold}  \nNarhi: {sum_correct(som)} som \nKomissiya: {commission} ')
            await state.finish()
        elif som < 16999:
            info_100 = get_info(100)
            minimum = info_100['price']
            await message.answer(f'Minimum {sum_correct(minimum)} som❗️', reply_markup=button_back)
        elif som > 10000000:
            await message.answer('Oyin qimen, buncha puliz yoq😂🤣', reply_markup=button_back)
    elif message.text == "Bekor qilish❌":
        await message.answer('Bekor qilindi✔️', reply_markup=buttons)
        await state.finish()
    else:
        await message.answer("🛑Hato! Iltimos butun son kiriting! \n Harflar va simvollar bolmasligi kerak!")
# FSM SOM UZ


#Akkaunt UZ
async def account_uz(message: types.Message):
    await message.answer("Sotmoqchimisiz yoki sotib olmoqchimisiz?", reply_markup=btn_acc_uz)

async def account_sell(message: types.Message):
    await message.answer("Akkaunt sotish togrisidagi eloningiz:\n @standoff2akkauntbozor kanaliga joylashtiliradi!", reply_markup=btn_boshiga)
    await message.answer("https://t.me/standoff2akkauntbozor")
    await message.answer("Davom etamizmi?", reply_markup=btn_ha)

async def account_sell2(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, """❗️Diqqat akkaunt sotiladi: 

📊Level: 
🏅Medal:
🔫Avtomat skinlar: 
🔪Pichoq:
🔥Gold:
📋Qoshimcha malumot:
💰Narxi: 
📌Qolgan malumotlar skriwnotlarda!

👤Akkaunt egasi: 

➖➖➖➖➖➖➖➖➖➖➖➖

‼️Mowenniklar dan extiyot boling - Adminsiz savdo qila kormang, adminsiz qilingan savdoga admin javobgar bolmaydi‼️

➖➖➖➖➖➖➖➖➖➖➖➖

➡️Kanal: @standoff2akkauntbozor
☑️Asosiy kanal: @standoff2shopuzb
👤Admin: @jamshid_5878✅
🤖Bot: @Standoff2Uzb_Shop_bot""")

    await bot.send_message(call.from_user.id, "⬆️Tepadagi anketani toldirib, skrinwotlari bilan - @jamshid_5878 ga jonating.", reply_markup=btn_send)

async def account_buy(message: types.Message):
    await message.answer('https://t.me/standoff2akkauntbozor', reply_markup=btn_boshiga)
    await message.answer('@standoff2akkauntbozor kanalida ozingizga kerakli akkauntni topishingiz mumkin😊 \n \n‼️Mowenniklar dan extiyot boling - Adminsiz aslo savdo qila kormang, adminsiz qilingan savdoga admin javobgar bolmaydi‼️', reply_markup=btn_kirish)

#Akkaunt UZ

#OTZV
async def otzv(message: types.Message):
    await message.answer("Marhamat😊 \nTanishib chiqishingiz mumkin!", reply_markup=buttons_otzv)
#OTZV

async def gr(message: types.Message):
    await message.reply("Gruppada reklama va sokinish taqiqlanadi!🚫 \nOzingizni yaxshi tuting!", reply_markup=button_gr)


#OTZV rus
async def otzv_ru(message: types.Message):
    await message.answer("Вот😊 \nМожете ознакомиться!", reply_markup=buttons_otzv_RU)
#OTZV rus

async def gr_ru(message: types.Message):
    await message.reply("В беседе строго запрещается реклама и мат!🚫 \nВведите себя адекватно!", reply_markup=button_gr_RU)

#Рус язык
async def rus(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await start_.delete()    
    await bot.send_message(call.from_user.id, "Выбран Русский язык!", reply_markup=buttons_rus)

async def gold_buy_sell_ru(message: types.Message):
    await message.answer("Выберите операцию:", reply_markup=button_buy_sell_ru)

async def gold_ru(message: types.Message):
    await message.answer("Выберите операцию:", reply_markup=btn_all_ru)

async def gold_sell_ru(message: types.Message):
    await message.answer('Хотите продать свою голду?🤔 \n \nНапишите нам ( @jamshid_5878 )! Купим вашу голду по хорошой цене😉')

async def price_ru(message: types.Message):
    await message.answer("📉От 1G до 999G - 1G=170 сум \n\n📉От 1000G до 2999G - 1G=166 сум \n\n📉От 3000 до ∞ - 1G=130 cум", reply_markup = btn_all_ru)

# FSM GOLD RU
async def gold_start_ru(message: types.Message):
    await message.answer('⬇️Введите количество голды:', reply_markup=button_back_RU)
    await FSMrus.gold.set()

async def gold_stop_ru(message: types.Message, state: FSMContext):
    text1 = message.text
    if text1.isnumeric():
        gold = int(text1)
        if gold > 99 and gold < 1000000:
            info = get_info(gold)
            price = info['price']
            commission = info['commission']
            main_som = sum_correct(price)
            skin = open("media/skin.jpg", 'rb')
            await bot.send_photo(message.from_user.id, skin, caption=f'{gold} GOLD🍯 - {main_som} cум.\n \n ❗️Чтобы купить голду - выставьте на продажу Graffiti "Explosion Warning" за {commission}, и отправьте скриншот сюда -> @jamshid_5878', reply_markup=inline_link_RU)
            skin.close()
            await message.answer("💳Способы оплаты: \nhttps://t.me/jamacards", reply_markup=buttons_rus)
            await bot.send_message(-1001666478836, f'Klient:  @{message.from_user.username}\nGold: {gold}  \nNarhi: {sum_correct(price)} som \nKomissiya: {commission} ')
            await state.finish()
        elif gold < 99:
            await message.answer('Минимум 100 GOLD❗️', reply_markup=button_back_RU)
        elif gold > 1000000:
            await message.answer('Слишком много, давайте без рофла!', reply_markup=button_back_RU)
    elif message.text == "Отмена❌":
        await message.answer('Успешно✔️', reply_markup=buttons_rus)
        await state.finish()
    else:
        await message.answer("🛑Ошибка! Введите целое число! \nБукв и символов не должно быть!")
# FSM GOLD RU


# FSM som uz
async def som_start_ru(message: types.Message):
    await message.answer('⬇️Введите сумму:', reply_markup=button_back_RU)
    await FSMsomRU.som.set()

async def som_stop_ru(message: types.Message, state: FSMContext):
    text1 = message.text
    if text1.isnumeric():
        som = int(text1)
        if som > 16999 and som < 9999999:
            info = get_info_sum(som)
            gold = info['gold']
            commission = info['commission']
            main_som = sum_correct(som)
            skin = open("media/skin.jpg", 'rb')
            await bot.send_photo(message.from_user.id, skin, caption=f'На {main_som} сум - {gold} GOLD🍯. \n \n  ❗️Чтобы купить голду - выставьте на продажу Graffiti "Explosion Warning" за {commission}, и отправьте скриншот сюда -> @jamshid_5878', reply_markup=inline_link_RU)
            skin.close()
            await message.answer("💳Способы оплаты: \nhttps://t.me/jamacards", reply_markup=buttons_rus)
            await bot.send_message(-1001666478836, f'Klient:  @{message.from_user.username}\nGold: {gold}  \nNarhi: {sum_correct(som)} som \nKomissiya: {commission} ')
            await state.finish()
        elif som < 16999:
            info_100 = get_info(100)
            minimum = info_100['price']
            await message.answer(f'Минимум {sum_correct(minimum)} сум❗️', reply_markup=button_back_RU)
        elif som > 10000000:
            await message.answer('Слишком много, давайте без рофла!', reply_markup=button_back_RU)
    elif message.text == "Отмена❌":
        await message.answer('Успешно✔️', reply_markup=buttons_rus)
        await state.finish()
    else:
        await message.answer("🛑Ошибка! Введите целое число! \nБукв и символов не должно быть!")
# FSM som uz

#Akkaunt ru
async def account_ru(message: types.Message):
    await message.answer("Хотите продать или купить?", reply_markup=btn_acc_ru)

async def account_sell_ru(message: types.Message):
    await message.answer("⬇️Ваше объявление о продаже аккаунта будет размещен на этот канал:", reply_markup=btn_boshiga_ru)
    await message.answer("https://t.me/standoff2akkauntbozor")
    await message.answer("Продолжим?", reply_markup=btn_ha_ru)

async def account_sell2_ru(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, """❗️Diqqat akkaunt sotiladi: 

📊Level: 
🏅Medal:
🔫Avtomat skinlar: 
🔪Pichoq:
🔥Gold:
📋Qoshimcha malumot:
💰Narxi: 
📌Qolgan malumotlar skriwnotlarda!

👤Akkaunt egasi: 

➖➖➖➖➖➖➖➖➖➖➖➖

‼️Mowenniklar dan extiyot boling - Adminsiz savdo qila kormang, adminsiz qilingan savdoga admin javobgar bolmaydi‼️

➖➖➖➖➖➖➖➖➖➖➖➖

➡️Kanal: @standoff2akkauntbozor
☑️Asosiy kanal: @standoff2shopuzb
👤Admin: @jamshid_5878✅
🤖Bot: @Standoff2Uzb_Shop_bot""")

    await bot.send_message(call.from_user.id, "⬆️Заполните данную анкету, прикрепите скриншоты или видео вашего акканта, и отправьте сюда -> @jamshid_5878", reply_markup=btn_send_ru)

async def account_buy_ru(message: types.Message):
    await message.answer('https://t.me/standoff2akkauntbozor', reply_markup=btn_boshiga_ru)
    await message.answer('⬆️На этом канале вы можете найти подходящий вам аккаунт и купить😊 \n \n‼️Остерегайтесь мошенников, не покупайте аккаунт на доверие продавца, пользуйтесь услугой ГАРАНТА \n\nГарант данного канала - @jamshid_5878 гарантирует вам 100% безопасную сделку.\nУслуга ГАРАНТА платная! ‼️', reply_markup=btn_kirish_ru)

#Akkaunt ru


#GOLD PASS
async def goldpass_ru(message: types.Message):
    await message.answer(f'''
        Season 5 Gold Pass

Gold Pass - 119.000 сум

+1 - 15.000 сум
+10 - 45.000 сум
+25 - 259.000 сум
+75 - 629.000 сум

От вас требуется только Айди и Ник🤝

❗️Чтобы купить отправьте скриншот оплаты(Чек), Айди и Ник сюда -> @jamshid_5878.
    ''', reply_markup=inline_link_RU)
    await message.answer("💳Способы оплаты: \nhttps://t.me/jamacards", reply_markup=buttons_rus)
    

async def menu_ru(message: types.Message):
    await message.answer('Вы вернулись в главное меню✔️', reply_markup=buttons_rus)
#GOLD PASS

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_callback_query_handler(uzb, text="uz")
    dp.register_callback_query_handler(rus, text="ru")
    dp.register_message_handler(gold_buy_sell, text="Gold🍯")
    dp.register_message_handler(goldpass, text="Gold Pass🎖")
    dp.register_message_handler(gold_uz, text="Sotib olish📈")
    dp.register_message_handler(gold_sell, text="Sotish📉")
    dp.register_message_handler(menu_uz, text="Boshiga🏠")
    dp.register_message_handler(price_uz, text="Prays list📜")
    dp.register_message_handler(gold_start_uz, text='X Gold🍯 - nechi som boladi?')
    dp.register_message_handler(gold_stop_uz, state=FSMuz.gold)
    dp.register_message_handler(som_start_uz, text='X som💸 ga - nechi gold boladi?')
    dp.register_message_handler(som_stop_uz, state=FSMsom.som)
    dp.register_message_handler(account_uz, text='Akkauntlar🔥')
    dp.register_message_handler(account_sell, text="Sotmoqchiman📉")
    dp.register_callback_query_handler(account_sell2, text='ha')
    dp.register_message_handler(account_buy, text="Sotib olmoqchiman📈")
    dp.register_message_handler(gr, text='Gruppamiz💬')
    dp.register_message_handler(otzv, text="Otzivlar📊")
    #Русский язык
    dp.register_message_handler(gold_buy_sell_ru, text="Голд🍯")
    dp.register_message_handler(goldpass_ru, text="Голд Пасс🎖")
    dp.register_message_handler(menu_ru, text="Главное меню🏠")
    dp.register_message_handler(gold_ru, text="Купить📈")
    dp.register_message_handler(price_ru, text="Прайс лист📜")
    dp.register_message_handler(gold_sell_ru, text="Продать📉")
    dp.register_message_handler(gold_start_ru, text="Сколько будет стоить Х-Голды🍯")
    dp.register_message_handler(gold_stop_ru, state=FSMrus.gold)
    dp.register_message_handler(som_start_ru, text="Сколько голды будет на Х сум💸")
    dp.register_message_handler(som_stop_ru, state=FSMsomRU.som)
    dp.register_message_handler(account_ru, text='Аккаунты🔥')
    dp.register_message_handler(account_sell_ru, text="Хочу продать📉")
    dp.register_callback_query_handler(account_sell2_ru, text='да')
    dp.register_message_handler(account_buy_ru, text="Хочу купить📈")
    dp.register_message_handler(gr_ru, text='Беседа💬')
    dp.register_message_handler(otzv_ru, text='Отзывы📊')
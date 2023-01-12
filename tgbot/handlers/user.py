from aiogram import Dispatcher
from aiogram import types
from tgbot.keyboards.inline import *
from aiogram import Bot
from tgbot.misc.states import FSMrus, FSMuz, FSMsom, FSMsomRU
from aiogram.dispatcher import FSMContext
from functions.func import get_info_sum, get_info, sum_correct

bot = Bot(token='5226272322:AAEZsPMW68-W9Hx7UkmtfkA-qUI1A9NTrQw', parse_mode='HTML')

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
    await message.answer('Hali tayyor mas!')
#GOLD PASS

async def gold_buy_sell(message: types.Message):
    await message.answer("Operatsiyani tanlang:", reply_markup=button_buy_sell)

async def menu_uz(message: types.Message):
    await message.answer('Bosh sahifaga qaytdingiz✔️', reply_markup=buttons)

async def price_uz(message: types.Message):
    await message.answer("📉1G dan 999G gacha - 1G=170 som \n\n📉1000G dan 2999G gacha - 1G=166 som \n\n📉3000G dan ∞ gacha - 1G=130 som", reply_markup = btn_all_uz)

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
            await message.answer(f'{gold} Gold🍯 - {main_som} som boladi.\n \n ❗️Sotib olish uchun 7000ta zaprosdan kop bolmagan skinni {commission} ga qoyib @jamshid_5878 ga skrinwot jonating😊', reply_markup=Inline_link)
            await message.answer("💳Uzcard:\n8600 5704 2845 4275\nIgamberdiev Ibrohim", reply_markup=buttons)
            await bot.send_message(-1001666478836, f'Klient:  @{message.from_user.username}\nGold: {gold}  \nNarhi: {sum_correct(price)} som \nKomissiya: {commission} ')
            await state.finish()
        elif gold < 99:
            await message.answer('Minimum 100 GOLD❗️', reply_markup=button_back)
        elif gold > 1000000:
            await message.answer('Oyin qimen, puliz yetmidi😂🤣')
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
        if som > 16999:
            info = get_info_sum(som)
            gold = info['gold']
            commission = info['commission']
            main_som = sum_correct(som)
            await message.answer(f'{main_som} som ga {gold} Gold🍯 boladi. \n \n ❗️Sotib olish uchun 7000ta zaprosdan kop bolmagan skinni {commission} ga qoyib @jamshid_5878 ga skrinwot jonating😊', reply_markup=Inline_link)
            await message.answer("💳Uzcard:\n8600 5704 2845 4275\nIgamberdiev Ibrohim", reply_markup=buttons)
            await bot.send_message(-1001666478836, f'Klient:  @{message.from_user.username}\nGold: {gold}  \nNarhi: {sum_correct(som)} som \nKomissiya: {commission} ')
            await state.finish()
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
    await message.answer("Akkaunt sotish togrisidagi eloningiz:\n @standoff2akkauntbozor kanaliga joylashtiliradi! \n \nElon joylashtirish narhi 10.000 som.", reply_markup=btn_boshiga)
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
    await message.reply("Gruppada reklama va sokinish taqiqlanadi!🚫 \n Ozingizni yaxshi tuting!", reply_markup=button_gr)

#Рус язык
async def rus(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await start_.delete()    
    await bot.send_message(call.from_user.id, "‼️Извините, в настоящее время Русский язык находится в разработке. Выберите другой язык!\n\nКликните -> /start")

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
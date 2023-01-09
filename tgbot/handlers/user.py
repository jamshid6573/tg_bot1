from aiogram import Dispatcher
from aiogram import types
from tgbot.keyboards.inline import *
from aiogram import Bot
from tgbot.misc.states import FSMrus, FSMuz, FSMsom, FSMsomRU
from aiogram.dispatcher import FSMContext
from functions.func import get_info_sum, get_info, sum_correct

bot = Bot(token='908579189:AAGf6CGZa_Vx_ohvDLPa_WXci10s3uksi0M', parse_mode='HTML')

async def user_start(message: types.Message):
    global start_
    start_ = await message.reply("Bot ga hush kelibsiz, tilni tanlang. \n \nДобро пожалововать в бот, выберите язык.", reply_markup=Inline_lang)


#Узб язык
async def uzb(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await start_.delete()    
    await bot.send_message(call.from_user.id, "Uzbek tili tanlandi!", reply_markup=buttons)


async def gold_uz(message: types.Message):
    await message.answer("Operatsiyani tanlang:", reply_markup = btn_all_uz)

#GOLD PASS
async def goldpass(message: types.Message):
    await message.answer('Gold pass')
#GOLD PASS

async def gold_buy_sell(message: types.Message):
    await message.answer("Operatsiyani tanlang:", reply_markup=button_buy_sell)

async def menu_uz(message: types.Message):
    await message.answer('Bosh sahifaga qaytdingiz✔️', reply_markup=buttons)

async def price_uz(message: types.Message):
    await message.answer("Prays", reply_markup = btn_all_uz)

#GOLD SOTISH
async def gold_sell(message: types.Message):
    await message.answer('Hali tayyormas')
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
            # await bot.send_message(-1001666478836, f'Zakaz:  @{message.from_user.username} - {gold} Gold \nNarhi: {price} ')
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
            await state.finish()
    elif message.text == "Bekor qilish❌":
        await message.answer('Bekor qilindi✔️', reply_markup=buttons)
        await state.finish()
    else:
        await message.answer("🛑Hato! Iltimos butun son kiriting! \n Harflar va simvollar bolmasligi kerak!")
# FSM SOM UZ




#Рус язык
async def rus(call: types.CallbackQuery):
    await bot.answer_callback_query(call.id)
    await start_.delete()    
    await bot.send_message(call.from_user.id, "Выбран русский язык!", reply_markup=buttons_rus)

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_callback_query_handler(uzb, text="uz")
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
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import os



bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button_1 = "Нидерланды"
    button_2 = "Франция"
    button_3 = "Испания"
    button_4 = "РФ"
    button_5 = "Казахстан"
    button_6 = "Беларусь"
    keyboard.add(button_1,button_2,button_3,button_4,button_5,button_6)
    await message.answer("Привет! Откуда ты?", reply_markup=keyboard)

NL = ["https://youtube.com", "https://yandex.com", "https://google.nl", "https://instagram.com", "🇳🇱"]
FR = ["https://youtube.com", "https://yandex.com", "https://google.fr", "https://instagram.com", "🇫🇷"]
ES = ["https://youtube.com", "https://yandex.com", "https://google.es", "https://instagram.com", "🇪🇸"]
RU = ["https://youtube.com", "https://yandex.ru", "https://google.ru", "https://instagram.com", "🇷🇺"]
KZ = ["https://youtube.com", "https://yandex.kz", "https://google.kz", "https://instagram.com", "🇰🇿"]
BY = ["https://youtube.com", "https://yandex.by", "https://google.by", "https://instagram.com", "🇧🇾"]

@dp.message_handler(lambda message: 'Нидерланды' in message.text)
async def netherlands_links (message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url=NL[0]))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url=NL[1]))
    keyboard.add(types.InlineKeyboardButton(text="Google", url=NL[2]))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url=NL[3]))
    
    await message.answer("Вы выбрали страну " + NL[4], reply_markup=keyboard)
    
@dp.message_handler(lambda message: 'Франция' in message.text)
async def france_links (message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url=FR[0]))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url=FR[1]))
    keyboard.add(types.InlineKeyboardButton(text="Google", url=FR[2]))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url=FR[3]))
    
    await message.answer("Вы выбрали страну " + FR[4], reply_markup=keyboard)
    
@dp.message_handler(lambda message: 'Испания' in message.text)
async def spain_links (message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url=ES[0]))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url=ES[1]))
    keyboard.add(types.InlineKeyboardButton(text="Google", url=ES[2]))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url=ES[3]))
    
    await message.answer("Вы выбрали страну " + ES[4], reply_markup=keyboard)

@dp.message_handler(lambda message: 'РФ' in message.text)
async def russia_links (message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url=RU[0]))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url=RU[1]))
    keyboard.add(types.InlineKeyboardButton(text="Google", url=RU[2]))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url=RU[3]))
    
    await message.answer("Вы выбрали страну " + RU[4], reply_markup=keyboard)

@dp.message_handler(lambda message: 'Казахстан' in message.text)
async def kazakhstan_links (message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url=KZ[0]))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url=KZ[1]))
    keyboard.add(types.InlineKeyboardButton(text="Google", url=KZ[2]))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url=KZ[3]))
    
    await message.answer("Вы выбрали страну " + KZ[4], reply_markup=keyboard)

@dp.message_handler(lambda message: 'Беларусь' in message.text)
async def belarus_links (message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url=BY[0]))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url=BY[1]))
    keyboard.add(types.InlineKeyboardButton(text="Google", url=BY[2]))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url=BY[3]))
    
    await message.answer("Вы выбрали страну " + BY[4], reply_markup=keyboard)    


executor.start_polling(dp, skip_updates=True)

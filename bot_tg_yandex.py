from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import os



bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = "/Нидерланды"
    keyboard.add(button_1)
    button_2 = "/Франция"
    keyboard.add(button_2)
    button_3 = "/Испания"
    keyboard.add(button_3)
    button_4 = "/РФ"
    keyboard.add(button_4)
    button_5 = "/Казахстан"
    keyboard.add(button_5)
    button_6 = "/Беларусь"
    keyboard.add(button_6)
    await message.answer("Привет! Откуда ты?", reply_markup=keyboard)

    
    
@dp.message_handler(commands="Нидерланды")
async def Netherlands(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url="https://youtube.com"))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url="https://yandex.com"))
    keyboard.add(types.InlineKeyboardButton(text="Google", url="https://google.nl"))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url="https://instagram.com"))
    
    await message.answer("Вы выбрали страну 🇳🇱", reply_markup=keyboard)

@dp.message_handler(commands="Франция")
async def France(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url="https://youtube.com"))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url="https://yandex.com"))
    keyboard.add(types.InlineKeyboardButton(text="Google", url="https://google.fr"))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url="https://instagram.com"))

    await message.answer("Вы выбрали страну 🇫🇷", reply_markup=keyboard)
    
@dp.message_handler(commands="Испания")
async def Spain(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url="https://youtube.com"))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url="https://yandex.com"))
    keyboard.add(types.InlineKeyboardButton(text="Google", url="https://google.es"))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url="https://instagram.com"))

    await message.answer("Вы выбрали страну 🇪🇸", reply_markup=keyboard)
    
@dp.message_handler(commands="РФ")
async def Russia(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url="https://youtube.com"))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url="https://yandex.ru"))
    keyboard.add(types.InlineKeyboardButton(text="Google", url="https://google.ru"))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url="https://instagram.com"))

    await message.answer("Вы выбрали страну 🇷🇺", reply_markup=keyboard)
    
@dp.message_handler(commands="Казахстан")
async def Kazakhstan(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url="https://youtube.com"))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url="https://yandex.kz"))
    keyboard.add(types.InlineKeyboardButton(text="Google", url="https://google.kz"))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url="https://instagram.com"))

    await message.answer("Вы выбрали страну 🇰🇿", reply_markup=keyboard)
    
@dp.message_handler(commands="Беларусь")
async def Belarus(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="YouTube", url="https://youtube.com"))
    keyboard.add(types.InlineKeyboardButton(text="Yandex", url="https://yandex.by"))
    keyboard.add(types.InlineKeyboardButton(text="Google", url="https://google.by"))
    keyboard.add(types.InlineKeyboardButton(text="Instagram", url="https://instagram.com"))

    await message.answer("Вы выбрали страну 🇧🇾", reply_markup=keyboard)
    
executor.start_polling(dp, skip_updates=True)
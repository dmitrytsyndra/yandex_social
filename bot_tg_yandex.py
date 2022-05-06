from re import X
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

countries = [
  {
     'name': 'Нидерланды',
     'flag': '🇳🇱',
     'socials': [
        { 'text': 'Youtube', 'url': 'youtube.com' },
        { 'text': 'Yandex', 'url': 'yandex.com' },
        { 'text': 'Google', 'url': 'google.nl' },
        { 'text': 'Instagram', 'url': 'instagram.com' },
     ]
  },
  {
     'name': 'Франция',
     'flag': '🇫🇷',
     'socials': [
        { 'text': 'Youtube', 'url': 'youtube.com' },
        { 'text': 'Yandex', 'url': 'yandex.com' },
        { 'text': 'Google', 'url': 'google.fr' },
        { 'text': 'Instagram', 'url': 'instagram.com' },
     ]
  },
  {
     'name': 'Испания',
     'flag': '🇪🇸',
     'socials': [
        { 'text': 'Youtube', 'url': 'youtube.com' },
        { 'text': 'Yandex', 'url': 'yandex.com' },
        { 'text': 'Google', 'url': 'google.es' },
        { 'text': 'Instagram', 'url': 'instagram.com' },
     ]
  },
  {
     'name': 'РФ',
     'flag': '🇷🇺',
     'socials': [
        { 'text': 'Youtube', 'url': 'youtube.com' },
        { 'text': 'Yandex', 'url': 'yandex.ru' },
        { 'text': 'Google', 'url': 'google.ru' },
        { 'text': 'Instagram', 'url': 'instagram.com' },
     ]
  },
  {
     'name': 'Казахстан',
     'flag': '🇰🇿',
     'socials': [
        { 'text': 'Youtube', 'url': 'youtube.com' },
        { 'text': 'Yandex', 'url': 'yandex.kz' },
        { 'text': 'Google', 'url': 'google.kz' },
        { 'text': 'Instagram', 'url': 'instagram.com' },
     ]
  },
  {
     'name': 'Беларусь',
     'flag': '🇧🇾',
     'socials': [
        { 'text': 'Youtube', 'url': 'youtube.com' },
        { 'text': 'Yandex', 'url': 'yandex.by' },
        { 'text': 'Google', 'url': 'google.by' },
        { 'text': 'Instagram', 'url': 'instagram.com' },
     ]
  },
]


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = []
    for c in countries:
        buttons.append(c['name'])

    keyboard.add(*buttons)

    await message.answer("Привет! Откуда ты?", reply_markup=keyboard)

def should_handle_on_country_button_click(message):
    for c in countries:
        if message.text == c['name']:
            return True
    return False

def get_country_by_name(country_name):
    for c in countries:
        if country_name == c['name']:
            return c
    return None
            
@dp.message_handler(should_handle_on_country_button_click)
async def on_country_button_click(message: types.Message):
    country = get_country_by_name(message.text)
    keyboard = types.InlineKeyboardMarkup()

    for s in country['socials']:
        keyboard.add(types.InlineKeyboardButton(text=s['text'], url=s['url']))
    await message.answer('Вы выбрали страну ' + country['flag'], reply_markup=keyboard)

executor.start_polling(dp, skip_updates=True)


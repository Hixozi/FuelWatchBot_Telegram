from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import xml.etree.ElementTree as ET

bot = Bot(token='6176971731:AAFJmyMYgylbEP1RhrA_NgNLOChkV41vV7I')
dp = Dispatcher(bot)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard1.add(KeyboardButton("ULP", callback_data='1'),
              KeyboardButton("PULP", callback_data='2'),
              KeyboardButton("DIESEL", callback_data='4'))



@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! Im FuelWatch Bot. Please select a fuel product to check.", reply_markup=keyboard1)


@dp.message_handler(lambda message: message.text.upper() in ["ULP", "PULP", "DIESEL"])
async def process_fuel_choice(message: Message):
    global selected_fuel
    selected_fuel = message.text
    await message.answer("Great! Now type in the suburb you want to check.")

@dp.message_handler()
async def process_suburb_choice(message: Message):
    global selected_fuel
    suburb = message.text
    await message.answer(f"Getting the fuel prices for {selected_fuel} in {suburb}.")


executor.start_polling(dp)

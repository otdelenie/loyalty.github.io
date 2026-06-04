import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import requests
from os import getenv
from aiogram.exceptions import TelegramBadRequest

CHANEL_ID = "@test5jj"

API_TOKEN = "8598365951:AAG6rMb1UEuXBB6Iua79UjZ8cqZ5zHol0M8"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

mini_app_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = "Mini App", url= "https://otdelenie.github.io/loyalty.github.io/")]])
@dp.message(F.text == "admin")
async def admin_command(message: Message):
    await message.answer("enter admin password:")

#test subscribe to channel
@dp.message(Command("test"))
async def test_command(message: Message):
    mes_kb = InlineKeyboardMarkup(inline_keyboard=
                                  [[InlineKeyboardButton(text="Chenel1",url="https://www.youtube.com/?app=desktop&gl=UA&hl=uk")],
                                   [InlineKeyboardButton(text="Test channel", url="https://t.me/test5jj")],
                                   [InlineKeyboardButton(text="Chenel3", callback_data="channel3")],
                                   [InlineKeyboardButton(text="Check Subscriptions", callback_data="check_subscriptions")]])
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    member = await bot.get_chat_member(CHANEL_ID, user_id)
    if member.status in ["creator", "administrator", "member"]:
        await message.answer(f"{user_name}, you are subscribed: {member.status} to the channel!", reply_markup= mini_app_kb)
        
    else:
        await message.answer(f"{user_name}, you are not subscribed to the channel. Please subscribe to the channel to register for the loyalty program.", reply_markup=mes_kb)

@dp.callback_query(F.data == "check_subscriptions")
async def check_subscriptions_callback(callback_query: CallbackQuery):
    await callback_query.answer()  # Acknowledge the callback query
    user_name = callback_query.from_user.full_name
    user_id = callback_query.from_user.id
    member = await bot.get_chat_member(CHANEL_ID, user_id)
    if member.status in ["creator", "administrator", "member"]:
        await callback_query.message.answer(f"{user_name}, you are subscribed: {member.status} to the channel!", reply_markup= mini_app_kb)
        
    else:
        await callback_query.message.answer(f"{user_name}, you are not subscribed: {member.status} to the channel. Please subscribe to the channel to register for the loyalty program.")
##

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.answer(message.from_user.full_name + ", welcome to the loyalty program! Please register by typing /register.")

@dp.message(Command("register"))
async def register_command(message: Message):  
    kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="test1"), KeyboardButton(text="test2")], [KeyboardButton(text="Cancel")]], 
                             resize_keyboard=True, input_field_placeholder="xxx")
    await message.answer("You have been registered for the loyalty program!", reply_markup=kb)

@dp.message(F.text == "Cancel")
async def cancel_command(message: Message):
    await message.answer("Registration cancelled.", reply_markup=ReplyKeyboardRemove())

# Запуск бота
async def main():

    print("Bot started successfully...")

    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()

# Запуск
if __name__ == "__main__":
    asyncio.run(main())


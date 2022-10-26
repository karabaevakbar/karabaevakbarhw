import random
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from Database.bot_db import sql_command_random, sql_command_all

# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f'Жакшысынарбы {message.from_user.full_name}')


# @dp.message_handler(commands=['mem'])
async def mem_command(message: types.Message):
    mem_photo = open("media/mem-3.jpg", "rb")
    number = random.randint(1, 4)
    if number == 1:
        mem_photo = open("media/mem-1.jpg", "rb")
    if number == 2:
        mem_photo = open("media/mem-2.jpg", "rb")
    await bot.send_photo(message.chat.id, mem_photo)


# @dp.message_handler(commands=["quiz"])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("След.", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Сколько областей есть в Кыргызстане?"
    answers = [
        '4',
        '5',
        '6',
        '7',
        'нету',
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="",
        open_period=30,
        reply_markup=markup
    )
async def pin(message: types.Message):
    if not message.reply_to_message:
        await message.reply('Комманда должна быть ответом на сообщение!')
    else:
        await bot.pin_chat_message(message.chat.id, message.message_id)
def register_handlers_client(dp: Dispatcher):
    async def get_random_user(message: types.Message):
        await sql_command_random(message)
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(mem_command, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(get_random_user, commands=["getmentor"])
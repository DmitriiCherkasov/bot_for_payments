from aiogram import types, Dispatcher
from create_bot import dp, bot
import time
from datetime import datetime
from keyboards.create_keyboard import create_keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from additional_functions.create_invoice import create_invoice
from all_messages import messages_dict
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dp.message_handler(commands=['start'], state=None)
async def greetings(message: types.Message):
    await message.answer(messages_dict['hello_message'], reply_markup=InlineKeyboardMarkup().add(
                        InlineKeyboardButton(text='Оплатить консультацию',
                                             url=create_invoice(price=1, order='Консультация')))
                         )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(greetings, commands=['start', 'help'])

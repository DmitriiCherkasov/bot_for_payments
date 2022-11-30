from aiogram import types, Dispatcher
from create_bot import dp, bot
import json
import string


#@dp.message_handler(lambda message: "?" in message.text)
#async def question(message: types.Message):
#    await bot.send_message(message.from_user.id, 'Хм.. Спросите у Дмитрия(@Dm Che).')


# @dp.message_handler()
# async def echo_send(message: types.Message):
#     if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(
#             set(json.load(open('forbidden_words.txt')))) != set():
#         await bot.send_message(message.from_user.id, 'Эй-эй!В бан захотел?')
#         await message.delete()


# def register_handlers_other(dp: Dispatcher):
#     dp.register_message_handler(echo_send)
#    dp.register_message_handler(question)

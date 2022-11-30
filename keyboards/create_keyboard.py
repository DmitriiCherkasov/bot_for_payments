from aiogram.types import InlineKeyboardMarkup


def create_keyboard(*args, count_of_buttons: int = 1):
    """This function create inline keyboard.
        First positional argument is text and second is a callback data
        of the first inline button."""
    buttons = []
    arguments_list = list(args)
    while arguments_list:
        button = {'text': arguments_list[0], 'callback_data': arguments_list[1]}
        arguments_list.pop(0)
        arguments_list.pop(0)
        buttons.append(button)
    return InlineKeyboardMarkup(row_width=count_of_buttons).add(*buttons)

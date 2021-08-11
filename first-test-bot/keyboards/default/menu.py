from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Котлетки"),
        ],
        [
            KeyboardButton(text="Макарошки"),
            KeyboardButton(text="Пюрешка")
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True)
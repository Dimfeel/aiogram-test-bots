from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_datas import buy_callback

from data.urls import product_urls 

product_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            #Два способа задания callback'ов
            InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(
                item_name = "pear", quantity = 1
            )),
            InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple:5")
        ],
        [
            InlineKeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ]
)

#Другой способ задать InlineKeyboard

# product_choice = InlineKeyboardMarkup(row_width=2)
# buy_pear = InlineKeyboardButton(text="Купить грушу", callback_data=buy_callback.new(
#                 item_name = "pear", quantity = 1
#             ))
# product_choise.insert(buy_pear)
# buy_apples = InlineKeyboardButton(text="Купить яблоки", callback_data="buy:apple:5")
# product_choise.insert(buy_apples)

# cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cansel")
# product_choise.insert(cancel_button)

#Клавиатуры для pear и apples
pear_choice = InlineKeyboardMarkup()
auchan_pear_button = InlineKeyboardMarkup(text="Купи в Ашан", url=product_urls["pears"])
pear_choice.insert(auchan_pear_button)

apple_choice = InlineKeyboardMarkup()
auchan_apple_button = InlineKeyboardMarkup(text="Купи в Ашан", url=product_urls["apples"])
apple_choice.insert(auchan_apple_button)
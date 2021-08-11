from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import Text
from aiogram.types.message import Message
from aiogram.types import CallbackQuery
from keyboards.inline import product_choice, pear_choice, apple_choice
from keyboards.inline.callback_datas import buy_callback

import logging

from loader import dp

@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(
        text="На продажу у нас есть 5 яблок и 1 груша.\n"
        "Если ничего не нужно, нажмите 'Отмена'",
        reply_markup=product_choice)

#при таком фильтре call.data - строка типа "buy:pear:1"
@dp.callback_query_handler(text_contains="pear")
async def buying_pear(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f"call = {callback_data}")
    await call.message.answer(
        "Вы выбрали купить грушу. Груша всего одна. Спасибо",
        reply_markup=pear_choice)

#при таком фильтре callback_data - dict {'@': 'buy', 'item_name': 'apple', 'quantity': '5'}
@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"call = {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(
        f"Вы выбрали яблоки. Яблок всего {quantity}. Спасибо",
        reply_markup=apple_choice)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    await call.answer("Вы отменили эту покупку", show_alert=True)
    await call.message.edit_reply_markup()
    #await call.message.edit_reply_markup(None)

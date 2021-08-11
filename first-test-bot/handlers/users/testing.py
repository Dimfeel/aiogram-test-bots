import data
from aiogram import types
from aiogram.dispatcher import dispatcher

from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import message
from states.test import Test

from loader import dp

@dp.message_handler(Command("test"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование!\n"
                        "Сколько вам лет? Чем занимаетесь?")
    
    #Вариант 1 - с помощью функции set
    await Test.Q1.set()
    
    #Вариант 2 - с помощью функции first
    #await Test.first()

@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.message.Message, state:FSMContext):
    answer = message.text

    #Вариант 2 получения state (от другого пользователя)
    #state = dp.current_state(chat=message.chat.id,user=message.from_user.id)

    #Вариант 1 сохранения переменных - записываем через key=var
    await state.update_data(answer1 = answer)

    #Вариант 2 - передаем как словарь
    #await state.update_data(
    #    {"answer1":answer}
    #)

    #Вариант 3 - через state.proxy
    #async with state.proxy() as data:
        #data["answer1"] = answer
        #Удобно, если нужно сделать data["some_digit"] += 1
        #Или data["some_list"].append(1), т.к. не нужно сначала доставать из стейта, а потом задавать

    await message.answer("Вопрос 2\n\n Че по чем и зачем?")

    await Test.next()

@dp.message_handler(state=Test.Q2)
async def answer_q1(message: types.message.Message, state:FSMContext):
    answer2 = message.text

    data = await state.get_data()
    answer1 = data.get("answer1")

    await message.answer("Спасибо за ваши ответы!")

    #Вариант 1
    await state.finish()

    #Вариант 2 завершения
    #await state.reset_state()

    #Вариант 3 завершения - без стирания данных в data
    #await state.reset_state(with_data=False)
from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("menu", "Клавиатуры: Текстовые кнопки"),
            types.BotCommand("items", "Клавиатуры: Inline кнопки"),
            types.BotCommand("test", "Машина состояний"),
        ]
    )

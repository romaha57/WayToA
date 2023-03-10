from aiogram import types

from keyboards.inline import start_buttons


async def echo(message: types.Message) -> None:
    """Отлавливает любые другие сообщения и выводит сообщение с кнопками функций бота"""

    await message.answer('Выберите одну из функций',
                         reply_markup=start_buttons())

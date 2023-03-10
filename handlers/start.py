from aiogram import types

from keyboards.inline import start_buttons


async def get_start(message: types.Message) -> None:
    """Обработчик команды /start и /help"""

    message_text = 'Вас приветствует бот компании WayToA\n' \
                   'Для подбора задач нажмите на кнопку '

    await message.answer(message_text, reply_markup=start_buttons())

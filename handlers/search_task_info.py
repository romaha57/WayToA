from aiogram import types
from aiogram.dispatcher import FSMContext

from states.search_state import SearchState
from config_db.database import session
from config_db.services import OperationDB
from utils.formatter_answer import format_search_result
from keyboards.inline import start_buttons


service = OperationDB(session=session)


async def press_search_task_button(callback: types.CallbackQuery) -> None:
    """Обработчик нажатия на кнопку 'Поиск по заданиям' """

    await callback.message.answer(
        'Введите название задачи')
    await SearchState.name.set()
    await callback.answer()


async def get_search_task(message: types.Message, state: FSMContext) -> None:
    """Отлавливаем слово для поиска и устанавливаем в FSM"""

    async with state.proxy() as data:
        data['name'] = message.text

    tasks = service.get_task_by_name(message.text.lower())
    answer = format_search_result(tasks)

    # завершаем FSM
    await state.finish()

    await message.answer(answer, reply_markup=start_buttons())

from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline import start_buttons
from keyboards.reply import get_categories_button, get_complexity_button
from states.selection_state import SelectionState
from config_db.database import session
from config_db.services import OperationDB
from utils.formatter_answer import format_search_result

service = OperationDB(session=session)


async def press_start_selection_button(callback: types.CallbackQuery) -> None:
    """Обработчик нажатия на кнопку 'начать подбор' """

    await callback.message.answer(
        'Выберите тему', reply_markup=get_categories_button())

    await SelectionState.category.set()
    await callback.answer()


async def get_category_name(message: types.Message, state: FSMContext) -> None:
    """Отлавливаем название темы и устанавливаем в FSM"""

    async with state.proxy() as data:
        data['category'] = message.text

    await SelectionState.complexity.set()
    await message.answer(f'Отлично, выбрана тема: {data["category"]}\n'
                         f'Теперь надо выбрать сложность заданий',
                         reply_markup=get_complexity_button())


async def get_complexity_task(message: types.Message, state: FSMContext) -> None:
    """Отлавливаем название темы и устанавливаем в FSM"""

    if message.text.isdigit():
        async with state.proxy() as data:
            data['complexity'] = message.text

        await state.finish()

        tasks = service.get_tasks_by_params(
            category=data['category'],
            complexity=data['complexity']
        )
        if tasks:
            answer = format_search_result(tasks=tasks)
            await message.answer(answer, reply_markup=start_buttons())
        else:
            await message.answer('Не удалось найти задачи по данным критериям',
                                 reply_markup=start_buttons())
    else:
        await message.answer('Сложность должна быть число(от 800 до 1800)',
                             reply_markup=start_buttons())

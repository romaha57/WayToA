from aiogram import Dispatcher

from handlers.selection import press_start_selection_button, get_category_name, get_complexity_task
from handlers.search_task_info import press_search_task_button, get_search_task
from handlers.start import get_start
from handlers.echo import echo
from states.search_state import SearchState
from states.selection_state import SelectionState


def register_handlers(dp: Dispatcher) -> None:
    """Функция для регистрации всех хендлеров"""

    dp.register_message_handler(get_start, commands=['start', 'help'])
    dp.register_callback_query_handler(press_start_selection_button, text='start_selection')
    dp.register_callback_query_handler(press_search_task_button, text='search_task')
    dp.register_message_handler(get_search_task, state=SearchState.name)
    dp.register_message_handler(get_category_name, state=SelectionState.category)
    dp.register_message_handler(get_complexity_task, state=SelectionState.complexity)
    dp.register_message_handler(echo, content_types=['text'])

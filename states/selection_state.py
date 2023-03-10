from aiogram.dispatcher.filters.state import StatesGroup, State


class SelectionState(StatesGroup):
    """Класс для создания машины состояния при подборе задач"""

    category = State()
    complexity = State()

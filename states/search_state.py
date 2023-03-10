from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchState(StatesGroup):
    """Класс для создания машины состояния при поиске"""

    name = State()

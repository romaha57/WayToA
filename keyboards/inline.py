from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_buttons():
    """Стартовые кнопки для поиска и подбора задачи"""

    start_selection_button = InlineKeyboardButton(text='Начать подбор', callback_data='start_selection')
    search_task_button = InlineKeyboardButton(text='Поиск по заданиям', callback_data='search_task')

    inline_buttons = InlineKeyboardMarkup()
    inline_buttons.add(start_selection_button, search_task_button)

    return inline_buttons

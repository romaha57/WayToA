from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config_db.database import session
from config_db.services import OperationDB


service = OperationDB(session=session)


def get_categories_button() -> ReplyKeyboardMarkup:
    """Reply кнопки для вывода всех категорий из БД"""

    categories = service.get_all_categories()
    all_reply_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for category in categories:
        button = KeyboardButton(text=f'{category.name}',)
        all_reply_keyboards.add(button)

    return all_reply_keyboards


def get_complexity_button() -> ReplyKeyboardMarkup:
    """Reply кнопки для вывода всех значений сложности задач из БД"""

    complexity = service.get_all_complexity_value()
    all_reply_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for c in complexity:
        button = KeyboardButton(text=f'{c}',)
        all_reply_keyboards.add(button)

    return all_reply_keyboards

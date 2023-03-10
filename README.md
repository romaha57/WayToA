# Тестовое задание
> Примечание
- Знаю, что файл .env не надо загружать в git, но решил так сделать, чтобы проще проверять задание вам

## Задача: 
- Спарсить данные с сайта https://codeforces.com/
- Добавить в БД Postgres
- Подключить телеграм бота для работы с этими данными

## Установка:

1. `git clone https://github.com/romaha57/WayToA.git`
2. `pip install -r requirements.txt`
3. `python schedule_task.py &`
4. `python main.py`


## Функционал

- Поиск по названию задачи(регистронезависимый)
- Подбор задач исходя из выбранной категории и сложности

## Структура БД

![database_structure](/img/database_structure.png)
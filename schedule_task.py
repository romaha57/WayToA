from config_db.database import Category, Task, session
from parser.pars_tasks import get_categories, get_tasks

import schedule


class ServiceDB:
    """Бизнес логика по добавлению данных с сайта в БД"""

    def __init__(self, session):
        self.session = session

    def add_categories_in_db(self):
        """Добавляет категории в БД"""

        categories = get_categories()
        categories_from_db = [cat.name for cat in self.session.query(Category).all()]
        new_categories = set(categories).difference(set(categories_from_db))
        print(f'Найдено {len(new_categories)} новых тем')
        if new_categories:
            for category in new_categories:
                cat = Category(
                    name=category
                )
                self.session.add(cat)
                print(f'Тема: {cat.name} добавлена')
            self.session.commit()

    def add_tasks_in_db(self):
        """Добавляет задачи в БД"""

        tasks_from_parser = get_tasks()
        tasks_from_parser_numbers = [t['number'] for t in tasks_from_parser]
        tasks_from_db = [t.number for t in self.session.query(Task).all()]

        # проверяем есть ли новые задачи по их номерам
        numbers_of_new_tasks = set(tasks_from_parser_numbers).difference(set(tasks_from_db))
        print(f'Найдено {len(numbers_of_new_tasks)} новых задач')
        if numbers_of_new_tasks:
            for task in tasks_from_parser:
                if task['number'] in numbers_of_new_tasks:
                    t = Task(
                        number=task['number'],
                        name=task['name'],
                        complexity=task['complexity'],
                        count_solution=task['count_solution']
                    )

                    for category_name in task['categories']:
                        category = self.session.query(Category).filter(Category.name==category_name).first()
                        if category:
                            t.categories_id.append(category)

                    self.session.add(t)
                    print(f'Задача: {t.name}/{t.number} добавлена')
                self.session.commit()


serv = ServiceDB(session=session)
schedule.every().hour.do(serv.add_categories_in_db)
schedule.every(59).minutes.do(serv.add_tasks_in_db)


def fill_db():
    while True:
        # каждый час добавляет данные в БД
        schedule.run_pending()


if __name__ == '__main__':
    fill_db()

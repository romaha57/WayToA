from random import randint

from sqlalchemy.orm import Session

from .database import Task, Category
from utils.split_task_in_group import split_tasks


class OperationDB:
    def __init__(self, session: Session):
        self.session = session

    def get_task_by_name(self, task_name):
        tasks = self.session.query(Task).filter(Task.name.contains(task_name)).order_by(Task.name)
        return tasks

    def get_all_categories(self):
        categories = self.session.query(Category).order_by(Category.name).all()

        return categories

    def get_all_complexity_value(self):
        complexity_value = self.session.query(Task).distinct(Task.complexity).order_by(Task.complexity)
        unique_complexity_value = [i.complexity for i in complexity_value]

        return unique_complexity_value

    def get_tasks_by_params(self, category, complexity):
        tasks = self.session.query(Task).filter(Task.complexity==complexity).filter(Task.categories_id.any(name=category))
        groups_tasks = list(split_tasks(tasks, delimiter=10))
        if groups_tasks:
            if len(groups_tasks) > 1:
                random_tasks_group = groups_tasks[randint(0, len(groups_tasks) - 1)]
                return random_tasks_group

            return groups_tasks[0]
        return False

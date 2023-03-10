from sqlalchemy.orm import Query


def split_tasks(tasks: Query, delimiter: int) -> None:
    """Разбивает задачи по группам в количестве delimiter: int"""

    for i in range(0, tasks.count(), delimiter):
        yield tasks[i: i + delimiter]

from sqlalchemy.orm import Query


def format_search_result(tasks: Query) -> str:
    """Формирует ответ в телеграм по задачам"""

    answer = ''
    count = 0
    for task in tasks:
        count += 1
        category_str = ''
        for category in task.categories_id:
            category_str += category.name + ' / '
        answer += f'\n<b>Название</b>: {task.name.title()}' \
                  f'\nНомер: {task.number}' \
                  f'\nСложность: {task.complexity}' \
                  f'\nКатегории: {category_str[:-2]}' \
                  f'\nКоличество решений: {task.count_solution}' \
                  f'\nРешить: https://codeforces.com/problemset/problem/{task.number[:-1]}/{task.number[-1]}\n\n'
    answer += f'<b>Всего найдено задач: {count}</b>'

    return answer

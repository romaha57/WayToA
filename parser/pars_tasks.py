from http import HTTPStatus

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


rand_user_agent = UserAgent().random
params = {
    'User-Agent': rand_user_agent,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}


def get_request(url: str) -> str | bool:
    """GET запрос по url"""

    response = requests.get(url, params=params)
    if response.status_code == HTTPStatus.OK:
        return response.text

    return False


def get_categories() -> list[str]:
    """Получает все категории из селектора на странице 'Архив' """

    categories_list = []
    response = get_request(url='https://codeforces.com/problemset?locale=ru')
    if response:
        soup = BeautifulSoup(response, 'lxml')

        selector = soup.find('div', class_='_FilterByTagsFrame_addTag smaller').find_all('option')
        for category in selector[2:]:
            categories_list.append(category.text.strip())

        # частный случай для категории
        categories_list.append('*особая задача')

        return categories_list


def get_amount_page() -> int:
    """Получает количество страниц """

    response = get_request(url='https://codeforces.com/problemset?locale=ru')
    if response:
        soup = BeautifulSoup(response, 'lxml')
        pagination = soup.find('div', class_='pagination')
        max_page = int(pagination.text.split()[-2])

        return max_page


def get_tasks() -> list[dict[str, int | list]]:
    """Получает информацию по задачам"""

    tasks_data = []
    for i in range(1, 16):
        response = get_request(url=f'https://codeforces.com/problemset/page/{i}?order=BY_SOLVED_DESC&locale=ru')
        if response:
            soup = BeautifulSoup(response, 'lxml')
            main_block = soup.find('table', class_='problems').find_all('tr')
            for row in main_block[1:]:
                number = row.find('a').text.strip()
                name = row.find('div').find('a').text.strip()

                categories_list = []
                categories = row.find('div').find('a').findNext().find_all('a')
                for category in categories:
                    categories_list.append(category.text.lower())

                try:
                    complexity = row.find('span', class_='ProblemRating').text

                # если значения нет на сайте поставим по умолчанию 800
                except AttributeError:
                    complexity = 800

                try:
                    count_solution = row.find('span', class_='ProblemRating').findNext().text.strip()
                    count_solution = count_solution.replace('x', '')

                # если значения нет на сайте поставим по умолчанию 0
                except AttributeError:
                    count_solution = 0

                tasks_data.append(
                    {
                        'number': number,
                        'name': name.lower(),
                        'categories': categories_list,
                        'complexity': int(complexity),
                        'count_solution': int(count_solution)
                    }
                )

    return tasks_data

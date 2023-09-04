# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

import logging
from datetime import datetime

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=logging.INFO, filename='project.log', encoding='utf-8',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)

MONTHS = ("", 'янв', 'фев', 'мар', "апр", "мая", "июн", "июл", "авг", "сен", "окт", "ноя", "дек")
WEEKDAYS = ("по", "вт", "ср", "че", "пя", "су", "во")


def get_date(string: str) -> datetime:
    year = datetime.now().year
    number, weekday, month = string.split()
    month = MONTHS.index(month[:3])
    weekday = WEEKDAYS.index(weekday[:2])
    number = int(number[0])
    logger.info(f'{number}, {weekday}, {month}, {year}')
    spam_count = 0
    for day in range(1, 31 + 1):
        date = datetime(day=day, month=month, year=year)
        if date.weekday() == weekday:
            spam_count += 1
            if spam_count == number:
                return date


if __name__ == '__main__':
    print(get_date('3-я среда мая'))
    print(get_date('1-й четверг ноября'))
    print(datetime.now().weekday())

# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# --------------------------------------------------
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.

import argparse
from datetime import datetime

from taks_4 import get_date, WEEKDAYS, MONTHS


def parser_func():
    parser = argparse.ArgumentParser(description='Получаем дату datetime из строки')
    parser.add_argument('-count', type=str, default='1')
    parser.add_argument('-weekday', type=str, default=datetime.now().weekday())
    parser.add_argument('-month', type=str, default=datetime.now().month)
    args = parser.parse_args()

    weekday = WEEKDAYS[args.weekday] if isinstance(args.weekday, int) else args.weekday
    month = MONTHS[args.month] if isinstance(args.month, int) else args.month
    return get_date(f'{args.count} {weekday} {month}')


if __name__ == '__main__':
    print(parser_func())

"""
python .\task_5.py 
"""

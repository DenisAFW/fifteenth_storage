# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='project.log', filemode='a', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger(__name__)


def zero_division(a, b):
    try:
        res = a / b
        logger.info(f'Деление на ноль числа {a} на число {b} = {res}')
        return res
    except ZeroDivisionError as exp:
        logger.error(f'Деление на ноль числа {a}')
        print('Делить на ноль нельзя')
    return float('infinity')


if __name__ == '__main__':
    print(zero_division(5, 0))
    print(zero_division(2, 6))
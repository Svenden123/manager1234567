from contextlib import contextmanager
from datetime import datetime
import math


@contextmanager
def timing():
    start = datetime.now()
    print('Время начала:', start)
    yield
    end = datetime.now()
    print('Время завершения:', end)
    print('Продолжительность:', end - start)


def main():
    print('Программа считает факториал числа')
    n = input('Введите число: ')
    if not n.isdigit():
        print('Ошибка: это не целое число')
        return
    with timing():
        fac = math.factorial(int(n))
        print('Числа:', fac)


if __name__ == '__main__':
    main()
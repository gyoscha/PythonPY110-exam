import json
import random
from typing import Iterator

from faker import Faker

from conf import MODEL


def main(pk=1):
    """
    Данная функция создает список из 100 объектов с помощью функции-генератора.

    :param pk: Счетчик, увеличивающийся на 1 при генерации нового объекта. По умолчанию равен 1.
    :return: Функция ничего не возвращает.
    """
    gen_book = task(pk)
    for _ in range(100):
        print(json.dumps(next(gen_book), indent=4, ensure_ascii=False))


def task(pk: int) -> Iterator[dict]:
    """
    Функция-генератор, которая преобразует словарь, значения которого представляют собой описание книги по различным
    параметрам. Основная задача: сформировать словарь и сделать его более читабельным, преобразовав в Json строку.

    :param pk: Счетчик
    :return: Json строка
    """
    while True:
        dictionary = {
            "model": MODEL,
            "pk": pk,
            "fields": {
                "title": title(),
                "year": year(),
                "pages": pages(),
                "isbn13": isbn13(),
                "rating": rating(),
                "price": price(),
                "author": author()
            }
        }

        yield dictionary
        pk += 1


def title() -> str:
    """
    Открывает файл 'books.txt' и выбирает случайное название книги.

    :return: Случайное название книги из файла books.txt
    """
    with open('books.txt', 'r', encoding='utf8') as file:
        return random.choice(file.read().splitlines())


def year(min_year: int = 1800, max_year: int = 2021) -> int:
    """
    Функция случайным образом выбирает год из диапазона, который задается динамически.
    Используется модуль random метод randint.

    :param min_year: минимальное значение диапазона дат
    :param max_year: максимальное значение диапазона дат
    :return: Случаный год
    """
    return random.randint(min_year, max_year)


def pages(min_page: int = 50, max_page: int = 250) -> int:
    """
    Функция случайным образом выбирает количество страниц в книге из диапазона, который задается динамически.
    Используется модуль random метод randint.

    :param min_page: минимальное значение диапазона страниц
    :param max_page: максимальное значение диапазона страниц
    :return: количество страниц в книге
    """
    return random.randint(min_page, max_page)


def isbn13() -> str:
    """
    Международный стандартный книжный номер, генерируется случайным образом с помощью модуля Faker.

    :return: случайный isbn13
    """
    fake = Faker()
    return fake.isbn13()


def rating(min_rating: float = 0.0, max_rating: float = 5.0) -> float:
    """
    Функция случайным образом выбирает и округляет до 2-х знаков значение рейтинга в диапазоне от 0 до 5.
    Используется модуль random метод uniform.

    :param min_rating: минимальное значение рейтинга
    :param max_rating: максимальное значение рейтинга
    :return: рейтинг книги
    """
    return round(random.uniform(min_rating, max_rating), 2)


def price(min_price: float = 500.0, max_price: float = 2500.0) -> float:
    """
    Функция случайным образом выбирает и округляет до 1 знака значение цены на книгу из диапазона,
    который задается динамически.
    Используется модуль random метод uniform.

    :param min_price: минимальное значение цены
    :param max_price: максимальное значение цены
    :return: цена книги
    """
    return round(random.uniform(min_price, max_price), 1)


def author() -> list:
    """
    Функция с помощью модуля Faker и метода name выбирает фэйковое Имя и Фамилию автора.

    :return: Имя и Фамилия автора
    """
    fake = Faker()
    return [fake.name() for _ in range(random.randint(1, 3))]


if __name__ == '__main__':
    """
    Формируем список из 100 книг в читабельном виде
    """
    main()

import re

from faker import Faker


if __name__ == '__main__':
    isbn_13_checker = re.compile(r"\b(?:978|979)-(?:\d{1,5})-(?:\d{1,7})-(?:\d{1,6})-(?:\d|X)\b")

    fake = Faker()
    for i in range(10 ** 6):
        isbn = fake.isbn13()
        print(isbn)
        check = isbn_13_checker.findall(isbn)
        if isbn in check:
            print('Valid')
        else:
            raise ValueError('Структура ISBN13 неверная')

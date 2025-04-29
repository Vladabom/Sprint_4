import pytest
from main import BooksCollector
import data

@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture(scope='function')
def prepare_books(collector):
    books_genre = [
        [fantasy_book, 'Фантастика'],
        [horror_book, 'Ужасы'],
        [detective_book, 'Детективы'],
        [child_book, 'Мультфильмы'],
        [comedy_book, 'Комедии']
    ]

    for book, genre in books_genre:
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
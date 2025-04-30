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
        [data.fantasy_book, 'Фантастика'],
        [data.horror_book, 'Ужасы'],
        [data.detective_book, 'Детективы'],
        [data.child_book, 'Мультфильмы'],
        [data.comedy_book, 'Комедии']
    ]

    for book, genre in books_genre:
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
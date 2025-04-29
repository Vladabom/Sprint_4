import pytest
from main import BooksCollector

@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector

fantasy_book = 'Фантастическая книга'
horror_book = 'Ужасная книга'
detective_book = 'Детективная книга'
child_book = 'Мульт книга'
comedy_book = 'Комедийная книга'

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
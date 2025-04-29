from main import BooksCollector
import pytest
import data


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2

        # ^ тут кажется ошибка, поменял словарь и метод get_books_rating на существующий словарь и метод get_books_genre
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
     
    # установка книге валидного жанра 
    def test_set_book_genre_add_valid_genre(self, collector):
        collector.add_new_book(fantasy_book)
        collector.set_book_genre(fantasy_book, 'Фантастика')

        assert collector.get_book_genre(fantasy_book) == 'Фантастика'

    # устанавливаем книге не валидный жанр
    def test_set_book_genre_add_invalid_genre(self, collector):
        collector.add_new_book('Книга путешествий')
        collector.set_book_genre('Книга путешествий', 'Путешествия')

        assert collector.get_book_genre('Книга путешествий') == ''

    # получаем жанр книги по её имени
    def test_get_book_genre_get_comedy_book(self, collector, prepare_books):
        assert collector.get_book_genre(comedy_book) == 'Комедии'

    # выводим список книг с определённым жанром, пример параметризации для задания )
    fantastic_genres = [
        ['Фантастическая книга','Фантастика'], 
        ['Книга фантастики','Фантастика'], 
        ['Фантастика и книга','Фантастика'] 
        ]
    @pytest.mark.parametrize('name, genre', fantastic_genres)
    def test_get_books_with_specific_genre_return_fantastic(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert name in collector.get_books_with_specific_genre(genre)

    # получаем словарь books_genre
    def test_get_books_genre(self, collector, prepare_books):
        test_dict = {
        fantasy_book: 'Фантастика',
        horror_book: 'Ужасы',
        detective_book: 'Детективы',
        child_book: 'Мультфильмы',
        comedy_book: 'Комедии'
        }

        assert collector.get_books_genre() == test_dict

    # вывод списка книг, которые подходят детям
    def test_get_books_for_children_three_books_get_list_book(self, collector, prepare_books):
        assert collector.get_books_for_children() == [fantasy_book, child_book, comedy_book]

    # в списке книг для детей нет книг для взрослых
    @pytest.mark.parametrize(
        'book, expected_result',
        [
            [fantasy_book, True],
            [horror_book, False],
            [detective_book, False],
            [child_book, True],
            [comedy_book, True]
        ]
    )
    def test_get_books_for_children_adult_books_not_included_the_list(self, collector, prepare_books, book, expected_result):
        children_books = collector.get_books_for_children()
        
        assert (book in children_books) == expected_result
    # добавление книги в избранное
    def test_add_book_in_favorites_add_one_book(self, collector, prepare_books):
        collector.add_book_in_favorites(fantasy_book)

        assert collector.get_list_of_favorites_books() == [fantasy_book]
    # удаление книги из избранного
    def test_delete_book_from_favorites_removes_book(self, collector, prepare_books):
        collector.add_book_in_favorites(fantasy_book)
        collector.delete_book_from_favorites(fantasy_book)

        assert collector.get_list_of_favorites_books() == []
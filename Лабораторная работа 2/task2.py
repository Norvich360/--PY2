BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    """Класс книги содержит id, название и количество строниц кинги"""

    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Вывод названия книги"""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Вывод всей информации о книге"""
        return f"Book(id_={self.id_}, name='{self.name}', pages={self.pages})"


class Library:
    """Класс, содержащий список книг"""

    def __init__(self, books=None):
        self.books = books
        self.get_next_book_id()

    def get_next_book_id(self) -> int:
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку"""
        if self.books: return [book.id_ + 1 for book in self.books][-1]
        else: return 1

    def get_index_by_book_id(self, number) -> int:
        """Метод, возвращающий индекс книги в списке,
         который хранится в атрибуте экземпляра класса"""
        if not number > 0:
            raise ValueError('Incorrect value. Number must be integers')
        if self.books[number-1] in self.books:
            return number-1
        else:
            raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки


    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

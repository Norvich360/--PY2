class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author: str) -> None:
        self._author = new_author

    def __str__(self):
        """Вывод всей информации о книге"""
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        """Описываем поведение функции repr()"""
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """Класс бумажной книги с аргументом
        количества страниц pages"""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Неверный тип количества страниц")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным и целым числом")
        self._pages = new_pages

    def __str__(self):
        """Вывод всей информации о книге"""
        return f"Книга {self.name}. Автор {self.author}. Страницы {self._pages}"

    def __repr__(self):
        """Описываем поведение функции repr()"""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self._pages!r})"

class AudioBook(Book):
    """Класс аудиокниги с аргументом
        продолжительности duration"""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self.duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Неверный тип длительности книги")
        if new_duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        """Вывод всей информации о книге"""
        return f"Книга {self.name}. Автор {self.author}. Продолжительность{self._duration}"

    def __repr__(self):
        """Описываем поведение функции repr()"""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self._duration!r})"


if __name__ == '__main__':
    book_1 = Book("Название_1", "Автор_1")
    book_2 = PaperBook('Название_2', "Автор_2", 546)
    book_3 = AudioBook('Название_3', "Автор_3", 5.7)
    print(book_1)
    print(book_2)
    print(book_3)
    print(repr(book_1))
    print(repr(book_2))
    print(repr(book_3))



class Auto:
    """Класс автомобиль. Имеет атрибуты - бренд, трансмиссия, цвет, количество колёс"""
    def __init__(self, brand: str, transmission: str, color: str, wheels: int):
        self._brand = brand  # закрываем доступ извне класса
        self._transmission = transmission  # закрываем доступ извне класса
        self._color = color  # закрываем доступ извне класса
        self._wheels = wheels  # закрываем доступ извне класса

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, new_brand: str) -> None:
        if not isinstance(new_brand, str):
            raise TypeError('Переменная должна быть строчного типа')
        self._brand = new_brand

    @property
    def transmission(self) -> str:
        return self._transmission

    @transmission.setter
    def transmission(self, new_transmission: str) -> None:
        if not isinstance(new_transmission, str):
            raise TypeError('Переменная должна быть строчного типа')
        if new_transmission.lower() not in ['auto', 'automatical', 'mech', 'mechanical']:
            raise ValueError("Тип трансмиссии должен быть выбран из: ['auto', 'automatical', 'mech', 'mechanical']")
        self._transmission = new_transmission

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        if not isinstance(new_color, str):
            raise TypeError('Переменная должна быть строчного типа')
        self._color = new_color

    @property
    def wheels(self) -> int:
        return self._wheels

    @wheels.setter
    def wheels(self, new_wheels: int) -> None:
        if not isinstance(new_wheels, int):
            raise TypeError('Переменная должна быть целочесленная')
        if new_wheels <= 0:
            raise ValueError("Количество колёс должно быть положительным числом")
        self._wheels = new_wheels

    def __str__(self):
        """Вывод всей информации о книге"""
        return f"Автомобиль {self._brand}. Трансмиссия {self._transmission}. " \
               f"Цвет {self._color}. Количество колес {self._wheels}"

    def __repr__(self):
        """Описываем поведение функции repr()"""
        return f"{self.__class__.__name__}(brand={self._brand!r}, transmission=" \
               f"{self._transmission!r}, color={self._color!r}, wheels={self._wheels!r})"

    def first_method(self) -> None:
        """Метод возвращает модели машин, соответствующих введённым параметрам"""
        ...

    def second_method(self) -> int:
        """Метод возвращает количество колес в машине с учетом запасных"""
        return self._wheels + 1


class Track(Auto):
    """Класс грузового автомобиля. Имеет дополнительный атрибут - масса."""
    def __init__(self, brand, transmission, color, wheels, weight: float):
        super().__init__(brand, transmission, color, wheels)
        self._weight = weight

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, new_weight: int) -> None:
        if not isinstance(new_weight, int):
            raise TypeError('Переменная должна быть числом с плавающей точкой')
        if new_weight <= 0:
            raise ValueError("Масса должна быть положительным числом")
        self._wheels = new_weight

    def __str__(self):
        """Вывод всей информации о книге"""
        return f"Автомобиль {self._brand}. Трансмиссия {self._transmission}. " \
               f"Цвет {self._color}. Количество колес {self._wheels}. Масса {self._weight}"

    def __repr__(self):
        """Описываем поведение функции repr()"""
        return f"{self.__class__.__name__}(brand={self._brand!r}, transmission=" \
               f"{self._transmission!r}, color={self._color!r}, " \
               f"wheels={self._wheels!r}, weight={self._weight!r})"

    def second_method(self) -> int:
        """Изменены выходные значения в связи с увеличением запасных колёс
        для грузовых автомобилей"""
        return self._wheels + 2


if __name__ == "__main__":
    auto = Auto('Volkswagen', 'mech', 'blue', 4)
    auto_2 = Track('Caterpillar', 'Mech', 'yellow', 8, 15.7)
    print(auto)
    print(auto_2)
    print(repr(auto))
    print(repr(auto_2))

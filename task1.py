# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
class Chair:
    def __init__(self, chair_legs: int, material: str, quantity: int) -> None:
        """
        Создание и подготовка к работе объекта "Стул"
        :param chair_legs: Количество ножек стула
        :param material: Материал стула
        :param quantity: Количество заказываемых стульев
        Примеры:
        >>> chair = Chair(4, 'wood', 30)  # инициализация экземпляра класса
        """
        if not isinstance(chair_legs, int):
            raise TypeError("Value must be 'integer'")
        if chair_legs < 2:
            raise ValueError(f"Количество ножек не может быть меньше 2")
        self.chair_legs = chair_legs
        if not isinstance(material, str):
            raise TypeError("Value must be 'string'")
        self.material = material
        if not isinstance(quantity, int):
            raise TypeError("Value must be 'integer'")
        if quantity < 0:
            raise ValueError(f"Количество стульев не может быть отрицательным числом")
        self.quantity = quantity
    def raise_quantity(self, new_quantity: int) -> None:
        """
        Изменяем количество заказываемых стульев
        :param new_quantity: Новое количество стульев(добавляем - положитеьное, убираем - отрицательное)
        :raise ValueError: Если новое количество заказываемыех стульев отрицательно, то вызываем ошибку
        Примеры:
        >>> chair = Chair(4, 'wood', 30)
        >>> chair.raise_quantity(4)
        """
        if not isinstance(new_quantity, int):
            raise TypeError("Value must be 'integer'")
        if self.quantity + new_quantity >= 0:
            self.quantity += new_quantity
        else: raise ValueError(f"Вы не можете заказать отрицательное количество стульев")
    def change_material(self, new_material: str) -> None:
        """
        Изменяем материал заказываемых стульев
        :param new_material: Новый материал стульев
        Примеры:
        >>> chair = Chair(4, 'wood', 30)
        >>> chair.change_material('steel')
        """
        if not isinstance(new_material, str):
            raise TypeError("Value must be 'string'")
        self.material = new_material

class Mouse:
    def __init__(self, color: Union[str, list], wire: bool) -> None:
        """
        Создание и подготовка к работе объекта "Мышь"
        :param color: Цвет
        :param wire: Тип 'проводная' или 'беспроводная'
        Примеры:
        >>> mouse = Mouse('rainbow', True)  # инициализация экземпляра класса
        """
        if not isinstance(color, (str, list)):
            raise TypeError("Value must be 'string' or 'list'")
        self.color = color
        if not isinstance(wire, bool):
            raise TypeError("Value must be 'boolean'")
        self.wire = wire
    def change_color(self, new_color: Union[str, list]) -> None:
        """
        Изменяем цвет мыши
        :param new_color: Новый цвет мыши
        Примеры:
        >>> mouse = Mouse('rainbow', True)
        >>> mouse.change_color('red')
        """
        if not isinstance(new_color, (str, list)):
            raise TypeError("Value must be 'string' or 'list'")
        self.color = new_color
    def change_mouse_type(self, new_wire: bool) -> None:
        """
        Изменяем тип мыши
        :param new_wire: Наличие провода
        Примеры:
        >>> mouse = Mouse('rainbow', True)
        >>> mouse.change_mouse_type(False)
        """
        if not isinstance(new_wire, bool):
            raise TypeError("Value must be 'boolean'")
        self.wire = new_wire

class Laser:
    def __init__(self, wavelangth: Union[int, float], power: Union[int, float], mode:str) -> None:
        """
        Создание и подготовка к работе объекта "Лазер"
        :param wavelangth: Длина волны лазера
        :param power: Мощность накачки лазера
        :param mode: Режим работы 'импульсный' или 'непрервный'
        Примеры:
        >>> laser = Laser(532, 1, 'Pulse')  # инициализация экземпляра класса
        """
        if not isinstance(wavelangth, (int, float)):
            raise TypeError("Value must be 'integer' or 'float'")
        if not 200 < wavelangth < 2000:
            raise ValueError(f"Мы не умеем изготавливать лазер на {wavelangth} длину волны")
        self.wavelength = wavelangth
        if not isinstance(power, (int, float)):
            raise TypeError("Value must be 'integer' or 'float'")
        self.power = power
        if power < 0:
            raise ValueError('What??? Incorrect value')
        if not isinstance(mode, str):
            raise TypeError("Value must be 'string'")
        self.mode = mode
    def change_mode(self, new_mode: str) -> None:
        """
        Изменяем режим работы
        :param new_mode: Новый режим работы
        :raise ValueError: Если новое режим работы не соответствует заданным
        Примеры:
        >>> laser = Laser(532, 1, 'Pulse')
        >>> laser.change_mode('Direct')
        """
        if not isinstance(new_mode, str):
            raise TypeError("Value must be 'string'")
        if new_mode.lower() == 'direct' or new_mode.lower() == 'pulse':
            self.mode = new_mode
        else: raise ValueError("You may choose between 'Direct' or 'Pulse' modes")
    def change_power(self, new_power: Union[int, float]) -> None:
        """
        Изменяем мощность накачки
        :param new_mode: Новый мощность накачки
        :raise ValueError: Если новая мощность накачки отрицательна
        Примеры:
        >>> laser = Laser(532, 1, 'Pulse')
        >>> laser.change_power(1.5)
        """
        if not isinstance(new_power, (int, float)):
            raise TypeError("Value must be 'integer' or 'float'")
        if new_power < 0:
            raise ValueError('What??? Incorrect value')
        self.power = new_power

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod() # тестирование примеров, которые находятся в документации

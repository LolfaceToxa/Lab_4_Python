class Auto:
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if isinstance(color, str):
            self.__color = color
        else:
            print("Цвет должен быть строкой!")

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        if isinstance(mark, str):
            self.__mark = mark
        else:
            print("Марка должна быть строкой!")

    @property
    def fuel(self):
        return self.__fuel

    @fuel.setter
    def fuel(self, fuel):
        if isinstance(fuel, bool):
            self.__fuel = fuel
        else:
            print("Наполненность бака должна быть строкой 1/0 (True/False)!")

    def __init__(self, color="зелёный", mark="Audi", fuel=True):  # конструктор с параметрами/по умолчанию
        self.color = color
        self.mark = mark
        self.fuel = fuel
        print("Конструктор Auto")

    def __del__(self):  # деструктор
        print(self.__str__(), " - удален из памяти")

    # методы класса
    def drive(self):
        if self.fuel is True:
            print("Вы прокатились в ветерком")
            self.fuel = False
        else:
            print("Надо заправиться")

    def refuel(self):
        self.fuel = True
        print("Вы заправились/дозаправились")

    def __str__(self):  # вывод информации об объекте
        return f"Цвет авто: {self.color} \t Марка: {self.mark} \t Наличие топлива в авто: {self.fuel}"

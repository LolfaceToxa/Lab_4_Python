class Machine:
    @property
    def system(self):
        return self.__system

    @system.setter
    def system(self, system):
        if isinstance(system, str):
            self.__system = system
        else:
            print("ID должно быть натуральным числом!")

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID):
        if isinstance(ID, int) and ID > 0:
            self.__ID = ID
        else:
            print("ID должно быть натуральным числом!")

    def __init__(self, system="Windows", ID=1):  # конструктор с параметрами/по умолчанию
        self.system = system
        self.ID = ID
        print("Конструктор Machine")

    def __del__(self):  # деструктор
        print(self.__str__(), " - удален из памяти")

    # методы класса
    def __str__(self):  # вывод информации об объекте
        return f"ОС: {self.system} \t ID аппаратуры: {self.ID}"

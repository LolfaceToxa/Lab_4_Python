from random import randint
from time import sleep
from Worker import Worker
from Auto import Auto


class Boss(Worker, Auto):
    @property
    def numOfEmployees(self):
        return self.__numOfEmployees

    @numOfEmployees.setter
    def numOfEmployees(self, num):
        if isinstance(num, int) and num > 0:
            self.__numOfEmployees = num
        else:
            print("Число подчинённых должно быть натуральным числом")

    def __init__(self, surname="Иванов", salary=45000, status="работяга",
                 system="Windows", ID=1, numOfEmployees=10, color="зелёный", mark="Audi",
                 fuel=True):  # конструктор с параметрами/по умолчанию
        Worker.__init__(self, surname, salary, status, system, ID)
        Auto.__init__(self, color, mark, fuel)
        self.numOfEmployees = numOfEmployees
        print("Конструктор Boss")

    def __del__(self):  # деструктор
        print(self.__str__(), " - удален из памяти")

    # методы класса
    def rank_up(self):
        self.status = "босс"

    def try_money(self):
        print("Босс затеял авантюру...")
        sleep(2.5)
        x = randint(0, 10)
        if x < 5:
            print("План провалился, деньги были потеряны.. =(")
            self.salary = round(self.salary * 0.5, 2)
        else:
            print("План удался, деньги были заработаны! =)")
            self.salary = round(self.salary * 2, 2)

    def drive(self):
        if self.fuel is True:
            print(f"{self.surname} прокатился с ветероком")
            self.fuel = False
        else:
            print("Надо заправиться")

    def __str__(self):  # вывод информации об объекте
        return f"Фамилия: {self.surname} \t Зарплата: {self.salary} \t Должность: {self.status} \tКоличество подчинённых: {self.numOfEmployees} \t" \
               f"Цвет авто: {self.color} \t Марка: {self.mark} \t Наличие топлива в авто: {self.fuel} \t" \
               f"ОС: {self.system} \t ID аппаратуры: {self.ID}"

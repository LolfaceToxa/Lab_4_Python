from Machine import Machine


class Worker(Machine):
    # поля класса
    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname
        else:
            print("Название должно быть строкой!")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if (isinstance(salary, int) or isinstance(salary, float)) and salary > 0:
            self.__salary = salary
        else:
            print("Зарплата должна быть натуральным числом!")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if isinstance(status, str):
            self.__status = status
        else:
            print("Статус должнен быть строкой!")

    # конструкторы, деструкторы
    def __init__(self, surname="Иванов", salary=45000, status="рабочий",
                 system="Windows", ID=1):  # конструктор с параметрами/по умолчанию
        Machine.__init__(self, system, ID)
        self.status = status
        self.salary = salary
        self.surname = surname
        print("Конструктор Worker")

    def __del__(self):  # деструктор
        print(self.__str__(), " - удален из памяти")

    # методы класса
    def salary_up(self):  # Увеличить оклад на 15%
        self.salary = round(self.salary * 1.15, 2)

    def engineer(self):  # Работникам, у которых фамилия начинается с сочетания букв «Иван»,
        if len(self.surname) >= 4:
            if "Иван" in self.surname[:4]:  # присвоить должность «инженер».
                self.status = "инженер"

    def __str__(self):  # вывод информации об объекте
        return f"Фамилия: {self.surname} \t Зарплата: {self.salary} \t Должность: {self.status} \t" \
               f"ОС: {self.system} \t ID аппаратуры: {self.ID}"

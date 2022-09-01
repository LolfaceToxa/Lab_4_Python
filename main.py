from Worker import Worker
from Auto import Auto
from Boss import Boss
from Machine import Machine
import unittest


def enter_int():  # проверка ввода натуральных чисел
    while True:
        try:
            x = int(input())
            if x < 0:
                raise ValueError
            break
        except IndentationError as e:
            print(e)
        except TypeError as t:
            print(t)
        except ValueError as v:
            print(v)
        except:
            print("Ошибка ввода")
    return x


def enter():
    while True:
        try:
            x = input()
            break
        except IndentationError as e:
            print(e)
        except:
            print("Ошибка ввода")
    return x


def enter_bool():
    t_yes = ("да", "yes")
    t_no = ("нет", "no")
    while True:
        try:
            x = input().lower()
            if x in t_yes:
                answer = True
                break
            elif x in t_no:
                answer = False
                break
            else:
                raise ValueError
        except ValueError:
            print("Вы не ввели требумое значение(оно указано в скобках)")
        except:
            print("Ошибка ввода")
    return answer

# 1 - индивидуальное задание
# human1 = Worker()
#
#
# print("Ввод данных обычного сотрудника\n_____________________________________________")
# print("Введите фамилию сотрудника: ")
# sur = enter()
# print("Введите зарплату сотрудника: ")
# sal = enter_int()
# print("Введите должность сотрудника: ")
# stat = enter()
# print("Введите ОС аппаратуры сотрудника")
# system = enter()
# print("Введите ID аппаратуры сотрудника")
# ID = enter_int()
#
# human2 = Worker(sur, sal, stat, system, ID)
#
# print("Ввод данных сотрудника(Worker)\n_____________________________________________")
# print("Введите фамилию сотрудника: ")
# sur = enter()
# print("Введите зарплату сотрудника: ")
# sal = enter_int()
# print("Введите должность сотрудника: ")
# stat = enter()
# print("Введите ОС аппаратуры сотрудника")
# system = enter()
# print("Введите ID аппаратуры сотрудника")
# ID = enter_int()
#
# human3 = Worker(sur, sal, stat, system, ID)
#
#
# print(human1)
# print(human2)
# print(human3)
#
# humanity = (human1, human2, human3)
# for human in humanity:
#     human.engineer()
#     human.salary_up()
# 2 - система классов
# print("Ввод данных сотрудника(Worker)\n_____________________________________________")
# print("Введите фамилию сотрудника: ")
# sur = enter()
# print("Введите зарплату сотрудника: ")
# sal = enter_int()
# print("Введите должность сотрудника: ")
# stat = enter()
# print("Введите ОС аппаратуры сотрудника")
# system = enter()
# print("Введите ID аппаратуры сотрудника")
# ID = enter_int()
#
# work1 = Worker(sur, sal, stat, system, ID)
# print(work1.__str__())
# print("_____________________________________________")
#
# work1.salary_up()
# work1.engineer()
# print(work1.__str__())
#
# print("Ввод данных начальника(Boss)\n_____________________________________________")
# print("Введите фамилию сотрудника: ")
# sur = enter()
# print("Введите зарплату сотрудника: ")
# sal = enter_int()
# print("Введите должность сотрудника: ")
# stat = enter()
# print("Введите ОС аппаратуры сотрудника: ")
# system = enter()
# print("Введите ID аппаратуры сотрудника: ")
# ID = enter_int()
# print("Введите количество подчинённых сотрудника: ")
# numOE = enter_int()
# print("Введите марку автомобиля начальника:")
# mark = enter()
# print("Введите цвет машины начальника")
# color = enter()
# print("Машина начальника заправлена?(да/нет;yes/no)")
# fuel = enter_bool()
#
# work2 = Boss(sur, sal, stat, system, ID, numOE, color, mark, fuel)
#
# print(work2.__str__())
#
# print("_____________________________________________")
#
# work2.rank_up()
# work2.try_money()
# work2.drive()
# work2.refuel()
# work2.drive()
#
# print(work2.__str__())
#
# print("_____________________________________________")
# 3 ввод/вывод бинарников
# import os
# import pickle
#
# machine1 = "machine.dat"
# worker1 = "worker.dat"
# auto1 = "auto.dat"
# boss1 = "boss.dat"
#
# class NonExistance(Exception): #пользовательское исключение
#     pass
#
# def load(t, i): #проверка файлов
#     try:
#         if os.path.exists(t):
#             with open(t, "rb") as file:
#                 print(f"{t} был открыт")
#                 lst[i] = pickle.load(file)
#                 for entity in lst[i]:
#                     print(entity)
#         else:
#             with open(t, "ab") as file:
#                 print(f"{t} был создан")
#     except IOError:
#         print("Ошибка чтения файла")
#
# def save(t, i):
#     try:
#         if os.path.exists(t) is False:
#             raise NonExistance
#         with open(t, "wb") as file:
#             print(f"{t} был открыт")
#             for entity in lst[i]:
#                 print(entity)
#             pickle.dump(lst[i], file)
#     except NonExistance as n:
#         print(n)
#     except IOError:
#         print("Ошибка чтения файла")
#
#
# lst = {'machine': [], 'worker': [], 'auto': [], 'boss': []}
# # load(machine1, 'machine')
# load(worker1, 'worker')
# # load(auto1, 'auto')
# # load(boss1, 'boss')
#
#
#
# bin1 = Worker()
# lst['worker'].append(bin1)
# bin2 = Worker()
# lst['worker'].append(bin2)
# save(worker1, 'worker')

# 4 тесты
#
# class Test(unittest.TestCase):
#
#     example = Auto("красный", "Renault", 2)
#
#     def test_color(self):
#         self.assertTrue(self.example.color, msg="Название не может быть пустой строкой")
#
#     def test_mark(self):
#         self.assertTrue(self.example.mark, msg="Название не может быть пустой строкой")
#
#     def test_fuel(self):
#         self.assertTrue(isinstance(self.example.fuel, bool), msg="Некорректное значение топлива")
#
#
# if __name__ == "__main__":
#     unittest.main()

bos = Boss()

bos+123
print(bos)
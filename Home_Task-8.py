# class MyClass:
#     @staticmethod
#     def on_sum_1(param_1, param_2):
#         return param_1 + param_2
#     def on_sum_2(self, param_1, param_2):
#         return param_1 + param_2
#     def on_sum_3(self, param_1, param_2):
#         return MyClass.on_sum_1(param_1, param_2)
#
# # print(MyClass.on_sum_1(20,30))
#
# mc = MyClass()
# print(mc.on_sum_2(10,20))
# print(mc.on_sum_1(40,30))
# print(mc.on_sum_3(50,50))

# Task 1

# class Data:
#     def __init__(self, a):
#         self.a = a
#     @staticmethod
#     def on_valid(a):
#         a = a.replace('-',' ').split()
#         d = []
#         for i in a:
#             i = int(i)
#             d.append(i)
#         if d[0] > 31:
#             print('Введен несуществующий день месяца')
#             b = None
#         else:
#             b = d[0]
#         if d[1] > 12:
#             print('Введен несуществующий месяц года')
#             c = None
#         else:
#             c = d[1]
#         if d[2] > 2100:
#             print('Введен несуществующий год')
#             e = None
#         else:
#             e = d[2]
#         print(f'Введенная дата - {b}, месяц - {c}, год - {e}')
#
#     @classmethod
#     def on_data(cls, a):
#         a = a.replace('-', ' ').split()
#         d = []
#         for i in a:
#             i = int(i)
#             d.append(i)
#         print(f'Введенная дата - {d[0]}, месяц - {d[1]}, год - {d[2]}')
#
# print(Data.on_valid('33-13-2101'))
# Data.on_data('31-12-2020')

# Task 2


# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# inp_data1 = input("Введите делимое: ")
# inp_data2 = input("Введите делитель: ")
#
# try:
#     inp_data1 = int(inp_data1)
#     inp_data2 = int(inp_data2)
#     res = inp_data1 / inp_data2
# except ZeroDivisionError:
#     print("На 0 делить нельзя!")
# else:
#     print(f"Все хорошо. Результат: {res:.2f}")
# finally:
#     print("Программа завершена")

# Task 3


# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
# d = []
# inp_data = 0
# while inp_data != 'stop':
#     inp_data = input("Введите любое число. Для прекращения ввода наберите 'stop': ")
#     try:
#         inp_data = float(inp_data)
#         d.append(inp_data)
#         if inp_data == 'stop':
#             print("Программа завершена")
#             break
#     except ValueError:
#         print("Введено не число")
# print(d)

# Task 4 - 6

# class WarehouseOT:
#     def __init__(self, name):
#         self.name = name
#         print(f'Название склада: {self.name}')
#     def send(self, sname, scount):
#         self.sname = sname
#         self.scount = scount
#         if self.scount == int:
#             print(f'Отправка {self.sname} в количестве {self.scount} шт. в подразделение компании.')
#         else:
#             print('Количество должно быть указано в виде ЧИСЛА')
#     def intake(self, pname, pcount):
#         self.pname = pname
#         self.pcount = pcount
#         if self.pcount == int:
#             print(f'Прием {self.pname} в количестве {self.pcount} шт. на склад.')
#         else:
#             print('Количество должно быть указано в виде ЧИСЛА')
#
# class OT(WarehouseOT):
#     def __init__(self, count_shelf, heigh_shelf):
#         self.count_shelf = count_shelf  # количество полок в ряду
#         self.heigh_shelf = heigh_shelf # кол-во полок в ряд
#         print(f'Параметры склада: кол-во полок в ряду {count_shelf}, кол-во полок в ряд {heigh_shelf}')
#     @staticmethod
#     def spisok_ot(name, price, count, owner):
#         my_dict = {'Название': name, 'Цена': price, 'Количество': count, 'Владелец': owner}
#         print(my_dict)
#
# class Printer(OT):
#     def __init__(self, count_shelf, heigh_shelf, count, heigh):
#         OT.__init__(self, count_shelf, heigh_shelf)
#         if self.count_shelf > count and self.heigh_shelf > heigh:
#             print(f'Параметры склада по размещению принтеров: всего полок в ряду {count}, всего полок в ряд {heigh}')
#         else:
#             print('Склад переполнен. Принтеры разместить негде.')
#     def printer_p(self, name, price, count, owner):
#         return OT.spisok_ot(name, price, count, owner)
#
#
# class Scaner(OT):
#     def __init__(self, count_shelf, heigh_shelf, count, heigh):
#         OT.__init__(self, count_shelf, heigh_shelf)
#         if self.count_shelf > count and self.heigh_shelf > heigh:
#             print(f'Параметры склада по размещению сканеров: кол-во полок в ряду {count}, кол-во полок в ряд {heigh}')
#         else:
#             print('Склад переполнен. Сканеры разместить негде.')
#     def scaner_p(self, name, price, count, owner):
#         return OT.spisok_ot(name, price, count, owner)
#
# class Xeroxs(OT):
#     def __init__(self, count_shelf, heigh_shelf, count, heigh):
#         OT.__init__(self, count_shelf, heigh_shelf)
#         if self.count_shelf > count and self.heigh_shelf > heigh:
#             print(f'Параметры склада по размещению ксероксов: кол-во полок в ряду {count}, кол-во полок в ряд {heigh}')
#         else:
#             print('Склад переполнен. Ксероксы разместить негде.')
#     def xerox_p(self, name, price, count, owner):
#         return OT.spisok_ot(name, price, count, owner)
#
# wot = WarehouseOT('O&T')
# pr = Printer(10, 5, 6, 2)
# pr.printer_p('HP', 100, 10, 'IBM')
# pr.send('Принтер', 2)
# pr.send('Принтер', 'фы')
# pr.intake('Принтер', 2)
# pr.intake('Принтер', 'qw')
# sc = Scaner(10, 5, 2, 2)
# sc.scaner_p('Xerox', 50, 5, 'SC')
# xr = Xeroxs(10, 5, 2, 1)
# xr.xerox_p('Samsung', 150, 3, 'DS')

# Task 7

# class ComplexDigit:
#     def __init__(self, nums1, nums2):
#         self.nums = complex(nums1, nums2)
#
#     def __str__(self):
#         return self.nums
#
#     def __add__(self, other):
#         return f'Сумма комплексных чисел: {self.nums + other.nums}'
#
#     def __mul__(self, other):
#         return f'Произведение комплексных чисел: {self.nums * other.nums}'
#
#
# cell_1 = ComplexDigit(2, 1)
# cell_2 = ComplexDigit(7, 5)
# print(cell_1 + cell_2)
# print(cell_1 * cell_2)
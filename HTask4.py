# Start

# Task 1 Разобраться с запуском скрипта с параметрами
# var1
# def salary(h, s, p):
# #    S = h*s + p
#     return h*s + p
# print(salary(170, 1000, 30000))

# var2
# a, b, c = 170, 1000, 20000
# print('Зарплата сотрудника с учетом премии составляет: ', a*b + c)

# var3

# from sys import argv
# S = int(argv[1])*int(argv[2]) + int(argv[3])
# print(f'Зарплата сотрудника с часовой ставкой {argv[1]}, отработавшего {argv[2]} часов и премией {argv[3]} равна', S)


# Task 2 Не смог использовать генератор

# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 555]
# new_list = []
# for num, val in enumerate(my_list):
#     if len(my_list) > (num + 1):
#         if my_list[num + 1] > my_list[num]:
#             new_list.append(my_list[num + 1])
# print(new_list)

# print(my_list)
# c = len(my_list)
# i = 0
# b = 1
# summer = []
# while i <= (c-2):
#     if my_list[i] < my_list[b]:
#         summer.append(my_list[b])
#     i += 1
#     b += 1
# print(summer)

# Task 3

# print('Числа, кратные 20 или 21 в интервале от 20 до 241: ', [n for n in range(20, 241) if n % 20 == 0 or n % 21 == 0])

# Task 4

# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# print([n for n in my_list if my_list.count(n) == 1])

# Task 5

# from functools import reduce
# my_list = [n for n in range(100, 1001) if n % 2 == 0]
# print(my_list)
# res = reduce((lambda x, y: x * y), my_list)
# print(res)

# Task 6
# 1 часть
# from itertools import count
# a = int(input('Введите стартовое число: '))
# b = int(input('Введите завершающее число: '))
# for el in count(a):
#     if el > b:
#         break
#     else:
#         print(el)

# 2 часть

# from itertools import cycle
# a = input('Введите любую последовательность элементов. При завершении нажмите Enter: ')
# c = int(input('Введите число повторений элементов: '))
# b = 0
# for el in cycle(a):
#     if b > c:
#         break
#     else:
#         print(el)
#         b += 1

# Task 7

# from math import factorial
# n = int(input('Введите число, возводимое в факториал: '))
# numb_fact = []
# def fact(n):
#     for el in range(n):
#         yield el
# for el in fact(n + 1):
#     numb_fact.append(el)
# numb_fact.remove(0)
# print('Элементы факториала: ', numb_fact)
# print(f'Факториал числа {n} равен', factorial(n))
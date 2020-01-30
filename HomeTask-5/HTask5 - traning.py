# Task 1

# print('Программное создание файла, запись в него построчных данных, вводимых пользователем. Пустая строка - окончание ввода.')
# i = 1
# c = []
# while i > 0:
#     a = input('Введите буквы, слова, словосочетания, фразы и т.д.: ')
#     b = '\n'
#     b1 = a + b
#     i = len(a)
#     f = open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-1.txt", "a")
#     c.append(b1)
# print('Окончание ввода данных.')
# f.writelines(c)
# f.close()

# Task 2

# print('Создать текстовый файл (не программно). Сохранить в нем несколько строк. Выполнить подсчет количества строк, количества слов в каждой строке.')
# i = 1
# with open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-2.txt", "r") as f_task2:
#     for line in f_task2:
#         print(line)
#         b = line.split(' ')
#         print(f'Количество слов в строке {i} равно {len(b)}')
#         i +=1
# f = open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-2.txt")
# count = sum(1 for line in f)
# print(f'Общее количество строк в файле {count}')
# f.close()

# Task 3

# print('Создать текстовый файл (не программно), в котором построчно записаны фамилии сотрудников и величина их окладов. Определить кто из'
#       'сотрудников имеет окдал менее 20 тыс. руб. - вывести их фамилии. Рассчитать средний оклад.')
# print(open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-3.txt").read())
# f = dict()
# with open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-3.txt", 'r') as f_task3:
#       for line in f_task3:
#             line = line.rstrip()
#             line = list(line.split(' '))
#             f.update([line])
# s = open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-3.txt")
# count = sum(1 for line in s)
# a = [k for k, v in f.items() if float(v) < 20000]
# print('Сотрудники с окладом меньше 20 000: ', a)
# total = 0
# for v in f.values():
#       total += float(v)
#       total1 = total / count
# print(f'Средняя зарплата {count} сотрудников составляет {total1:.2f}')

# Task 4

# print('Создать текстовый файл (не программно). Написать программу, открывающую файл на чтение и считывающую построчно данные.\n'
#       'При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.')
# my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# f = open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-4-1.txt", "w")
# f.close()
# c = []
# with open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-4.txt", "r") as f_task4:
#     for line in f_task4:
#         print(line)
#         b = line.split(' ')
#         print(b)
#         for key in my_dict.keys():
#               if key == b[0]:
#                     b.pop(0)
#                     b.insert(0, my_dict[key])
#                     f = open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-4-1.txt", "a")
#                     f.writelines(b)
#                     f.close()
# print('Произведена замена английских числительных на русские.')

# Task 5

# print('Программное создание файла, запись в него набора чисел, вводимых пользователем. Подсчет суммы чисел и вывод на экран.')
# d = open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-5.txt", "w")
# d.close()
# a = input('Введите числа, разделенные пробелами: ')
# print(a)
# f = open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-5.txt", "a")
# print('Окончание ввода чисел.')
# f.write(a)
# b = a.split(' ')
# print(b)
# for n in b:
#     n = float(n)
#     n += n
# print('Сумма введенных чисел: ', n)
# f.close()

# Task 6

# print('Создать текстовый файл (не программно). Каждая строка описывает учебный предмет: лекции, практики, лабораторные. Сформировать словарь и общее кол-во занятий по нему.')
#
# print(open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-6.txt").read())
# f = dict()
# with open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-6.txt", 'r') as f_task6:
#       for line in f_task6:
#             line = line.rstrip()
#             line = list(line.split(' '))
#             b = line[1] + line[2] + line[3]
#             d = b.replace('(л)', ' ')
#             d = d.replace('(пр)', ' ')
#             d = d.replace('(лаб)', ' ')
#             d = d.replace('-', '', 3)
#             d = d.strip()
#             d = d.split(' ')
#             S = 0
#             for i in d:
#                 S += int(i)
#             c = (line[0][:-1], S)
#             f.update([c])
# print(f)

# Task 7

# import json
#
# print('Создать текстовый файл (не программно. Каждая строка содержит данные о фирме: название, ОПФ, выручка, издержки. '
#       'I ЧАСТЬ. Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила '
#       'убытки, в расчет средней прибыли ее не включать.'
#       'II ЧАСТЬ. Список, словарь с фирмами и их прибылями, указать среднюю прибыль. Если фирма получила убытки, то ее также включить.'
#       'Итоговый файл сохранить в виде JSON-объекта.')
# s = open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-7.txt")
# count = sum(1 for line in s)
# print(open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-7.txt").read())
# a = dict()
# b = dict()
# f = 'average_profit:'
# e = list()
# h = list()
# with open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-7.txt", 'r') as f_task7:
#       for line in f_task7:
#             line = line.rstrip()
#             line = list(line.split(' '))
#             c = int(line[2]) - int(line[3])
#             d = {line[0]: c}
#             a.update(d)
#             if c > 0:
#                   e.append(c)
#             g = sum(e)
#             g1 = g / count
#             h.append(c)
#             g2 = sum(h) / count
# k = {f, g1}
# k1 = {f, g2}
# S = [a, k1]
# print('I ЧАСТЬ')
# print([a, k])
# print('II ЧАСТЬ')
# print(S)
# k2 = (f, g2)
#
# with open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-7-1.json", "w") as write_f:
#     json.dump(a, write_f)
#
# with open(r"/home/vyacheslav/Рабочий стол/Data Scientist/Основы Python/my_task5-7-1.json", "a") as write_f:
#       json.dump(k2, write_f)

# Загрузка на GitHub
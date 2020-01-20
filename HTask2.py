# Task 1

# my_list = [2, 'text', 456, 45.3, None, False, [1,2,3]]
# for el in my_list:
#     print(type(el))

# Task 2

# my_list = []
# q = ''
# while q != 'y':
#     q = input('Введите любой текст/число. Для прекращения ввода введите y')
#     my_list.append(q)
#     continue
# my_list.pop()
# print(my_list)
# # print(len(my_list))
# my_list_new = []
# list_val = []
# # print(my_list)
# # print(my_list_new)
# i = 1
# while i <= (len(my_list) - 1):
#     list_val.append(i)
#     i = i + 2
# # print(list_val)
# n = 0
# m = 1
# if len(my_list) % 2 != 0:
#     while n <= (len(my_list) - 3):
#         list_val.insert(m, n)
#         m = m + 2
#         n = n + 2
#     # print(list_val)
# else:
#     while n <= (len(my_list) - 2):
#         list_val.insert(m, n)
#         m = m + 2
#         n = n + 2
#     # print(list_val)
# s = 0
# if len(my_list) % 2 == 0:
#     while s <= (len(my_list) - 1):
#         my_list_new.insert(s, my_list[list_val[s]])
#         s = s + 1
# else:
#     while s <= (len(my_list) - 2):
#         my_list_new.insert(s, my_list[list_val[s]])
#         s = s + 1
# if len(my_list) % 2 != 0:
#     my_list_new.append(my_list[len(my_list) - 1])
#     print(my_list_new)
# else:
#     print(my_list_new)

# Task 3

# a = int(input('Введите месяц в виде числа: '))
# win = [12, 1, 2]
# spr = [3, 4, 5]
# sum = [6, 7, 8]
# aut = [9, 10, 11]
# if a in win:
#     print('Вы ввели зимний месяц')
# if a in spr:
#     print('Вы ввели весенний месяц')
# if a in sum:
#     print('Вы ввели летний месяц')
# if a in aut:
#     print('Вы ввели осенний месяц')
# Решение через словарь
# a = int(input('Введите месяц в виде числа: '))
# my_dict_VG = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
# print(my_dict_VG)
# for k in my_dict_VG:
#     c = my_dict_VG.get(k)
#     if a in c:
#         print('Вы ввели месяц времени года ', k)

# Task 4

# a = input('Введите несколько слов. В качестве разделителя используйте пробел: ')
# b = a.split(' ')
# print(b)
# for ind, el in enumerate(b, 1):
#     print(ind, el[0:10])

# Task 5

# my_list = [7, 5, 3, 2]
# a = ''
# while a != 0:
#     a = int(input('Введите рейтинг ученика от 1 до 9 включительно. Для прекращения ввода введите 0: '))
#     my_list.append(a)
#     continue
# my_list.sort(reverse=True)
# my_list.pop()
# print(my_list)

# Task 6

# a = int(input('Введите количество товаров: '))
# i = 1
# my_list_fin = list()
# my_dict_new = list()
# while i <= a:
#     my_dict = {'Название': ' ', 'Цена': ' ', 'Количество': ' ', 'Ед.изм.': ' '}
#     b = input('Введите НАЗВАНИЕ товара: ')
#     my_dict.update({'Название':b})
#     c = input('Введите цену товара: ')
#     my_dict.update({'Цена':c})
#     d = input('Введите количество товара: ')
#     my_dict.update({'Количество':d})
#     e = input('Введите ед.изм. товара: ')
#     my_dict.update({'Ед.изм.':e})
#     my_korteg = (i, my_dict)
#     i += 1
#     my_list_fin.append(my_korteg)
#     my_dict_new.append(my_dict)
# print(my_list_fin)
# print(my_dict_new)
# resultdict = [{}]
# for x in my_dict_new:
#     for y in x:
#         if y in resultdict[0]:
#             resultdict[0][y].append(x[y])
#             resultdict[0][y].sort()
#         else:
#             resultdict[0][y]=[x[y]]
# f = list(set(resultdict[0].get('Ед.изм.')))
# resultdict[0].update({'Ед.изм.':f})
# print(resultdict)

# Комментарий для GITHub

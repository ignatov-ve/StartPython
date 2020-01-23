# Task 1

# def del_d():
#     try:
#         d1 = float(input('Введите первое число: '))
#         d2 = float(input('Введите второе число: '))
#         d3 = d1 / d2
#     except ZeroDivisionError:
#         print('Деление на 0 невозможно')
#         return
#     else:
#         return d3
# d3_val = del_d()
# print(f'Результат деления введенных числе: {d3_val:.2f}')

# Task 2

# name = ()
# last_n = ()
# born = ()
# city = ()
# mail = ()
# tel = ()
# def first_func(name, last_n, born, city, mail, tel):
#     name = input('Введите свое имя: ')
#     last_n = input('Введите свою фамилию: ')
#     born = input('Введите свой год рождения: ')
#     city = input('Введите свой город проживания: ')
#     mail = input('Введите свой адрес эл. почты: ')
#     tel = input('Введите свой номер телефона: ')
#     return name, last_n, born, city, mail, tel
# name, last_n, born, city, mail, tel = first_func(name, last_n, born, city, mail, tel)
# print(f'С нами работает пользователь: имя - {name}, фамилия - {last_n}, {born} года рождения, проживающий в городе {city}, контакты: почта - {mail}, телефон - {tel}')

# Task 3

# def my_func():
#     global var1, var2, var3, digit_new
#     var1 = int(input('Введите любое ПЕРВОЕ число: '))
#     var2 = int(input('Введите любое ВТОРОЕ число: '))
#     var3 = int(input('Введите любое ТРЕТЬЕ число: '))
#     digit = [var1, var2, var3]
#     digit.remove(min(digit))
#     b = sum(digit)
#     return b, digit
# num_sum, list_new = my_func()
# print(f'Пользователь ввел числа: {[var1, var2, var3]}')
# print('Максимальные числа: ', list_new)
# print('Сумма максимальных чисел: ', num_sum)

# Task 4

# x = input('Введите число, возводимое в степень: ')
# y = int(input('Введите степень - целое отрицательное число: '))
# i = abs(y)
# z = [x] * i
# res = 1
# for el in z:
#     el = int(el)
#     res *= el
# st = 1 / res
# print(f'Результат возведения числа {x} в степень {y} равен: ', st)

# Task 5

# d = list()
# n = -1
# while n <= 0:
#     a = str(input('Введите числа, разделитель - пробел. По окончании ввода нажмите Enter. Для продолжения - начинайте ввод. Для завершения - "/": '))
#     a = list(a)
#     n = int(str(a).find('/'))
#     for i in reversed(range(len(a))):
#         if a[i] == ' ':
#             del a[i]
#     for i in range(len(a)):
#         if a[i] == '/':
#             del a[i]
#     print(a)
#     res = 0
#     for el in a:
#         el = int(el)
#         res += el
#     print('Сумма введенных чисел равна: ', res)
#     d.append(res)
#     print(d)
# print('Общая сумма введенных чисел равна: ', sum(d))

# Task 6

# i = 0
# while i < 2:
#     def int_func():
#         a = input('Введите любое слово/ количество слов на латиннице: ')
#         b = a.title()
#         return b
#     b = int_func()
#     print(b)
#     i += 1
# ДЗ 1

# a = 4
# b = float(5)
# c = int(True)
# print(a)
# print(b)
# print(c)
# d = int(input('Введите любое число: '))
# print(d)
# e = float(input('Введите нецелое число вида "3.5":'))
# print(e)
# f = input('Введите любое слово (несколько слов): ')
# print(f)

# ДЗ 2

# a = int(input('Введите время в секундах (от 1 до 10000): '))
#
# if a == 0:
#     print('Время не может быть равно 0')
# if a < 0:
#     print('Время не может быть меньше 0')
# else:
#     b = a // 3600 # часы
#     c = a // 60 # минуты
#     e = a - b*3600 - c*60 # секунды
#     print(f"Введенное время в формате ЧЧ:ММ:СС: {b}:{c}:{e}")

# ДЗ 3

# a = input('Введите любое число от 0 до 10: ')
# b = int(a+a)
# c = int(a+a+a)
# e = int(a) + b + c
# print('Вычисление введенного пользователем числа N в формате N + NN + NNN', a, '+', b, '+', c, 'равно: ', e)

# ДЗ 4

# a = list(input('Введите любое целое положительное число: ')) # Должно быть так
# print(max(a))

# a = input('Введите любое целое положительное число от 1 до 99: ') # Но т.к. мы способы выше не проходили, то будет так
# i = 0
# b = int(a[i])
# c = int(a[i+1])
# if b > c:
#     print('Самое большое число: ', b)
# else:
#     print('Самое большое число: ', c)


# ДЗ 5

# a = int(input('Введите выручку Вашей фирмы: '))
# b = int(input('Введите издержки Вашей фирмы: '))
# if a > b:
#     print('Ваша фирма приносит прибыль')
#     c = (a - b) / a
#     print('Рентабельность выручки составляет: ', c)
#     d = int(input('Введите численность сотрудников Вашей фирмы: '))
#     e = (a - b) / d
#     print('Прибыль на одного сотрудника составляет: ', e)
# else:
#     print('Ваша фирма работает в убыток')


# ДЗ 6
# i = 0
# a = int(input('Введите количество КМ, которое пробежал спортсмен в 1-й день: '))
# b = int(input('Введите ЦЕЛЕВОЕ количество КМ, которое должен пробегать спортсмен: '))
# while b > a:
#     a = a + a*0.1
#     i += 1
#     print(a)
# print(i+1)


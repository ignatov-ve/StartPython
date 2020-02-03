# Task 1

# import time
# class TrafficLight:
#     __color = 0
#
#     def running(self, red, yellow, green):
#         TrafficLight.__color = red
#         print(f'Сейчас горит {red} (7 сек.)')
#         time.sleep(7)
#         TrafficLight.__color = yellow
#         print(f'Сейчас горит {yellow} (2 сек.)')
#         time.sleep(2)
#         TrafficLight.__color = green
#         print(f'Сейчас горит {green} (7 сек.)')
#         time.sleep(7)
#
# s = TrafficLight()
# s.running('красный', 'желтый', 'зеленый')

# Task 2

# class Road:
#     _lenght = int(input('Введите длину дороги: '))
#     _width = int(input('Введите ширину дороги: '))
#
#     def summary(self, massa, depth):
#         self.massa = massa
#         self.depth = depth
#         s = Road._lenght * Road._width * massa * depth / 1000
#         print(f'Масса асфальта, необходимая для покрытия по указанным параметрам составляет {s} тонн')
#
# r = Road()
# r.summary(25, 5)

# Task 3

# class Worker:
#     name = input('Введите имя сотрудника: ')
#     surname = input('Введите фамилию сотрудника: ')
#     position = input('Введите должность сотрудника: ')
#     _income = {'Оклад': 200000, 'Бонус': 50000}
#
# class Position(Worker):
#     def get_full_name(self):
#         print(f'Сотрудник: {Worker.name} {Worker.surname}')
#     def get_total_income(self):
#         total = Worker._income['Оклад'] + Worker._income['Бонус']
#         print(f'Должность {Worker.position}, доход с учетом премии {total}')
#
# p = Position()
# p.get_full_name()
# p.get_total_income()

# Task 4

# class Car:
#     speed = int(input('Введите скорость автомоблия в км/ч: '))
#     color = input('Введите цвет автомобиля: ')
#     name = input('Введите марку (название) автомобиля: ')
#     is_police = False
#     def go(self):
#         print('Машина поехала')
#     def stop(self):
#         print('Машина остановилась')
#     def turn(self, direction):
#         self.direction = direction
#         print(f'Машина повернула {direction}')
#     def show_speed(self, speed):
#         self.speed = speed
#         print(f'Текущая скорость автомобиля равна {speed}')
#
# class TownCar(Car):
#     print(f'Городская машина {Car.name} {Car.color} цвета двигается со скоростью {Car.speed} км/ч')
#     print(f'Машина полицейская? {Car.is_police}')
#     def show_speed(self):
#         if Car.speed > 60:
#             print('Автомобиль превышает разрешенную скорость в 60 км/ч')
#
#
# class SportCar(Car):
#     print(f'Спортивная машина {Car.name} {Car.color} цвета двигается со скоростью {Car.speed} км/ч')
#     print(f'Машина полицейская? {Car.is_police}')
#
# class WorkCar(Car):
#     print(f'Рабочая машина {Car.name} {Car.color} цвета двигается со скоростью {Car.speed} км/ч')
#     print(f'Машина полицейская? {Car.is_police}')
#     def show_speed(self):
#         if Car.speed > 40:
#             print('Автомобиль превышает разрешенную скорость в 40 км/ч')
#
# class PoliceCar(Car):
#     print(f'Полицейская машина {Car.name} в спец.раскраске двигается со скоростью --- км/ч. А какое значение имеет скорость, это же спец.машина.')
#     Car.is_police = True
#     print(f'Машина полицейская? {Car.is_police}')
#
# tc = WorkCar()
# tc.show_speed()
# tc.go()
# tc.stop()
# tc.turn('Направо')


# Task 5

# class Stationery:
#     title = 'Канцелярские принадлежности'
#     def draw(self):
#         print(f'Запуск отрисовки класса {Stationery.title}')
# class Pen(Stationery):
#     def draw(self):
#         print('Ручка - канцелярская принадлежность')
# class Pencil(Stationery):
#     def draw(self):
#         print('Карандаш - канцелярская принадлежность')
# class Handel(Stationery):
#     def draw(self):
#         print('Маркер - канцелярская принадлежность')
#
# st = Stationery()
# st.draw()
# p = Pen()
# p.draw()
# pe = Pencil()
# pe.draw()
# h = Handel()
# h.draw()
# Task 1. Здесь у меня почему-то не получилось сделать красивый вывод без ошибки

# class Matrix:
#     def __init__(self, a):
#         self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
#         List = []
#         for i in a:
#             List.append([j for j in i])
#         self.a = List
#         for line in List:
#             for item in line:
#                 print(f'{item:>4}', end = '')
#             print()
#         print('-' * len(List) * 5)
#
#     def __str__(self):
#         for line in self.a:
#             for item in line:
#                 print(f'{item:>4}', end='')
#             print()
#         return self.a
#
#
#     def __add__(self, other):
#         NumStr = len(self.a)
#         NumCol = len(other.a[0])
#         for i in range(NumStr):
#             for j in range(NumCol):
#                 self.a[i][j] = self.a[i][j] + other.a[i][j]
#             Result = self.a
#         return Matrix(Result)
#
# m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
# print(m1 + m2)

# Task 2. Здесь у меня не получилось без использования 1-й формулы дважды

# class Suit:
#     def __init__(self, vs_h, vc_s):
#         self.vs = (vs_h / 6.5) + (2 * vc_s) + 0.8
#
# class Clothes:
#     def __init__(self, vs_h, vc_s):
#         print('Создание экземпляра класса')
#         self.vs = (vs_h / 6.5) + (2 * vc_s) + 0.8
#         self.wd = []
#     def add_vs(self, vs_h, vc_s):
#         self.wd.append(Suit(vs_h, vc_s))
#     @property
#     def lf(self):
#         main_lf = self.vs
#         for el in self.wd:
#             main_lf += el.vs
#         return f'{main_lf/2:.2f}'
#
# r = Clothes(180, 52)
# a = r.add_vs(180, 52)
# print(r.lf)

# Task 3. Не совсем понял задание в части производимых операций

# class Cell:
#     def __init__(self, n):
#         self.n = n
#     def __add__(self, other):
#         return self.n + other
#     def __sub__(self, other):
#         return self.n - other
#     def __mul__(self, other):
#         return self.n * other
#     def __truediv__(self, other):
#         return round(self.n / other)
#     def make_order(self, cel):
#         self.celf = ""
#         while self.n > 0:
#             self.n -= cel
#             if self.n < 0:
#                 self.celf += ("$" * (cel+self.n)+"\n")
#             else:
#                 self.celf += ("$"*cel+"\n")
#         return self.celf
#     def __call__(self, new_n):
#         self.n=new_n
#
# S=Cell(50)
# print(S.make_order(8))
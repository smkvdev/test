# from tabulate import tabulate
# class Matrix:
#     def __init__(self, matrix_):
#         self.matrix_ = matrix_
#
#     def __add__(self, other):
#         try:
#             self.matrix = []
#             matrix_small = []
#             for elem in range(0, len(self.matrix_)):
#                 cells = len(self.matrix_[elem])
#                 for cell in range(0, cells):
#                     matrix_small.append(self.matrix_[elem][cell] + other.matrix_[elem][cell])
#                 self.matrix.append(matrix_small)
#                 matrix_small = []
#             self.matrix_ = self.matrix
#             return self
#         except Exception:
#             print("Разная длина списков")
#
#     def __str__(self):
#         return (tabulate(self.matrix_, tablefmt="plain"))
#
# a = [[10, 2], [3, 4], [5, 6], [7, 8]]
# b = [[1, 2], [3, 4], [5, 6], [10, 20]]
#
# matr_1 = Matrix(a)
# matr_2 = Matrix(b)
# matr_3 = Matrix(b)
#
# print(matr_1)
# print(matr_1 + matr_2)
#-------------------------------------------------------------------------------------------------
# from abc import ABC, abstractmethod
# class Wear(ABC):
#     def __init__(self, title):
#         self.title = title
#
#     @abstractmethod
#     def fabric_consumption(self):
#         pass
#
# class Coat(Wear):
#     def __init__(self, title, size):
#         super().__init__(title)
#         self.size = size
#
#     def fabric_consumption(self):
#         result = self.size/6.5+0.5
#         str = f"модель {self.title} имеет площадь {result}см.кв."
#         return str
#
# class Suit(Wear):
#     def __init__(self, title, height):
#         super().__init__(title)
#         self.height = height
#
#     def fabric_consumption(self):
#         pass
#         result = (2*self.height+0.3)
#         str = f"модель {self.title} имеет площадь {result}см.кв."
#         return str
#
#
# coat1 = Coat("Пижон", 178)
# print(coat1.fabric_consumption())
# suit1 = Suit("Александрия", 50)
# print(suit1.fabric_consumption())
#-------------------------------------------------------------------------------------------------

# class Cell:
#     def __init__(self, numbers):
#         self.numbers = numbers
#
#     def __add__(self, other):
#         pass
#
#     def __sub__(self, other):
#         pass
#
#     def __mul__(self, other):
#         pass
#
#     def __truediv__(self, other):
#         pass
#
"""
В первой строке дан типа интервала
type — строка, принимающая одно из следующих значений: WEEK, MONTH, QUARTER, YEAR, REVIEW.
Во второй строке через пробел даны начальная и конечная даты
start и end (start≤end) в формате yyyy-MM-dd.
Гарантируется, что обе даты лежат в промежутке с 1 января 2000 года по 31 декабря 3999 года включительно.
"""
import re
import datetime
from datetime import timedelta
import calendar
import pendulum as pdl


period1 = "WEEK"
dates_ = "2020-01-31 2020-03-25"
dates = re.findall(r"(\S+)", dates_)
d_start = pdl.DateTime.fromisoformat(dates[0])
d_end = pdl.DateTime.fromisoformat(dates[1])


def week(start, stop):
    d_track = []
    d_start = start
    d_end = stop
    if d_start.day_of_week == pdl.SUNDAY:
        d_track.append(f"{str(d_start)[:10]} {str(d_start)[:10]}")
    d_start = d_start.end_of("week")
    while d_start < d_end:
        start_week = d_start.next(pdl.MONDAY)
        d_start = d_start.next(pdl.SUNDAY)

        if d_start > d_end:
            d_start = d_end
        d_track.append(f"{str(start_week)[:10]} {str(d_start)[:10]}")
    return d_track

# a = week(d_start, d_end)
# print(len(a))
# for i in a:
#     print(i)

# def month(start, stop):
#     d_track = []
#     d_start = start
#     d_end = stop
#     if d_start == d_start.end_of("month") :
#         print(f"{d_start} конец месяца")
#         d_track.append(f"{str(d_start)[:10]} {str(d_start)[:10]}")
#     d_start = d_start.end_of("week")
#     while d_start < d_end:
#         start_week = d_start.next(pdl.MONDAY)
#         d_start = d_start.next(pdl.SUNDAY)
#
#         if d_start > d_end:
#             d_start = d_end
#         d_track.append(f"{str(start_week)[:10]} {str(d_start)[:10]}")


# a = month(d_start, d_end)
# print(len(a))
# for i in a:
#     print(i)

d_track = []
end_month = d_start.end_of("month")
d_track.append(f"{str(d_start)[:10]} {str(end_month)[:10]}")
d_track
dt.start_of('month')
dt.end_of('month')

print(d_track)
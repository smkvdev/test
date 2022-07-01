# class Cell:
#     def __init__(self, number):
#         self.number = number
#
#     def __add__(self, other):
#         return self.number + other.number
#
#     def __sub__(self, other):
#         res = self.number - other.number
#         if res > 0:
#             return res
#         else:
#             raise ValueError("Результат должен быть больше 0")
#
#     def __mul__(self, other):
#         return self.number * other.number
#
#     def __truediv__(self, other):
#         return int(self.number / other.number)
#
#     def make_order(self, step):
#         lst = "".join(["*" for el in range(0, self.number)])
#         for item in range(0, len(lst), step):
#             print(lst[item:item+step])
#
#
#
# cell1 = Cell(15)
# cell2 = Cell(12)
#
# print(cell1+cell2)      #+
# print(cell1*cell2)      #*
# print(cell1-cell2)      #-
# print(cell1/cell2)      #/
#
# cell1.make_order(5)

a = [[4, 1, 6, 8], [0, 4, 5, 1], [5, 6, 3, 1]]
print(",".join(map(str, a)))

print(list(map(str, a)))
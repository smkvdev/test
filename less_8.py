# from re import findall
# import datetime
#
# class MyData():
#     tmp_data = []
#
#     def __init__(self, data):
#         self.data = data
#
#     @classmethod
#     def str_to_int(cls, param):
#         cls.tmp_data = findall(r"(\w+)", param)
#         return cls.tmp_data
#
#     @staticmethod
#     def check_data(param):
#         d1 = MyData.tmp_data
#         try:
#             date_obj = datetime.datetime(int(d1[2]), int(d1[1]), int(d1[0]))
#         except ValueError:
#             print("Ошибка ввода данных")
#         else:
#             print(f"{date_obj} True")
#
#
# data1 = MyData("29-02-2021")
# data1.str_to_int(data1.data)
# data1.check_data(data1.data)
#---------------------------------------------------------------------
# from re import findall
# class MyClass:
#     def __init__(self, text):
#         self.text = text
# try:
#     exist = 10/0
#
# except ZeroDivisionError as err:
#     #raise MyClass("Wrong!")
#     print("!!!!")
# else:
#     print(exist)

# class MyError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
# inp = ""
# lst = []
#
# while not inp == "stop":
#     inp = input("Enter number: ")
#     try:
#         if not inp.isdigit():
#             raise MyError("Wrong input!")
#     except (ValueError, MyError) as err:
#             print(err)
#     else:
#         lst.append(float(inp))
#---------------------------------------------------------------------------------------
# class Warehouse:
#     def __init__(self):
#         self._stock = {}
#
#     def format(self, obj):
#         dict = {}
#         tmp = vars(obj)
#         serial = tmp["serial"]
#         tmp.pop("serial")
#         dict[serial] = tmp
#         return dict
#
#     def set_stock(self, obj):
#         for key in obj:
#             self._stock[key] = obj[key]
#
#     def get_stock(self):
#         return self._stock
#
#     def move(self, obj, item):
#         obj.set_stock(item)
#         for key in item:
#             self._stock.pop(key)
#         #self._stock.pop(item)
#
# class Accouting(Warehouse):
#     def __init__(self):
#         self._stock = {}
#
#     def set_stock(self, obj):
#         for key in obj:
#             self._stock[key] = obj[key]
#
#     def get_stock(self):
#         return self._stock
#
#
# class Orgtecnic:
#     def __init__(self, serial, model, name,  color, price):
#         self.serial = serial
#         self.name = name
#         self.model = model
#         self.color = color
#         self.price = price
#
# class Printer(Orgtecnic):
#     def __init__(self, serial, model, name, color, price, s_print):
#         super().__init__(serial, model, name, color, price)
#         self.s_print = s_print
#
# class Scaner(Orgtecnic):
#     def __init__(self, serial, model, name, color, price, s_scan):
#         super().__init__(serial, model, name, color, price)
#         self.s_scan = s_scan
#
# class Xerox(Orgtecnic):
#     def __init__(self, serial, model, name, color, price, capacity):
#         super().__init__(serial, model, name, color, price)
#         self.capacity = capacity
#
# warehouse = Warehouse()
# accounting = Accouting()
#
# pr_dcp_7057R = Printer("dcp7053_123", "DCP-7057R", "Brother",  "white", "10000", "24")
# scaner_DC_3320 = Scaner("dc3320_123", "DC-3320", "DocMate", "grey", "42000", "23")
# xerox_B_230v = Xerox("b230v_123", "B-230V", "Xerox", "blue", "15000", "36")
#
# pr_dcp_7057R = warehouse.format(pr_dcp_7057R)
# warehouse.set_stock(pr_dcp_7057R)
#
# scaner_DC_3320 = warehouse.format(scaner_DC_3320)
# warehouse.set_stock(scaner_DC_3320)
#
# xerox_B_230v = warehouse.format(xerox_B_230v)
# warehouse.set_stock(xerox_B_230v)
#
# warehouse.move(accounting, pr_dcp_7057R)
# print(accounting.get_stock())
# print(warehouse.get_stock())

#---------------------------------------------------------------------------------------
from re import findall
class Compl:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        self.num

a = (10 + 3i)
















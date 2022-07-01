# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def count_road(self):
#         return (f"масса асфальта составляет {self._length * self._width * 25 * 0.005}т.")
#
# road = Road(20, 5000)
# print(road.count_road())
#------------------------------------------------------------------------------------------
# class Worker:
#     def __init__(self, name, surname, position, wage = 0, bonus = 0):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
# class Position(Worker):
#     def get_full_name(self):
#         print(f"{self.name} {self.surname}")
#
#     def get_total_income(self):
#         aa = self._income["wage"]
#         bb = self._income["bonus"]
#         print(f"{self.position} wage: {aa} bonus: {bb}")
#
# aa = Position("Ivan", "Ivanov", "Boss", 100, 150)
# aa.get_full_name()
# aa.get_total_income()

#------------------------------------------------------------------------------------------

# class Car:
#     def __init__(self, speed, color, name, is_police: bool):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print("Машина поехала")
#
#     def stop(self):
#         print("Машина остановилась")
#
#     def turn(self, direction):
#         print(f"машина повернула {direction}")
#
#     def show_speed(self):
#         print(f"Скорость автомобиля {self.speed} км/ч")
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             print("Превышение скорости")
#
# class SportCar(Car):
#     pass
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             print("Превышение скорости")
#
# class PoliceCar(Car):
#     pass
#------------------------------------------------------------------------------------------

# class MyClass:
#     def __init__(self, n):
#         self.n = n
#
#     def __del__(self):
#          print(f"Delete object")
#
# my = MyClass(10)


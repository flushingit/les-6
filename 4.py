# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    speed = int
    colour = str
    name = str
    is_police = bool

    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = is_police

    def go(self):
        return"поехала"

    def stop(self):
        return "остановилась"

    def turn(self, direction):
        return f"повернула на {direction}"

    def show_speed(self):
        return f"со скоростью {self.speed}км/ч"


class TownCar(Car):

    def show_speed(self):

        if self.speed > 60:
            return f"со скоростью {self.speed}км/ч Внимание! Скорость превышена"
        return f"движется со скоростью {self.speed}км/ч"

class WorkCar(Car):
    def show_speed(self):

        if self.speed > 40:
            return f"со скоростью {self.speed}км/ч Внимание! Скорость превышена"
        return f"со скоростью {self.speed}км/ч"


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


my_car = TownCar(70, "black", "My Car", 'false')
taxi_1 = WorkCar(40, "yellow", "Taxi 1", 'false')
taxi_2 = WorkCar(50, "yellow", "Taxi 2", 'false')
speedster = SportCar(120, "red", "Porcshe", 'false')
cop = PoliceCar(120, "blue", "Police", 'true')

#print(my_car.go())
print(f"Машина {my_car.name} цвета {my_car.colour} полицейская {my_car.is_police} {my_car.go()} {my_car.show_speed()}, {my_car.turn('лево')} и {my_car.stop()}")
print(f"Машина {taxi_1.name} цвета {taxi_1.colour} полицейская {taxi_1.is_police} {taxi_1.go()} {taxi_1.show_speed()}, {taxi_1.turn('право')} и {taxi_1.stop()}")
print(f"Машина {taxi_2.name} цвета {taxi_2.colour} полицейская {taxi_2.is_police} {taxi_2.go()} {taxi_2.show_speed()}, {taxi_2.turn('право')} и {taxi_2.stop()}")
print(f"Машина {speedster.name} цвета {speedster.colour} полицейская {speedster.is_police} {speedster.go()} {speedster.show_speed()}, {speedster.turn('лево')} и {speedster.stop()}")
print(f"Машина {cop.name} цвета {cop.colour} полицейская {cop.is_police} {cop.go()} {cop.show_speed()}, {cop.turn('лево')} и {cop.stop()}")

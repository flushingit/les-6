# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Ручка кончилась")


class Pencil(Stationery):
    def draw(self):
        print("Карандаш сломался")


class Handle(Stationery):
    def draw(self):
        print("Маркер высох")


a = Stationery("Принадлежность")
b = Pen("Ручка")
c = Pencil("Карандаш")
d = Handle("Маркер")

a.draw()
b.draw()
c.draw()
d.draw()

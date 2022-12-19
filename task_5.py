# 5) Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод
# для каждого экземпляра.

class Stationery:
    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        pass

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start draw")


class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)

    def draw(self):
        print("Drawing using small ball")


class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)

    def draw(self):
        print("Drawing using my graphite")


class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)

    def draw(self):
        print("Drawing like fingernail on glass")


if __name__ == '__main__':
    pen_black = Pen("pen_black")
    pencil_toy = Pencil("pencil_toy")
    handle_red = Handle("handle_red")

    pen_black.draw()
    pencil_toy.draw()
    handle_red.draw()

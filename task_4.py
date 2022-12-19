# 4) Реализуйте базовый класс Car. У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
#
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно
# выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed: int, color, name, is_police: bool):
        self.__is_police = is_police
        self.__name = name
        self.__color = color
        self.speed = speed

    def is_it_police(self):
        return self.__color

    def get_color(self):
        return self.__color

    def get_name(self):
        return self.__name

    def go(self):
        print(f"Car {self.__name} go")

    def stop(self):
        print(f"Car {self.__name} stopped")

    def turn(self, direction):
        print(f"Car {self.__name} change direction to - {direction}")

    def show_speed(self):
        print(f"Car {self.__name} speed is {self.speed}")


class TownCar(Car):
    def __init__(self, speed: int, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Speed is more than 60. Make less pls")
        super(TownCar, self).show_speed()


class SportCar(Car):
    def __init__(self, speed: int, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed: int, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Speed is more than 40. Make less pls")
        super(WorkCar, self).show_speed()


class PoliceCar(Car):
    def __init__(self, speed: int, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)


if __name__ == '__main__':
    volvo_car = Car(70, "green", "volvo", False)
    kia_car = TownCar(66, "black", "kia", False)
    bugatti_car = SportCar(120, "yellow", "bugatti", False)
    kamaz_car = WorkCar(50, "orange", "kamaz", False)
    uaz_car = PoliceCar(40, "grey", "uaz", True)

    kia_car.go()
    kia_car.show_speed()

    kamaz_car.go()
    print(
        f"Check car {kamaz_car.get_name()} is polise - {kamaz_car.is_it_police()}")

    uaz_car.go()
    print(f"Car {uaz_car.get_name()} has color {uaz_car.get_color()}")

    volvo_car.go()
    volvo_car.stop()

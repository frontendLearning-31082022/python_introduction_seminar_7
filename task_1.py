# 1) Создать класс TrafficLight (светофор)
# и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
from itertools import cycle
from time import sleep


class TrafficLight:

    def __init__(self, secs_red, secs_yellow, secs_green):
        self.__regimes = {'red': secs_red, 'yellow': secs_yellow,
                          'green': secs_green}
        self.__color = None
        self.__cycler = cycle(self.__regimes)

    def running(self):
        while True:
            self.__color = next(self.__cycler)
            print(f"Switched to {self.__color}")
            sleep(self.__regimes[self.__color])


if __name__ == '__main__':
    trafficLight = TrafficLight(7, 2, 5)
    trafficLight.running()

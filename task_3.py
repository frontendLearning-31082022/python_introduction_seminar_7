# 3) Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность),
# income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    @property
    def _income(self):
        money_reasons = self.__income_detail.values()

        if all(v is None for v in money_reasons):
            return None

        sum_count = 0
        for money in self.__income_detail.values():
            if money != None:
                sum_count += money
        return sum_count

    @_income.setter
    def _income(self, value):
        print("Incopability operation. Try to set wage and bonus at first")

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.position = surname
        self.__income_detail = {'wage': None, 'bonus': None}

    def set_wage(self, value):
        self.__income_detail['wage'] = value

    def set_bonus(self, value):
        self.__income_detail['bonus'] = value


class Position(Worker):

    def __init__(self, worker_person: Worker, position_type):
        super(Position, self).__init__(worker_person.name,
                                       worker_person.surname)
        self.position = position_type

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income


if __name__ == '__main__':
    person_1 = Worker("Ivan", "Ivanov")
    worker_in_staff = Position(person_1, "Accounter")

    worker_2 = Position(Worker("Petr", "Petrov"), "Driver")

    print(f"{worker_in_staff.get_full_name()} money get every month"
          f" {worker_in_staff.get_total_income()}")

    print("Add something")
    worker_in_staff.set_wage(30000)
    worker_in_staff.set_bonus(2)
    print(f"{worker_in_staff.get_full_name()} money get every month"
          f" {worker_in_staff.get_total_income()}")

    worker_2.set_wage(1000)
    print(f"{worker_2.get_full_name()} has {worker_2.get_total_income()}")

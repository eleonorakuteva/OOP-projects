from abc import ABC, abstractmethod


class BaseAstronaut(ABC):

    MINIMUM_STAMINA = 0
    MAXIMUM_STAMINA = 100

    def __init__(self, id_number: str, salary: float, specialization: str, stamina: int):
        self.id_number = id_number
        self.salary = salary
        self.specialization = specialization
        self.stamina = stamina

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, value: str):
        if not value.isdigit():
            raise ValueError("ID can contain only digits!")
        self.__id_number = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value: float):
        if value < 0.0:
            raise ValueError("Salary must be a positive number!")
        self.__salary = value

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value: str):
        if not value.strip():
            raise ValueError("Specialization cannot be empty!")
        self.__specialization = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < self.MINIMUM_STAMINA or value > self.MAXIMUM_STAMINA:
            raise ValueError("Stamina is out of range!")
        self.__stamina = value

    @property
    @abstractmethod
    def stamina_increase(self):
        pass

    def train(self):
        if self.stamina + self.stamina_increase <= 100:
            self.stamina += self.stamina_increase



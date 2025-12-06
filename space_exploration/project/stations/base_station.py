from abc import ABC, abstractmethod

from project.astronauts.base_astronaut import BaseAstronaut


class BaseStation (ABC):

    MINIMUM_CAPACITY = 0

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: list[BaseAstronaut] = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not all(ch.isalnum() or ch == "-" for ch in value):
            raise ValueError("Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < self.MINIMUM_CAPACITY:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value


    def calculate_total_salaries(self):
        total_salary = sum(a.salary for a in self.astronauts)
        return f"{total_salary:.2f}"

    def status(self) -> str:
        astronauts = "N/A"
        if self.astronauts:
            sorted_astro = sorted(self.astronauts, key=lambda a: a.id_number)
            astronauts = ' #'.join(a.id_number for a in sorted_astro)

        result = (f"Station name: {self.name}; "
                  f"Astronauts: {astronauts}; "
                  f"Total salaries: {self.calculate_total_salaries()}")

        return result

    @property
    @abstractmethod
    def salary_update_based_on_station_type(self):
        pass

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass



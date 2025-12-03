from abc import ABC, abstractmethod
from math import floor
from project.equipment.base_equipment import BaseEquipment


class BaseTeam(ABC):

    MINIMUM_LEN_CHARS_FOR_COUNTRY = 2

    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins: int = 0
        self.equipment: list[BaseEquipment] = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value: str):
        if len(value.strip()) < self.MINIMUM_LEN_CHARS_FOR_COUNTRY:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value: int):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value


    @abstractmethod
    def win(self):
        pass

    def get_statistics(self) -> str:
        total_price_of_team_equipment = sum(e.price for e in self.equipment)

        avg_team_protection = 0
        if self.equipment:
            avg_team_protection = sum(e.protection for e in self.equipment) / len(self.equipment)

        result = [
            f"Name: {self.name}",
            f"Country: {self.country}",
            f"Advantage: {self.advantage} points",
            f"Budget: {self.budget:.2f}EUR",
            f"Wins: {self.wins}",
            f"Total Equipment Price: {total_price_of_team_equipment:.2f}",
            f"Average Protection: {floor(avg_team_protection)}"
        ]

        return '\n'.join(result)


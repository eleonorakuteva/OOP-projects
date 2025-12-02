from abc import ABC, abstractmethod

class Astronaut(ABC):


    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack: list = []

    @property
    @abstractmethod
    def oxygen_units_while_breathing(self) -> int:
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.oxygen_units_while_breathing

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
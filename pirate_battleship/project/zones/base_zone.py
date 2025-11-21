from abc import ABC, abstractmethod

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):

    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: list[BaseBattleship] = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value: str):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    def get_ships(self) -> list:

        sorted_ships = sorted(self.ships, key=lambda s: (-s.hit_strength, s.name))
        return sorted_ships

    @abstractmethod
    def zone_info(self):
        pass
from abc import ABC, abstractmethod


class Horse(ABC):

    MINIMUM_LEN_NAME = 4

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        # one horse can have only one rider
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value.strip()) < self.MINIMUM_LEN_NAME:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value: int):
        if value > self.max_speed:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @property
    @abstractmethod
    def max_speed(self) -> int:
        pass

    @property
    @abstractmethod
    def increases_speed_by_train(self) -> int:
        pass

    @abstractmethod
    def train(self):
        pass


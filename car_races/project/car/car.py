from abc import ABC, abstractmethod


class Car(ABC):
    MINIMUM_MODEL_SYMBOLS = 4

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        # One car can be driven by ONLY one driver.
        self.is_taken = False

    @property
    @abstractmethod
    def min_speed_limit(self):
        pass

    @property
    @abstractmethod
    def max_speed_limit(self):
        pass

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        if len(value) < self.MINIMUM_MODEL_SYMBOLS:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value not in range(self.min_speed_limit(), self.max_speed_limit() + 1):
            raise ValueError(f"Invalid speed limit! Must be between {self.min_speed_limit()} and {self.max_speed_limit()}!")
        self.__speed_limit = value
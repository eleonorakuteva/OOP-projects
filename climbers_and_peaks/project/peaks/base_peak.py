from abc import ABC, abstractmethod


class BasePeak(ABC):

    MIN_LENGTH_NAME = 2
    MIN_ELEVATION = 1_500

    def __init__(self, name: str, elevation: int) -> None:
        self.name = name
        self.elevation = elevation

    @property
    @abstractmethod
    def recommended_gear(self):
        pass

    @property
    @abstractmethod
    def difficulty_level(self):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value.strip()) < BasePeak.MIN_LENGTH_NAME:
            raise ValueError("Peak name cannot be less than 2 symbols!")
        self.__name = value

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self, value: int):
        if value < BasePeak.MIN_ELEVATION:
            raise ValueError("Peak elevation cannot be below 1500m.")
        self.__elevation = value


    def get_recommended_gear(self):
        """each type of peak has specific requirements for the gear"""
        pass


    def calculate_difficulty_level(self):
        """
        The difficulty levels are "Extreme" and "Advanced".
        Different for different peaks.
        """
        pass
        
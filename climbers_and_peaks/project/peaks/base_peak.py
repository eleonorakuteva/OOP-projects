from abc import ABC, abstractmethod


class BasePeak(ABC):

    MIN_LENGTH_NAME: int  = 2
    MIN_ELEVATION: int = 1_500
    EVEREST_HEIGHT: int = 8_849

    def __init__(self, name: str, elevation: int) -> None:
        self.name = name
        self.elevation = elevation
        self.difficulty_level:str | None = self.calculate_difficulty_level()

    @property
    @abstractmethod
    def recommended_gear(self) -> list:
        pass

    @property
    @abstractmethod
    def difficulty_levels(self) -> dict:
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


    def get_recommended_gear(self) -> list[str]:
        """Each type of peak has specific requirements for the gear"""
        return self.recommended_gear


    def calculate_difficulty_level(self) -> str:
        """
        The difficulty levels are "Extreme" and "Advanced".
        Different for different peaks.
        """
        for level, level_range in self.difficulty_levels.items():
            if self.elevation in level_range:
                return level


        
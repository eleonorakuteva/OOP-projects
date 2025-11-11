from abc import ABC, abstractmethod


class BasePeak(ABC):

    MIN_LENGTH_NAME: int = 2
    MIN_ELEVATION: int = 1_500

    def __init__(self, name: str, elevation: int) -> None:
        self.name = name
        self.elevation = elevation
        self.difficulty_level: str | None = self.calculate_difficulty_level()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value.strip()) < BasePeak.MIN_LENGTH_NAME:
            raise ValueError(f"Peak name cannot be less than {BasePeak.MIN_LENGTH_NAME} symbols!")
        self.__name = value

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self, value: int):
        if value < BasePeak.MIN_ELEVATION:
            raise ValueError(f"Peak elevation cannot be below {BasePeak.MIN_ELEVATION}m.")
        self.__elevation = value

    @abstractmethod
    def get_recommended_gear(self) -> list[str]:
        """Each type of peak has specific requirements for the gear"""
        pass
        # return self.recommended_gear

    @abstractmethod
    def calculate_difficulty_level(self) -> str:
        """
        The difficulty levels are "Extreme" and "Advanced".
        Different for different peaks.
        """
        pass



        
from abc import ABC, abstractmethod
from project.peaks.base_peak import BasePeak


class BaseClimber(ABC):

    POINTS_PER_REST: float = 15.0

    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: list[BasePeak] = []
        self.is_prepared: bool = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value: float):
        if value <= 0.0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @abstractmethod
    def can_climb(self):
        pass

    def climb(self, peak: BasePeak):
        """
        The method takes a peak parameter that represents the peak
        the climber is trying to conquer. The climber's strength is
        reduced by a specific amount based on the peak's difficulty
        level, and a list is collected of conquered peaks by each climber.
        """
        pass

    def rest(self) -> float:
        """ Increases the climber's strength """
        return self.__strength + BaseClimber.POINTS_PER_REST

    def __str__(self) -> str:
        return f"{type(self).__name__}: /// Climber name: {self.__name} * Left strength: {self.__strength} * Conquered peaks: {', '.join(p.name for p in self.conquered_peaks)} ///"
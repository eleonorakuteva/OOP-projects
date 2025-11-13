from abc import ABC, abstractmethod
from project.fish.base_fish import BaseFish


class BaseDiver(ABC):

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: list[BaseFish] = []
        self.competition_points: round(float, 1) = 0
        self.has_health_issue: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value: float):
        if value < 0.0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @abstractmethod
    def miss(self, time_to_catch: int) -> None:
        """
        Decreases the diver's oxygen_level property.
        When the method is invoked the diver's oxygen_level is decreased by a certain value,
        that will depend on the fish that is chased.
        :param time_to_catch: int
        :return None
        """
        pass

    @abstractmethod
    def renew_oxy(self):
        """
        The diver's oxygen_level should be fully replenished to its original value.
        This would mean setting the oxygen_level back to its starting value depending on the diver’s type.
        :return:
        """
        pass

    def hit(self, fish: BaseFish):

        if self.oxygen_level >= fish.time_to_catch:
            self.oxygen_level -= fish.time_to_catch
            self.competition_points += fish.points
            self.catch.append(fish)
        else:
            self.oxygen_level = 0


    def update_health_status(self) -> bool:
        """
        Changes the health status of the diver to True, if it is False or reciprocally.
        :return: bool
        """
        return not self.has_health_issue

    def zero_oxygen_level_handling(self):
        if self.oxygen_level <= 0:
            self.has_health_issue = True

    def __str__(self) -> str:
        return (f"{type(self).__name__}: "
                f"[Name: {self.name}, "
                f"Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, "
                f"Points earned: {self.competition_points}]")
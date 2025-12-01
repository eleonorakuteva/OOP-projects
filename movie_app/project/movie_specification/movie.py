from abc import ABC, abstractmethod
from project.user import User


class Movie(ABC):

    MINIMUM_YEAR_RELEASED = 1888

    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner: object[User] = owner
        self.age_restriction = age_restriction
        self.likes: int = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value: str):
        if not value.strip():
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        if value < self.MINIMUM_YEAR_RELEASED:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value: object):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value


    @abstractmethod
    def details(self) -> str:
        pass


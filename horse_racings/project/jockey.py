from project.horse_specification.horse import Horse


class Jockey:

    MINIMUM_AGE_JOCKEY = 18

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        # one jockey can ride only one horse
        self.horse: None | Horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < self.MINIMUM_AGE_JOCKEY:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")
        self.__age = value

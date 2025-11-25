from abc import ABC, abstractmethod


class Musician(ABC):

    MINIMUM_AGE = 16

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills :list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < self.MINIMUM_AGE:
            raise ValueError("Musicians should be at least 16 years old!")
        self.__age = value

    @property
    @abstractmethod
    def available_skills_for_type_of_musician(self) -> list[str]:
        pass

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.available_skills_for_type_of_musician:
            raise ValueError(f"{new_skill} is not a needed skill!")

        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")

        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."

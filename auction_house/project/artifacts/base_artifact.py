from abc import ABC, abstractmethod


class BaseArtifact(ABC):

    def __init__(self, name: str, price: float, space_required: int):
        self.name = name
        self.price = price
        self.space_required = space_required

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Artifact name cannot be null or empty!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0.0:
            raise ValueError("Artifact price should be more than 0.0!")
        self.__price = value

    @property
    def space_required(self):
        return self.__space_required

    @space_required.setter
    def space_required(self, value: int):
        if value < 1 or value > 1000:
            raise ValueError("Space required for the artifact exhibition must be between 1 and 1000!")
        self.__space_required = value

    @abstractmethod
    def type(self):
        pass

    def artifact_information(self):
        return (f"{self.type()}: {self.name}; "
                f"Price: {self.price:.2f}; "
                f"Required space: {self.space_required}")
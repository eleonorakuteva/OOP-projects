from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor: str|None = None
        self.ram: int|None = None
        self.price: int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @property
    @abstractmethod
    def max_ram(self):
        pass

    @property
    @abstractmethod
    def valid_processors(self) -> dict[str: int]:
        pass

    @property
    @abstractmethod
    def type_computer(self) -> str:
        pass

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.valid_processors.keys():
            raise ValueError(f"{processor} is not compatible with {self.type_computer} {self.manufacturer} {self.model}!")

        if ram not in self.list_valid_ram():
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type_computer} {self.manufacturer} {self.model}!")

        processor_price = self.valid_processors[processor]
        ram_price = self.ram_price(ram)

        self.processor = processor
        self.ram = ram
        self.price = processor_price + ram_price

        return (f"Created "
                f"{repr(self)}"
                f" for {self.price}$.")

    def list_valid_ram(self) -> list:
        valid_ram = [2 ** i for i in range(1, int(log2(self.max_ram))+1)]
        return valid_ram

    @staticmethod
    def ram_price(ram):
        return int(log2(ram) * 100)


    def __repr__(self) -> str:
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

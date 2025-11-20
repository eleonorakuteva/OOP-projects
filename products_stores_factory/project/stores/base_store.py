from abc import ABC, abstractmethod
from project.products.base_product import BaseProduct


class BaseStore(ABC):

    LOCATION_CHAR_LONG = 3
    ESTIMATED_PROFIT = 0.1

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: list[BaseProduct] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value: str):
        if len(value.strip()) != self.LOCATION_CHAR_LONG:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        products_count = len(self.products)
        sum_all_products = sum(p.price for p in self.products)
        profit = sum_all_products * self.ESTIMATED_PROFIT
        return f"Estimated future profit for {products_count} products is {profit:.2f}"


    @property
    @abstractmethod
    def store_type(self):
        pass


    @abstractmethod
    def store_stats(self):
        pass





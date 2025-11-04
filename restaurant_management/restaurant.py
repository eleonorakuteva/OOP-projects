from customer import Customer
from waiter import Waiter


class Restaurant:
    def __init__(self, name:str) -> None:
        self.name = name
        self.__list_of_customers: list[Customer] = []
        self.__list_of_waiters: list[Waiter] = []
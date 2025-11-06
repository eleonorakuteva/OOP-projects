from customer import Customer
from waiter import Waiter


class Restaurant:
    def __init__(self, name:str) -> None:
        self.name = name
        self.__list_of_customers: list[Customer] = []
        self.__list_of_waiters: list[Waiter] = []
        self.total_earnings = 0

    def add_customer(self, customer:Customer):
        try:
            self.__list_of_customers.append(customer)
        except AttributeError:
            return f"The {type(customer).__name__.lower()} {customer.name} already work in {self.name}"

    def add_waiter(self, waiter:Waiter):
        try:
            self.__list_of_waiters.append(waiter)
        except AttributeError:
            return f"The {type(waiter).__name__.lower()} {waiter.name} already work in {self.name}"
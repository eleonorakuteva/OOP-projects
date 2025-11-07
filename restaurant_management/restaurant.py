from customer import Customer
from waiter import Waiter


class Restaurant:
    """
    Purpose: Store the restaurant name, menu, waiters, and customers.

    Key Methods:

    add_waiter(waiter) → adds waiter to staff.

    add_customer(customer) → registers a customer currently seated.

    show_menu() → displays available dishes.

    summary() → shows how many active orders and total earnings.
    """
    def __init__(self, name:str) -> None:
        self.name = name
        self.__list_of_customers: list[Customer] = []
        self.__list_of_waiters: list[Waiter] = []
        self.total_earnings = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) < 3 and value.strip().isalpha():
            self.__name = value.title()
        raise ValueError("Restaurant name must contain at least 3 letters.")

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
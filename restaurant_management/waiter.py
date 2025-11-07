from restaurant import Restaurant
from customer import Customer


class Waiter:
    def __init__(self, name:str, id_:int, restaurant: Restaurant):
        self.name = name
        self.id = id_
        self.restaurant = restaurant
        self.tip: float = 0.0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The waiter name cannot be an empty string")
        self.__name = value


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value.isdigit() and len(value) == 8:
            self.__id = value
        else:
            raise ValueError("The id must contain 8 digits.")


    def take_order(self, customer: Customer, *args):
        pass


    def create_payment(self, customer: Customer, method:str):
        pass




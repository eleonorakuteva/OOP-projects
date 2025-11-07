from restaurant import Restaurant


class Customer:
    def __init__(self, name:str) -> None:
        self.name = name
        self.order_list :list = []
        self.total_bill = 0


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) < 3 and value.strip().isalpha():
            self.__name = value.title()
        raise ValueError("Name must contain at least 3 letters.")


    def view_bill(self):
        return self.total_bill

    def order_dish(self, restaurant: Restaurant, dish_name: str) -> str:
        pass

    def view_orders(self) -> str:
        pass

    def make_payment(self, amount: float, payment_method: str) -> str:
        pass
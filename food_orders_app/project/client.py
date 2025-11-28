from project.meals.meal import Meal

class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: list[Meal] = []
        self.bill: float = 0.0
        self.receipt_id = 0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value:str):
        if not value.isdigit() or len(value) != 10 or not value.startswith("0"):
            raise ValueError("Invalid phone number!")
        self.__phone_number = value


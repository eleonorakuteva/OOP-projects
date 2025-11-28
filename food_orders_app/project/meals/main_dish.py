from project.meals.meal import Meal


class MainDish(Meal):

    INITIAL_QUANTITY = 50

    def __init__(self, name, price, quantity = INITIAL_QUANTITY):
        super().__init__(name, price, quantity)

    def details(self) -> str:
        return f"Main Dish {self.name}: {self.price:.2f}lv/piece"


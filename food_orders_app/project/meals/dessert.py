from project.meals.meal import Meal


class Dessert(Meal):

    INITIAL_QUANTITY = 30

    def __init__(self, name, price, quantity = INITIAL_QUANTITY):
        super().__init__(name, price, quantity)

    def details(self) -> str:
        return f"Dessert {self.name}: {self.price:.2f}lv/piece"
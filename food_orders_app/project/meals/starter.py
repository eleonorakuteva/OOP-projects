from project.meals.meal import Meal


class Starter(Meal):

    INITIAL_QUANTITY = 60

    def __init__(self, name, price, quantity = INITIAL_QUANTITY):
        super().__init__(name, price, quantity)

    def details(self) -> str:
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
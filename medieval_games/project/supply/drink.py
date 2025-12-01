from project.supply.supply import Supply


class Drink(Supply):
    INITIAL_UNITS_OF_ENERGY = 15

    def __init__(self, name):
        super().__init__(name, self.INITIAL_UNITS_OF_ENERGY)

    def details(self):
        return f"{type(self).__name__}: {self.name}, {self.energy}"

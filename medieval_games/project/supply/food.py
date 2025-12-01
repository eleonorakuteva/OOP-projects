from project.supply.supply import Supply


class Food(Supply):

    INITIAL_UNITS_OF_ENERGY = 25

    def __init__(self, name, energy = None):
        if energy is None:
            energy = self.INITIAL_UNITS_OF_ENERGY
        super().__init__(name, energy)

    @property
    def type(self):
        return "Food"

    # def details(self):
    #     return f"{type(self).__name__}: {self.name}, {self.energy}"


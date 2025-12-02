from project.car.car import Car

class Driver:

    def __init__(self, name: str):
        self.name = name
        # One driver drives ONLY one car.
        self.car: Car | None = None
        self.number_of_wins: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    @property
    def has_car(self):
        return self.car is not None


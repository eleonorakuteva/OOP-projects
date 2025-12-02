from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    INITIAL_OXYGEN = 50

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)

    def oxygen_units_while_breathing(self) -> int:
        return 10
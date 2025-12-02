from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_OXYGEN = 90

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)

    def oxygen_units_while_breathing(self) -> int:
        return 15
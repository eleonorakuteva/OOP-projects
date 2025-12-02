from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    INITIAL_OXYGEN = 70

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN)

    def oxygen_units_while_breathing(self) -> int:
        return 5
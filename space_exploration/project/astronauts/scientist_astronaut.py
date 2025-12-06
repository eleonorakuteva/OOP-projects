from project.astronauts.base_astronaut import BaseAstronaut


class ScientistAstronaut(BaseAstronaut):
    INITIAL_STAMINA = 70
    SPECIALIZATION = "ScientistAstronaut"

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, self.SPECIALIZATION, self.INITIAL_STAMINA)

    @property
    def stamina_increase(self):
        return 3

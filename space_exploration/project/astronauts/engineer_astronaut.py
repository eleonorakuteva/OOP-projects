from project.astronauts.base_astronaut import BaseAstronaut


class EngineerAstronaut(BaseAstronaut):

    INITIAL_STAMINA = 80
    SPECIALIZATION = "EngineerAstronaut"

    def __init__(self, id_number: str, salary: float):
        super().__init__(id_number, salary, self.SPECIALIZATION, self.INITIAL_STAMINA)

    @property
    def stamina_increase(self):
        return 5
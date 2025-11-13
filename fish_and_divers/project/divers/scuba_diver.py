from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540

    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int) -> None:
        pass

    def renew_oxy(self) -> None:
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL





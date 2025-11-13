from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    INITIAL_OXYGEN_LEVEL = 540
    DECREASED_PERCENTAGE_PER_MISS = 0.3

    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int) -> None:
        decreased = int(round(time_to_catch * self.DECREASED_PERCENTAGE_PER_MISS))
        self.oxygen_level = max(0, (self.oxygen_level - decreased))

    def renew_oxy(self) -> None:
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL






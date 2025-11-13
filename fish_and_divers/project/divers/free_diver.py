from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):

    INITIAL_OXYGEN_LEVEL = 120
    DECREASED_PERCENTAGE_PER_MISS: float = 0.6

    def __init__(self, name):
        super().__init__(name, self.INITIAL_OXYGEN_LEVEL)

    def miss(self, time_to_catch: int) -> None:
        reduce_amount = int(round(time_to_catch * self.DECREASED_PERCENTAGE_PER_MISS))
        self.oxygen_level = max(0, (self.oxygen_level - reduce_amount))

    def renew_oxy(self) -> None:
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL


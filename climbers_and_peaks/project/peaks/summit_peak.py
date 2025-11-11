from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):

    @property
    def recommended_gear(self) -> list:
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    @property
    def difficulty_level(self) -> dict:
        levels = {"Advanced": range(1500, 2501), "Extreme": range(2_501, BasePeak.EVEREST_HEIGHT + 1)}
        return levels


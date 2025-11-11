from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):

    @property
    def recommended_gear(self) -> list:
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    @property
    def difficulty_levels(self) -> dict:
        levels = {"Advanced": range(2000, 3001), "Extreme": range(3001, BasePeak.EVEREST_HEIGHT + 1)}
        return levels




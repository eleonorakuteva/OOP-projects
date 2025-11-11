from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):

    @property
    def recommended_gear(self) -> list:
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self) -> str:
        if 2_000 <= self.elevation <= 3_000:
            return "Advanced"
        elif self.elevation > 3000:
            return "Extreme"




from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):

    @property
    def recommended_gear(self) -> list:
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self) -> str:
        if 1_500 <= self.elevation <= 2_500:
            return "Advanced"
        elif self.elevation > 2_500:
            return "Extreme"


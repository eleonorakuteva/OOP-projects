from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    INITIAL_STRENGTH: float = 150
    NEEDED_STRENGTH_FOR_CLIMBING: float = 75

    def __init__(self, name):
        super().__init__(name, SummitClimber.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= self.NEEDED_STRENGTH_FOR_CLIMBING


    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= (30 * 2.5)

        elif peak.difficulty_level == "Advanced":
            self.strength -= (30 * 1.3)

        self.conquered_peaks.append(peak.name)

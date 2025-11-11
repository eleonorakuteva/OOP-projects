from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):

    INITIAL_STRENGTH: float = 200
    NEEDED_STRENGTH_FOR_CLIMBING: float = 100

    def __init__(self, name):
        super().__init__(name, ArcticClimber.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= self.NEEDED_STRENGTH_FOR_CLIMBING

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2

        elif peak.difficulty_level == "Advanced":
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)





from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):

    INITIAL_STRENGTH: int = 150
    NEEDED_STRENGTH_FOR_CLIMBING: int = 75

    def __init__(self, name):
        super().__init__(name, SummitClimber.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.NEEDED_STRENGTH_FOR_CLIMBING

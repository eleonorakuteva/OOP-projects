from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):

    INITIAL_STRENGTH: int = 200
    NEEDED_STRENGTH_FOR_CLIMBING: int = 100

    def __init__(self, name):
        super().__init__(name, ArcticClimber.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.NEEDED_STRENGTH_FOR_CLIMBING





from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):

    INITIAL_BUDGET = 1_000.0
    ADVANTAGE_POINTS_PER_WIN = 115

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.INITIAL_BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE_POINTS_PER_WIN
        self.wins += 1
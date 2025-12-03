from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    INITIAL_BUDGET = 500.0
    ADVANTAGE_POINTS_PER_WIN = 145

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.INITIAL_BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE_POINTS_PER_WIN
        self.wins += 1

    @property
    def type(self):
        return "IndoorTeam"
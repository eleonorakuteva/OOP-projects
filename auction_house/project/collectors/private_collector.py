from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    INITIAL_MONEY = 25_000.0
    INITIAL_SPACE = 3_000
    MONEY_TO_INCREASE = 5_000

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_MONEY, self.INITIAL_SPACE)

    def increase_money(self):
        self.available_money += self.MONEY_TO_INCREASE


from project.clients.base_client import BaseClient


class Adult(BaseClient):
    INITIAL_INTEREST = 4.0
    PERCENT_TO_INCREASE_INTEREST = 2.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.INITIAL_INTEREST)

    def increase_clients_interest(self):
        self.interest += self.PERCENT_TO_INCREASE_INTEREST

    @property
    def type_of_loan(self):
        return "MortgageLoan"
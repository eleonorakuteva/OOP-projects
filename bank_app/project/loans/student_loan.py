from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):

    INTEREST_RATE = 1.5
    INCREASE_INTEREST_RATE = 0.2
    AMOUNT = 2_000.00

    def __init__(self):
        super().__init__(self.interest_rate, self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.INCREASE_INTEREST_RATE


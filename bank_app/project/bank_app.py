from project.clients.base_client import BaseClient
from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:

    VALID_TYPES_LOAN = {"StudentLoan": StudentLoan, "MortgageLoan" : MortgageLoan}
    VALID_TYPES_CLIENT = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity):
        self.capacity: int = capacity
        self.loans: list[BaseLoan] = []
        self.clients: list[BaseClient] = []

    def add_loan(self, loan_type: str):
        try:
            new_loan = self.VALID_TYPES_LOAN[loan_type]()
            self.loans.append(new_loan)
            return f"{loan_type} was successfully added."
        except KeyError:
            raise Exception("Invalid loan type!")


    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        try:
            new_client = self.VALID_TYPES_CLIENT[client_type](client_name, client_id, income)
            if self.capacity <= 0:
                return "Not enough bank capacity."

            self.clients.append(new_client)
            return f"{client_type} was successfully added."

        except KeyError:
            raise Exception("Invalid client type!")

    def grant_loan(self, loan_type: str, client_id: str):
        pass

    def remove_client(self, client_id: str):
        pass

    def increase_loan_interest(self, loan_type: str):
        pass

    def increase_clients_interest(self, min_rate: float):
        pass

    def get_statistics(self) -> str:
        total_clients_count = len(self.clients)
        result = [f"Active Clients: {total_clients_count}"]
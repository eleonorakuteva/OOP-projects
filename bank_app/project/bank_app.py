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
            if len(self.clients) >= self.capacity:
                return "Not enough bank capacity."

            self.clients.append(new_client)
            return f"{client_type} was successfully added."

        except KeyError:
            raise Exception("Invalid client type!")


    def grant_loan(self, loan_type: str, client_id: str):

        curr_client = next((c for c in self.clients if c.client_id == client_id), None)
        curr_loan = next((l for l in self.loans if l.loan_type == loan_type), None)

        if not curr_loan and not curr_client:
            pass

        if curr_loan.loan_type != curr_client.type_of_loan:
            raise Exception("Inappropriate loan type!")

        curr_client.loans.append(curr_loan)
        self.loans.remove(curr_loan)
        return f"Successfully granted {loan_type} to {curr_client.name} with ID {client_id}."


    def remove_client(self, client_id: str):

        curr_client = next((c for c in self.clients if c.client_id == client_id), None)
        if curr_client is None:
            raise Exception("No such client!")

        if curr_client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(curr_client)
        return f"Successfully removed {curr_client.name} with ID {client_id}."


    def increase_loan_interest(self, loan_type: str):

        increasing_all_loans_in_the_bank_with_curr_loan_type = [l.increase_interest_rate() for l in self.loans if l.loan_type == loan_type]

        return f"Successfully changed {len(increasing_all_loans_in_the_bank_with_curr_loan_type)} loans."


    def increase_clients_interest(self, min_rate: float):

        increasing_interest_for_all_clients_with_rate_less_then_minimum = [c.increase_clients_interest()
                                                                           for c in self.clients
                                                                           if c.interest < min_rate]
        return f"Number of clients affected: {len(increasing_interest_for_all_clients_with_rate_less_then_minimum)}."


    def get_statistics(self):

        total_clients_income = sum(c.income for c in self.clients)
        loans_count_granted_to_clients = sum(1 for c in self.clients for l in c.loans)
        granted_sum = sum(l.amount for c in self.clients for l in c.loans)
        not_granted_sum = sum(l.amount for l in self.loans)
        avg_client_interest_rate = sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0


        result = (f"Active Clients: {len(self.clients)}\n"
                  f"Total Income: {total_clients_income:.2f}\n"
                  f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}\n"
                  f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}\n"
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")

        return result
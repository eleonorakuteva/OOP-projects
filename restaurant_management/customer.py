class Customer:
    def __init__(self, name:str) -> None:
        self.name = name
        self.order_list :list = []
        self.total_bill = 0

    def view_bill(self):
        return self.total_bill

    def order_item(self):
        pass
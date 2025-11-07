class PaymentSystem:

    PAYMENT_METHODS:list[str] = ["Cash", "Card"]

    def __init__(self):
        self.method: str = ""
        self.customer_name: str = ""
        self.restaurant_name: str = ""
        self.amount_paid: float = 0.0
        self.tip: float = 0.0
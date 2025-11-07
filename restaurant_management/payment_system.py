class PaymentSystem:

    PAYMENT_METHODS:list[str] = ["Cash", "Card"]
    payment_history: list[dict[str, str | float]] = []

    def __init__(self):
        self.method: str = ""
        self.customer_name: str = ""
        self.restaurant_name: str = ""
        self.amount_paid: float = 0.0
        self.tip: float = 0.0
        PaymentSystem.payment_history.append(
            {
                "customer" : self.customer_name. title(),
                "method" : self.method.lower(),
                "amount" : self.amount_paid,
                "tip" : self.tip,
                "date" : "dd.mm.yyyy"
             }
        )
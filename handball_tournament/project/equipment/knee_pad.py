from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):

    INITIAL_PROTECTION: int = 120
    INITIAL_PRICE: float = 15.0
    INCREASING_PRICE_PERCENT = 1.2

    def __init__(self):
        super().__init__(protection=self.INITIAL_PROTECTION, price=self.INITIAL_PRICE)

    def increase_price(self):
        self.price *= self.INCREASING_PRICE_PERCENT


from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):

    INITIAL_PROTECTION: int = 90
    INITIAL_PRICE: float = 25.0
    INCREASING_PRICE_PERCENT = 1.1

    def __init__(self):
        super().__init__(protection=self.INITIAL_PROTECTION, price=self.INITIAL_PRICE)

    def increase_price(self):
        self.price *= self.INCREASING_PRICE_PERCENT


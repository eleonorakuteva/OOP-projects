from project.products.base_product import BaseProduct


class Chair(BaseProduct):

    MATERIAL = 'Wood'
    SUB_TYPE = 'Furniture'
    DISCOUNT = 0.9

    def __init__(self, model: str, price: float):
        super().__init__(model, price, material=self.MATERIAL, sub_type=self.SUB_TYPE)

    def discount(self):
        self.price *= self.DISCOUNT
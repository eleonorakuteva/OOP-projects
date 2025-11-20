from project.products.base_product import BaseProduct


class Chair(BaseProduct):

    MATERIAL = 'Wood/Plastic'
    SUB_TYPE = 'Toys'
    DISCOUNT = 0.8

    def __init__(self, model: str, price: float):
        super().__init__(model, price, material=self.MATERIAL, sub_type=self.SUB_TYPE)

    def discount(self):
        self.price *= self.DISCOUNT
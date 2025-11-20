from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):

    INITIAL_CAPACITY = 50

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)

    @property
    def store_type(self):
        return f"{self.__class__.__name__}"

    @property
    def permitted_sub_type(self):
        return 'Furniture'

    def store_stats(self):
        available_capacity = self.INITIAL_CAPACITY - len(self.products)
        result = [f"Store: {self.name}, location: {self.location}, available capacity: {available_capacity}",
                  self.get_estimated_profit(), "**Furniture for sale:"]

        product_dict = {}
        products_model_price = [(p.model, p.price)  for p in self.products]
        sorted_products_per_model = sorted(products_model_price, key=lambda kvp: kvp[0])

        for model, price in sorted_products_per_model:
            if model not in product_dict:
                product_dict[model] = [0, 0]
            product_dict[model][0] += 1
            product_dict[model][1] += price

        for p_model, p_info in product_dict.items():
            num_of_product_pieces = p_info[0]
            avg_price_per_model = p_info[1] / num_of_product_pieces
            result.append(f"{p_model}: {num_of_product_pieces}pcs, average price: {avg_price_per_model:.2f}")


        return '\n'.join(result)

p1 = Chair("model1", 10)
p2 = Chair("a_model1", 10)
p3 = Chair("b_model1", 10)
p4 = Chair("model1", 10)
p5 = HobbyHorse("horse1", 20)
p6 = HobbyHorse("horse1", 20)
p7 = HobbyHorse("horse1", 20)
p8 = HobbyHorse("aaahorse1", 20)
furn = FurnitureStore("store", "as3")
furn.products.append(p1)
furn.products.append(p2)
furn.products.append(p3)
furn.products.append(p4)
furn.products.append(p5)
furn.products.append(p6)
furn.products.append(p7)
furn.products.append(p8)

print(furn.store_stats())
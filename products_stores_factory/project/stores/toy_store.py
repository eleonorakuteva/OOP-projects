from project.stores.base_store import BaseStore


class ToyStore(BaseStore):

    INITIAL_CAPACITY = 100

    def __init__(self, name: str, location: str):
        super().__init__(name, location, self.INITIAL_CAPACITY)

    @property
    def store_type(self):
        return f"{self.__class__.__name__}"

    def store_stats(self):
        available_capacity = self.INITIAL_CAPACITY - len(self.products)
        result = [f"Store: {self.name}, location: {self.location}, available capacity: {available_capacity}",
                  self.get_estimated_profit(), "**Toys for sale:"]

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

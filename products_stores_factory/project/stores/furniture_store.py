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

        for product_ in self.products:
            product_dict[product_.model]= product_dict.get(product_.model, {"count": 0, "total_price": 0})
            product_dict[product_.model]["count"] += 1
            product_dict[product_.model]["total_price"] += product_.price



        for p_model in sorted(product_dict.keys()):
            num_of_product_pieces = product_dict[p_model]["count"]
            avg_price_per_model = product_dict[p_model]["total_price"] / num_of_product_pieces
            result.append(f"{p_model}: {num_of_product_pieces}pcs, average price: {avg_price_per_model:.2f}")


        return '\n'.join(result)


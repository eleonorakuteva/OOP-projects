from project.products.base_product import BaseProduct
from project.stores.base_store import BaseStore
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:

    VALID_PRODUCT_TYPES = {"Chair" : Chair, "HobbyHorse": HobbyHorse, }
    VALID_STORES_TYPE = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []


    def produce_item(self, product_type: str, model: str, price: float):
        try:
            new_product = self.VALID_PRODUCT_TYPES[product_type](model, price)
            self.products.append(new_product)
            return f"A product of sub-type {new_product.sub_type} was produced."
        except KeyError:
            raise Exception("Invalid product type!")


    def register_new_store(self, store_type: str, name: str, location: str):
        try:
            new_store = self.VALID_STORES_TYPE[store_type](name, location)
            self.stores.append(new_store)
            return f"A new {store_type} was successfully registered."
        except KeyError:
            raise Exception(f"{store_type} is an invalid type of store!")


    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        pass

    def unregister_store(self, store_name: str):
        pass


    def discount_products(self, product_model: str):
        pass


    def request_store_stats(self, store_name: str):
        pass

    def statistics(self):
        pass





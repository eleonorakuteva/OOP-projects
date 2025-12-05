from project.clients.base_client import BaseClient
from project.plants.base_plant import BasePlant


class FlowerShopManager:

    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        pass

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        pass

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        pass

    def remove_plant(self, plant_name: str):
        pass

    def remove_clients(self):
        pass

    def shop_report(self):
        pass
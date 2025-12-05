from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:

    VALID_TYPES_PLANTS = {
        "Flower": Flower,
        "LeafPlant": LeafPlant
    }

    VALID_TYPES_CLIENTS = {
        "BusinessClient": BusinessClient,
        "RegularClient": RegularClient
    }

    def __init__(self):
        self.income: float = 0.0
        self.plants: list[BasePlant] = []
        self.clients: list[BaseClient] = []

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        try:
            new_plant = self.VALID_TYPES_PLANTS[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)
        except KeyError:
            raise ValueError("Unknown plant type!")

        self.plants.append(new_plant)
        return f"{plant_name} is added to the shop as {plant_type}."


    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        try:
            new_client = self.VALID_TYPES_CLIENTS[client_type](client_name, client_phone_number)
        except KeyError:
            raise ValueError("Unknown client type!")

        is_already_client = self._check_client_by_phone_number(client_phone_number)
        if is_already_client:
            raise ValueError("This phone number has been used!")

        self.clients.append(new_client)
        return f"{client_name} is successfully added as a {client_type}."


    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):

        curr_client = self._check_client_by_phone_number(client_phone_number)
        if not curr_client:
            raise ValueError("Client not found!")



    def remove_plant(self, plant_name: str):
        pass

    def remove_clients(self):
        pass

    def shop_report(self):
        pass


    def _check_client_by_phone_number(self, phone_number):
        return next((c for c in self.clients if c.phone_number == phone_number), None)
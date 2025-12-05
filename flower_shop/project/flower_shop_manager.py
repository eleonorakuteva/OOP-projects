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
        self.count_of_orders = 0

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

        is_already_client = self._check_for_existence_client_by_phone_number(client_phone_number)
        if is_already_client:
            raise ValueError("This phone number has been used!")

        self.clients.append(new_client)
        return f"{client_name} is successfully added as a {client_type}."


    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):

        curr_client = self._check_for_existence_client_by_phone_number(client_phone_number)
        if not curr_client:
            raise ValueError("Client not found!")

        has_plant = self._check_for_existence_plant_by_plant_name(plant_name)
        if not has_plant:
            raise ValueError("Plants not found!")

        return self.sell_actions(plant_quantity, plant_name, curr_client)



    def sell_actions(self, quantity_to_sold: int, plant_name: str, client: BaseClient):

        filtered_plants_by_name = [p for p in self.plants if p.name == plant_name]
        count_filtered_plants = len(filtered_plants_by_name)

        if quantity_to_sold > count_filtered_plants:
            return "Not enough plant quantity."

        plants_to_remove = filtered_plants_by_name[:quantity_to_sold]

        order_amount = 0
        for curr_plant in plants_to_remove:
            self.plants.remove(curr_plant)
            price_curr_plant = curr_plant.price - (curr_plant.price * client.discount / 100)
            order_amount += price_curr_plant

        self._update_count_of_orders()
        self.income += order_amount
        client.update_total_orders()
        client.update_discount()

        return f"{quantity_to_sold}pcs. of {plant_name} plant sold for {order_amount:.2f}"

    def _update_count_of_orders(self):
        self.count_of_orders += 1

    def remove_plant(self, plant_name: str):
        plant = self._check_for_existence_plant_by_plant_name(plant_name)
        if plant is None:
            return "No such plant name."

        self.plants.remove(plant)
        return f"Removed {plant.plant_details()}"

    def remove_clients(self):
        removed_clients = [c for c in self.clients if c.total_orders == 0]
        if removed_clients:
            [self.clients.remove(c) for c in removed_clients]

        return f"{len(removed_clients)} client/s removed."

    def shop_report(self) -> str:

        result = [
            "~Flower Shop Report~",
            f"Income: {self.income:.2f}",
            f"Count of orders: {self.count_of_orders}",
            f"~~Unsold plants: {len(self.plants)}~~"
        ]

        plants_dict = {}
        for plant in self.plants:
            if plant.name not in plants_dict:
                plants_dict[plant.name] = 0
            plants_dict[plant.name] += 1

        sorted_plants = sorted(plants_dict.items(), key=lambda kvp: (-kvp[1], kvp[0]))

        for plant_name, count in sorted_plants:
            result.append(f"{plant_name}: {count}")

        result.append(f"~~Clients number: {len(self.clients)}~~")


        sorted_clients = sorted(self.clients, key=lambda c: (-c.total_orders, c.phone_number))
        for client in sorted_clients:
            result.append(client.client_details())

        return '\n'.join(result)


    def _check_for_existence_client_by_phone_number(self, phone_number):
        return next((c for c in self.clients if c.phone_number == phone_number), None)

    def _check_for_existence_plant_by_plant_name(self, plant_name):
        return next((p for p in self.plants if p.name == plant_name), None)

    def _return_number_of_all_plants_with_given_name(self, plant_name):
        return len([p for p in self.plants if p.name == plant_name])
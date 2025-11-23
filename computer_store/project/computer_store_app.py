from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop

class ComputerStoreApp:

    VALID_TYPES_COMPUTERS = {
        "Desktop Computer" : DesktopComputer,
        "Laptop" : Laptop,
    }

    def __init__(self):
        self.warehouse: list[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        try:
            computer = self.VALID_TYPES_COMPUTERS[type_computer](manufacturer, model)
        except KeyError:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration: str = computer.configure_computer(processor, ram)

        self.warehouse.append(computer)

        return configuration

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):

        has_wanted_computer = next((c for c in self.warehouse
                                    if c.price <= client_budget
                                    and c.processor == wanted_processor
                                    and c.ram >= wanted_ram), None)

        if has_wanted_computer is None:
            raise Exception("Sorry, we don't have a computer for you.")

        price_diff = client_budget - has_wanted_computer.price
        self.profits += price_diff
        self.warehouse.remove(has_wanted_computer)

        return f"{has_wanted_computer} sold for {client_budget}$."

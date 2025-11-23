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
        pass

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        pass
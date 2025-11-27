from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread



class ChristmasPastryShopApp:

    VALID_DELICACIES_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: list[Booth] = []
        self.delicacies: list[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        try:
            new_delicacy = self.VALID_DELICACIES_TYPES[type_delicacy](name, price)
        except KeyError:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if new_delicacy in self.delicacies:
            raise Exception(f"{name} already exists!")

        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."


    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        try:
            new_booth = self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
        except KeyError:
            raise Exception(f"{type_booth} is not a valid booth!")

        if new_booth in self.booths:
            raise Exception(f"Booth number {booth_number} already exists!")

        self.booths.append(new_booth)
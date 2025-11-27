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

        has_delicacy_with_same_name = next((d for d in self.delicacies if d.name == name),None)

        if has_delicacy_with_same_name:
            raise Exception(f"{name} already exists!")

        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."


    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        try:
            new_booth = self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
        except KeyError:
            raise Exception(f"{type_booth} is not a valid booth!")

        has_booth_with_same_booth_number = next((b for b in self.booths if b.booth_number == booth_number), None)

        if has_booth_with_same_booth_number:
            raise Exception(f"Booth number {booth_number} already exists!")

        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        # if number_of_people <= 0:
        #     return "not correct number_of_people provided"

        have_booth = next((b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people), None)

        if not have_booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        have_booth.reserve(number_of_people)
        return f"Booth {have_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        pass
from project.vehicles.base_vehicle import BaseVehicle
from math import floor


class CargoVan(BaseVehicle):

    MAX_MILEAGE = 180

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage= CargoVan.MAX_MILEAGE)


    def drive(self, mileage: float):
        # when driving CargoVan, you should reduce an additional 5%, because of the load.
        percentage = ((mileage / CargoVan.MAX_MILEAGE) * 100) + 5
        round_percentage = floor(percentage + 0.5)
        self.battery_level -= round_percentage
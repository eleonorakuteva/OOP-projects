from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):

    MAX_MILEAGE = 180

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage= self.MAX_MILEAGE)


    def drive(self, mileage: float):
        # when driving CargoVan, you should reduce an additional 5%, because of the load.
        percentage = (mileage / self.MAX_MILEAGE) * 100
        round_percentage = round(percentage + 5)
        self.battery_level -= round_percentage
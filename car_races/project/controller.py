from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    VALID_TYPES_OF_CARS = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: list[Car] = []
        self.drivers: list[Driver] = []
        self.races: list[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        try:
            new_car = self.VALID_TYPES_OF_CARS[car_type](model, speed_limit)
        except KeyError:
            return None

        same_model_already_exists = next((c for c in self.cars if c.model == model), None)
        if same_model_already_exists:
            raise Exception(f"Car {model} is already created!")

        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver_already_exists = next((d for d in self.drivers if d.name == driver_name), None)
        if driver_already_exists:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

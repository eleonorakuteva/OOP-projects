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
        driver_already_exists = self._driver_found_by_name(driver_name)
        if driver_already_exists:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."


    def create_race(self, race_name: str):
        race_already_exists = self._race_found_by_name(race_name)
        if race_already_exists:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."


    def add_car_to_driver(self, driver_name: str, car_type: str):
        curr_driver = self._driver_found_by_name(driver_name)
        if not curr_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        curr_car = self._last_available_car_found_by_type(car_type)
        if not curr_car:
            raise Exception(f"Car {car_type} could not be found!")

        # if driver doesn't have a car
        if curr_driver.car is None:
            return f"Driver {driver_name} chose the car {curr_car.model}."

        # if driver has a car
        old_model = curr_driver.car.model
        # change the old one with the curr one
        curr_driver.car = curr_car
        new_model = curr_driver.car.model
        return (f"Driver {driver_name} changed his car from "
                f"{old_model} to {new_model}.")


    def _driver_found_by_name(self, driver_name)-> bool | Driver:
        driver = next((d for d in self.drivers if d.name == driver_name), None)
        if driver:
            return driver
        return False

    def _race_found_by_name(self, race_name) -> bool | Race:
        race = next((r for r in self.races if r.name == race_name), None)
        if race:
            return race
        return False

    def _last_available_car_found_by_type(self, car_type) -> bool | Car:
        reversed_cars = self.cars[::-1]
        car = next((c for c in reversed_cars if type(c).__name__ == car_type and not c.is_taken), None)
        if car:
            return car
        return False


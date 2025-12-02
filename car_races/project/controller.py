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
        if not curr_driver.has_car:
            curr_car.is_taken = True
            curr_driver.car = curr_car
            return f"Driver {driver_name} chose the car {curr_car.model}."

        # if driver has a car
        old_model = curr_driver.car.model
        curr_driver.car.is_taken = False
        # change the old one with the curr one
        curr_driver.car = curr_car
        curr_car.is_taken = True
        new_model = curr_driver.car.model
        return (f"Driver {driver_name} changed his car from "
                f"{old_model} to {new_model}.")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        curr_race = self._race_found_by_name(race_name)
        if not curr_race:
            raise Exception(f"Race {race_name} could not be found!")

        curr_driver = self._driver_found_by_name(driver_name)
        if not curr_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not curr_driver.has_car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        # driver already participated in the race
        if curr_driver in curr_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        else:
            curr_race.drivers.append(curr_driver)
            return f"Driver {driver_name} added in {race_name} race."



    def start_race(self, race_name: str):
        curr_race = self._race_found_by_name(race_name)
        if not curr_race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(curr_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = sorted(curr_race.drivers, key=lambda d: -d.car.speed_limit)
        # print([f"{d.name}, {d.car.speed_limit}" for d in winners])
        result = []
        for idx in range(0, 3):
            speed_limit = winners[idx].car.speed_limit
            driver_name = winners[idx].name
            winners[idx].number_of_wins += 1
            result.append(f"Driver {driver_name} wins "
                          f"the {race_name} race with a speed "
                          f"of {speed_limit}.")
        return '\n'.join(result)


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


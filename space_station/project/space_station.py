from collections import deque
from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    VALID_ASTRONAUT_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0


    def add_astronaut(self, astronaut_type: str, name: str):
        try:
            new_astronaut = self.VALID_ASTRONAUT_TYPES[astronaut_type](name)
        except KeyError:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        list_of_items_planet_have = items.split(', ')
        new_planet = Planet(name)
        new_planet.extend_items(list_of_items_planet_have)

        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            self.astronaut_repository.remove(astronaut)
            return f"Astronaut {name} was retired!"
        elif astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for ast in self.astronaut_repository.astronauts:
            ast.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")

        top_five_suitable_astronauts = self._check_for_most_suitable_astronauts()

        if self.is_success_collecting_items_from_planet(planet, top_five_suitable_astronauts):
            astronauts_participated = []
            for a in top_five_suitable_astronauts:
                astronauts_participated.append(a.name)
            return (f"Planet: {planet_name} was explored. "
                    f"{', '.join(astronauts_participated)} astronauts participated in collecting items.")

        return "Mission is not completed."


    def report(self) -> str:
        result = [f"{self.successful_missions} successful missions!",
                  f"{self.not_completed_missions} missions were not completed!",
                  f"Astronauts' info:"]

        for a in self.astronaut_repository.astronauts:
            result.append(a.details())

        return '\n'.join(result)

    def is_success_collecting_items_from_planet(self, planet: Planet, astronauts: list[Astronaut]):
        astronauts = deque(astronauts)

        while True:
            # print(planet.items)
            # print([a.oxygen for a in astronauts])
            if not planet.items:
                break
            if not astronauts:
                break

            astro = astronauts[0]
            astro.breathe()
            if astro.oxygen > 0:
                collected_item = planet.items.pop()
                astro.backpack.append(collected_item)

            elif astro.oxygen <= 0:
                astro.oxygen = 0
                astronauts.popleft()

        if not planet.items:
            self.successful_missions += 1
            return True
        self.not_completed_missions += 1
        return False



    def _check_for_most_suitable_astronauts(self):
        sorted_astronauts_by_highest_amount_oxygen = sorted(
            self.astronaut_repository.astronauts,
            key=lambda a: -a.oxygen)
        # print([a.oxygen for a in sorted_astronauts_by_highest_amount_oxygen])
        suitable_astronauts = [a for a in sorted_astronauts_by_highest_amount_oxygen if a.oxygen > 30]
        # print([a.oxygen for a in suitable_astronauts])
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        top_five_suitable: list = []
        if len(suitable_astronauts) <= 5:
            top_five_suitable = suitable_astronauts
        if len(suitable_astronauts) > 5:
            top_five_suitable = suitable_astronauts[:5]

        # print([a.oxygen for a in top_five_suitable])
        return top_five_suitable






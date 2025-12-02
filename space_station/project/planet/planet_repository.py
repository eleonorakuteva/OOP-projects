from project.planet.planet import Planet


class PlanetRepository:

    def __init__(self):
        self.planets: list[Planet] = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        self.planets.remove(planet)

    def find_by_name(self, name: str):
        return next((p for p in self.planets if p.name == name), None)
    
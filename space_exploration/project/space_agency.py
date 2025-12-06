from project.astronauts.base_astronaut import BaseAstronaut
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.base_station import BaseStation
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:

    VALID_ASTRONAUTS = {
        "EngineerAstronaut": EngineerAstronaut,
        "ScientistAstronaut": ScientistAstronaut
    }

    VALID_STATIONS = {
        "ResearchStation": ResearchStation,
        "MaintenanceStation": MaintenanceStation
    }

    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []
        self.stations: list[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        try:
            new_astronaut = self.VALID_ASTRONAUTS[astronaut_type](astronaut_id_number, astronaut_salary)
        except KeyError:
            raise ValueError("Invalid astronaut type!")

        has_astronaut = self._search_for_astronaut_by_id(astronaut_id_number)
        if has_astronaut:
            raise ValueError(f"{astronaut_id_number} has been already added!")

        self.astronauts.append(new_astronaut)
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."


    def add_station(self, station_type: str, station_name: str):
        try:
            new_station = self.VALID_STATIONS[station_type](station_name)
        except KeyError:
            raise ValueError("Invalid station type!")

        has_station = self._search_for_station_with_given_name(station_name)
        if has_station:
            raise ValueError(f"{station_name} has been already added!")

        self.stations.append(new_station)
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):

        curr_station = self._search_for_station_with_given_name(station_name)
        if curr_station is None:
            raise ValueError(f"Station {station_name} does not exist!")

        curr_astronaut = self._search_for_astronaut_by_type(astronaut_type)
        if curr_astronaut is None:
            raise ValueError("No available astronauts of the type!")


        if not self._has_available_capacity(curr_station):
            return "This station has no available capacity."

        return self.assigning_to_station(curr_station, curr_astronaut)



    def assigning_to_station(self, station: BaseStation, astronaut: BaseAstronaut):
        self.astronauts.remove(astronaut)
        station.astronauts.append(astronaut)
        station.capacity -= 1
        return f"{astronaut.id_number} was assigned to {station.name}."

    @staticmethod
    def _has_available_capacity(station: BaseStation) -> bool:
        return station.capacity >= 1

    @staticmethod
    def train_astronauts(station: BaseStation, sessions_number: int):

        for _ in range(sessions_number):
            for a in station.astronauts:
                a.train()

        total_stamina = sum(a.stamina for a in station.astronauts)

        return (f"{station.name} astronauts have {total_stamina} "
                f"total stamina after {sessions_number} training session/s.")

    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        curr_astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)

        if curr_astronaut is None or curr_astronaut.stamina == 100:
            return "The retirement process was canceled."

        return self.retire_valid_astronaut(station, curr_astronaut)

    @staticmethod
    def retire_valid_astronaut(station: BaseStation, astronaut: BaseAstronaut):
        station.capacity += 1
        station.astronauts.remove(astronaut)

        return f"Retired astronaut {astronaut.id_number}."


    def agency_update(self, min_value: float):

        for station in self.stations:
            station.update_salaries(min_value)

        sorted_stations = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))

        available_astronauts_count = len(self.astronauts)
        stations_total_count = len(self.stations)
        total_available_capacity = sum(s.capacity for s in self.stations) if self.stations else 0
        result = [
            "*Space Agency Up-to-Date Report*",
            f"Total number of available astronauts: {available_astronauts_count}",
            f"**Stations count: {stations_total_count}; Total available capacity: {total_available_capacity}**"
        ]

        for station in sorted_stations:
            result.append(station.status())

        return '\n'.join(result)



    def _search_for_station_with_given_name(self, given_name):
        return next((s for s in self.stations if s.name == given_name), None)


    def _search_for_astronaut_by_id(self, given_id):
        return next((a for a in self.astronauts if a.id_number == given_id), None)


    def _search_for_astronaut_by_type(self, given_type):
        return next((a for a in self.astronauts if type(a).__name__ == given_type), None)


from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):

    INITIAL_CAPACITY = 3

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_CAPACITY)

    @property
    def salary_update_based_on_station_type(self):
        return 3_000.0

    def update_salaries(self, min_value: float):
        for astro in self.astronauts:
            if astro.salary <= min_value and type(astro).__name__ == "EngineerAstronaut":
                astro.salary += self.salary_update_based_on_station_type


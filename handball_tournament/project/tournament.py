from project.equipment.base_equipment import BaseEquipment
from project.teams.base_team import BaseTeam


class Tournament:

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list[BaseEquipment] = []
        self.teams: list[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        pass

from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:

    VALID_EQUIPMENT_TYPES = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }

    VALID_TEAM_TYPES = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam
    }

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
        try:
            new_equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]
        except KeyError:
            raise Exception("Invalid equipment type!")

        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):

        try:
            new_team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)

        except KeyError:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        pass

    def remove_team(self, team_name: str):
        pass

    def increase_equipment_price(self, equipment_type: str):
        pass

    def play(self, team_name1: str, team_name2: str):
        pass

    def get_statistics(self):
        pass

    def _find_team_by_name(self, team_name):
        return next((t for t in self.teams if t.name == team_name), None)

    def _find_equipment_by_type(self, equipment_type):
        return next(e for e in self.equipment if type(e).__name__ == equipment_type)





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
            new_equipment = self.VALID_EQUIPMENT_TYPES[equipment_type]()
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

        equipment = self._find_equipment_reversed_by_type(equipment_type)

        team = self._find_team_by_name(team_name)
        if not self._is_team_have_enough_budget(team, equipment.price):
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    @staticmethod
    def _is_team_have_enough_budget(team: BaseTeam, amount) -> bool:
        if team.budget >= amount:
            return True
        return False

    def remove_team(self, team_name: str):
        team = self._find_team_by_name(team_name)
        if team is None:
            raise Exception("No such team!")
        if team.wins >= 1:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed_equipments_sum = 0
        if self._find_equipment_reversed_by_type(equipment_type) is not None:
            changed = [e.increase_price() for e in self.equipment if type(e).__name__ == equipment_type]
            changed_equipments_sum = len(changed)
        return f"Successfully changed {changed_equipments_sum}pcs of equipment."


    def play(self, team_name1: str, team_name2: str):
        team_1 = self._find_team_by_name(team_name1)
        team_2 = self._find_team_by_name(team_name2)

        if team_1.type != team_2.type:
            raise Exception("Game cannot start! Team types mismatch!")

        return self._return_winner(team_1, team_2)

    @staticmethod
    def _return_winner(team1, team2):
        if team1.result_points_advantage_and_protection() > team2.result_points_advantage_and_protection():
            team1.win()
            return f"The winner is {team1.name}."
        elif team2.result_points_advantage_and_protection() > team1.result_points_advantage_and_protection():
            team2.win()
            return f"The winner is {team2.name}."
        elif team1.result_points_advantage_and_protection() == team2.result_points_advantage_and_protection():
            return f"No winner in this game."


    def get_statistics(self):
        result = [f"Tournament: {self.name}",
                  f"Number of Teams: {len(self.teams)}",
                  "Teams:"]

        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        for t in sorted_teams:
            result.append(t.get_statistics())

        return '\n'.join(result)


    def _find_team_by_name(self, team_name):
        return next((t for t in self.teams if t.name == team_name), None)


    def _find_equipment_reversed_by_type(self, equipment_type):
        reverse_equipment = self.equipment[::-1]
        equipment = next((e for e in reverse_equipment if type(e).__name__ == equipment_type), None)
        return equipment





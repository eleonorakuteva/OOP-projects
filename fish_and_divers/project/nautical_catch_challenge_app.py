from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish

class NauticalCatchChallengeApp:

    VALID_DIVER_TYPES = {"FreeDiver" : FreeDiver,
                         "ScubaDiver": ScubaDiver}

    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        try:
            new_diver = self.VALID_DIVER_TYPES[diver_type](diver_name)

        except KeyError:
            return f"{diver_type} is not allowed in our competition."

        try:
            next(d for d in self.divers if d.name == diver_name)
            return f"{diver_name} is already a participant."

        except StopIteration:
            self.divers.append(new_diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."


    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        pass

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        pass

    def health_recovery(self):
        pass

    def diver_catch_report(self, diver_name: str):
        pass

    def competition_statistics(self):
        pass
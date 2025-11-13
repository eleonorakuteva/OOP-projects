from project.divers.base_diver import BaseDiver
from project.fish.base_fish import BaseFish

class NauticalCatchChallengeApp:

    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        pass

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
from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    VALID_DIVER_TYPES = {"FreeDiver" : FreeDiver,
                         "ScubaDiver": ScubaDiver}

    VALID_FISH_TYPES = {"PredatoryFish" : PredatoryFish,
                        "DeepSeaFish" : DeepSeaFish,}

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
        try:
            new_fish = self.VALID_FISH_TYPES[fish_type](fish_name, points)

        except KeyError:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            next(f for f in self.fish_list if f.name == fish_name)
            return f"{fish_name} is already permitted."

        except StopIteration:
            self.fish_list.append(new_fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."


    def diver_validation(self, diver_name: str):
        try:
            curr_diver = next(d for d in self.divers if d.name == diver_name)
            return curr_diver
        except StopIteration:
            return None

    def fish_validation(self, fish_name: str):
        try:
            curr_fish = next(f for f in self.fish_list if f.name == fish_name)
            return curr_fish
        except StopIteration:
            return None

    @staticmethod
    def diver_health_check(diver: BaseDiver):
        return True if diver.has_health_issue else False

    @staticmethod
    def oxygen_level_comparison(diver: BaseDiver, fish: BaseFish, is_lucky: bool):
        if diver.oxygen_level < fish.time_to_catch:
            return False

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                return True
            else:
                return False

        elif diver.oxygen_level > fish.time_to_catch:
            return True


    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        curr_diver = self.diver_validation(diver_name)
        if not curr_diver:
            return f"{diver_name} is not registered for the competition."

        curr_fish = self.fish_validation(fish_name)
        if not curr_fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        # ???
        if not self.diver_health_check(curr_diver):
            return f"{diver_name} will not be allowed to dive, due to health issues."

        # ???
        if self.oxygen_level_comparison(curr_diver, curr_fish, is_lucky):
            curr_diver.hit(curr_fish)
            return f"{diver_name} hits a {curr_fish.points}pt. {fish_name}."
        else:
            curr_diver.miss(curr_fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."



    def health_recovery(self):
        pass

    def diver_catch_report(self, diver_name: str):
        pass

    def competition_statistics(self):
        pass
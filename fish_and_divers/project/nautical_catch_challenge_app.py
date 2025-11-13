from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    VALID_DIVER_TYPES = {"FreeDiver" : FreeDiver,
                         "ScubaDiver": ScubaDiver,}

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


    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        message = None
        try:
            curr_diver = next(d for d in self.divers if d.name == diver_name)
        except StopIteration:
            return f"{diver_name} is not registered for the competition."

        try:
            curr_fish = next(f for f in self.fish_list if f.name == fish_name)
        except StopIteration:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if curr_diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if curr_diver.oxygen_level < curr_fish.time_to_catch:
            curr_diver.miss(curr_fish.time_to_catch)
            message = f"{diver_name} missed a good {fish_name}."

        elif curr_diver.oxygen_level == curr_fish.time_to_catch:
            if is_lucky:
                curr_diver.hit(curr_fish)
                message = f"{diver_name} hits a {curr_fish.points}pt. {fish_name}."
            else:
                curr_diver.miss(curr_fish.time_to_catch)
                message = f"{diver_name} missed a good {fish_name}."

        elif curr_diver.oxygen_level > curr_fish.time_to_catch:
            curr_diver.hit(curr_fish)
            message = f"{diver_name} hits a {curr_fish.points}pt. {fish_name}."

        if curr_diver.oxygen_level == 0:
            curr_diver.update_health_status()

        return message


    def health_recovery(self):
        divers_with_health_issues = [d for d in self.divers if d.has_health_issue == True]
        for diver in self.divers:
            if diver in divers_with_health_issues:
                diver.has_health_issue = False
                diver.renew_oxy()
        return f"Divers recovered: {len(divers_with_health_issues)}"


    def diver_catch_report(self, diver_name: str):
        pass
        # curr_diver = next((d for d in self.divers if d.name == diver_name), None)
        # if curr_diver:
        #     return (f"**{diver_name} Catch Report**\n"
        #             f"{'\n'.join(f.fish_details() for f in curr_diver.catch)}")


    def competition_statistics(self):
        all_divers_in_good_health = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(all_divers_in_good_health, key= lambda d: (-d.competition_points, -len(d.catch), d.name))
        result = ["**Nautical Catch Challenge Statistics**",]
        for d in sorted_divers:
            result.append(str(d))
        return '\n'.join(result)

#
# nautical_catch_challenge = NauticalCatchChallengeApp()
#
# # Dive into competition
# print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "MaxineHarper"))
# print(nautical_catch_challenge.dive_into_competition("FreeDiver", "JamalCarter"))
# print(nautical_catch_challenge.dive_into_competition("SkyDiver", "FionaBennett"))
# print(nautical_catch_challenge.dive_into_competition("FreeDiver", "OscarWallace"))
# print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "LilaMoreno"))
# print(nautical_catch_challenge.dive_into_competition("FreeDiver", "LilaMoreno"))
#
# # Swim into competition
# print(nautical_catch_challenge.swim_into_competition("ReefFish", "AzureDamselfish", 8.7))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "BluestripeSnapper", 6.3))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "YellowtailSurgeonfish", 5.0))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Barracuda", 9.2))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Coryphaena", 9.7))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Bluefish", 4.4))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "SwordFish", 10.0))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Mahi-Mahi", 9.1))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Tuna", 8.5))
# print(nautical_catch_challenge.swim_into_competition("AquariumFish", "SilverArowana", 3.3))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Barracuda", 8.6))
#
# # Conduct fishing competitions
# print(nautical_catch_challenge.chase_fish("FionaBennett", "AzureDamselfish", False))
# print(nautical_catch_challenge.chase_fish("JamalCarter", "SilverArowana", True))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "YellowtailSurgeonfish", False))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "Mahi-Mahi", False))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "Tuna", False))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "Coryphaena", True))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "BluestripeSnapper", True))
# print(nautical_catch_challenge.chase_fish("OscarWallace", "Barracuda", False))
# print(nautical_catch_challenge.chase_fish("OscarWallace", "YellowtailSurgeonfish", False))
# print(nautical_catch_challenge.chase_fish("OscarWallace", "Tuna", True))
# print(nautical_catch_challenge.chase_fish("JamalCarter", "Barracuda", True))
# print(nautical_catch_challenge.chase_fish("JamalCarter", "YellowtailSurgeonfish", True))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))
#
# # Check health recovery
# print(nautical_catch_challenge.health_recovery())
#
# # Conduct fishing competitions
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))
#
# # View catch reports
# print(nautical_catch_challenge.diver_catch_report("LilaMoreno"))
#
# # View competition statistics
# print(nautical_catch_challenge.competition_statistics())


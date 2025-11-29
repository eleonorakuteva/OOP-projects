from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    VALID_TYPE_HORSES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses: list[Horse] = []
        self.jockeys: list[Jockey] = []
        self.horse_races: list[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if horse_type not in self.VALID_TYPE_HORSES.keys():
            pass

        have_horse_with_same_name = next((h for h in self.horses if h.name == horse_name), None)

        if have_horse_with_same_name:
            raise Exception(f"Horse {horse_name} has been already added!")

        new_horse = self.VALID_TYPE_HORSES[horse_type](horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."


    def add_jockey(self, jockey_name: str, age: int):
        has_jockey_with_same_name = next((j for j in self.jockeys if j.name == jockey_name), None)

        if has_jockey_with_same_name:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jokey = Jockey(jockey_name, age)
        self.jockeys.append(new_jokey)
        return f"Jockey {jockey_name} is added."


    def create_horse_race(self, race_type: str):

        has_race_with_same_race_type = next((r for r in self.horse_races if r.race_type == race_type), None)

        if has_race_with_same_race_type:
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."


    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        pass

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        pass

    def start_horse_race(self, race_type: str):
        pass


# horseRaceApp = HorseRaceApp()
# print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
# print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
# print(horseRaceApp.add_jockey("Peter", 19))
# print(horseRaceApp.add_jockey("Mariya", 21))
# print(horseRaceApp.create_horse_race("Summer"))


# print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
# print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.start_horse_race("Summer"))


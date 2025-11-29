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

    MINIMUM_PARTICIPANTS_IN_RACE = 2

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
        curr_jockey = next((j for j in self.jockeys if j.name == jockey_name), None)

        if curr_jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        all_horses_from_given_type = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken]

        if not all_horses_from_given_type:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if curr_jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        last_horse_from_list = all_horses_from_given_type.pop()
        horse_name = last_horse_from_list.name
        last_horse_from_list.is_taken = True
        curr_jockey.horse = last_horse_from_list
        return f"Jockey {jockey_name} will ride the horse {horse_name}."



    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race_with_given_type = self._search_by_race_type(race_type)

        curr_jockey = next((j for j in self.jockeys if jockey_name == j.name), None)

        if curr_jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if curr_jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        race_with_given_type.jockeys.append(curr_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."


    def start_horse_race(self, race_type: str):
        curr_race = self._search_by_race_type(race_type)

        participant_in_curr_race = self._participant_in_current_race(curr_race)

        if participant_in_curr_race < self.MINIMUM_PARTICIPANTS_IN_RACE:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        

    @staticmethod
    def _participant_in_current_race(race: HorseRace) -> int:
        return len(race.jockeys)

    def _search_by_race_type(self, race_type):
        race_with_given_type = next((r for r in self.horse_races if r.race_type == race_type), None)

        if race_with_given_type is None:
            raise Exception(f"Race {race_type} could not be found!")

        return race_with_given_type



horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))


print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))


print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))


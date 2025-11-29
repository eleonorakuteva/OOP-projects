from project.jockey import Jockey


class HorseRace:

    VALID_TYPE_RACES = ["Winter", "Spring", "Autumn", "Summer"]

    def __init__(self, race_type: str):
        self.race_type = race_type
        # will store all the jockeys (objects) who will take part in the race
        self.jockeys: list[Jockey] = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value: str):
        if value not in self.VALID_TYPE_RACES:
            raise ValueError("Race type does not exist!")
        self.__race_type = value
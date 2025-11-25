from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    VALID_MUSICIANS_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }
    VALID_BAND_TYPES = {}

    def __init__(self):
        self.bands: list[Band] = []
        self.musicians: list[Musician] = []
        self.concerts: list[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        try:
            new_musician = self.VALID_MUSICIANS_TYPES[musician_type](name, age)

            if any(m.name == name for m in self.musicians):
                raise Exception(f"{name} is already a musician!")

            self.musicians.append(new_musician)
            return f"{name} is now a {musician_type}."

        except KeyError:
            raise ValueError("Invalid musician type!")

    def create_band(self, name: str):

        if any(b.name == name for b in self.bands):
            raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        new_concert = Concert(genre, audience, ticket_price, expenses, place)

        if any(c.place == place for c in self.concerts):
            raise Exception(f"{place} is already registered for {genre} concert!")

        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."
    

    def add_musician_to_band(self, musician_name: str, band_name: str):
        pass

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        pass

    def start_concert(self, concert_place: str, band_name: str):
        pass


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
        curr_musician = next((m for m in self.musicians if musician_name == m.name), None)
        if curr_musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        curr_band = next((b for b in self.bands if band_name == b.name), None)
        if curr_band is None:
            raise Exception(f"{band_name} isn't a band!")

        curr_band.members.append(curr_musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        curr_band = next((b for b in self.bands if band_name == b.name), None)
        if curr_band is None:
            raise Exception(f"{band_name} isn't a band!")

        member_in_curr_band = next((m for m in curr_band.members if m.name == musician_name), None)
        if member_in_curr_band is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        curr_band.members.remove(member_in_curr_band)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        curr_concert = next((c for c in self.concerts if c.place == concert_place), None)
        curr_band = next((b for b in self.bands if b.name == band_name), None)

        if not curr_concert and not curr_band:
            pass

        drummers = [d for d in curr_band.members if isinstance(d, Drummer)]
        singers = [s for s in curr_band.members if isinstance(s, Singer)]
        guitarists = [g for g in curr_band.members if isinstance(g, Guitarist)]


        if not (drummers and singers and guitarists):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        drummers_have_needed_skill = False
        singers_have_needed_skill = False
        guitarists_have_needed_skill = False

        if curr_concert.genre == "Rock":
            drummers_have_needed_skill = all("play the drums with drumsticks" in  d.skills for d in drummers)
            singers_have_needed_skill = all("sing high pitch notes" in  s.skills for s in singers)
            guitarists_have_needed_skill = all("play rock" in  g.skills for g in guitarists)

        elif curr_concert.genre == "Metal":
            drummers_have_needed_skill = all("play the drums with drumsticks" in d.skills for d in drummers)
            singers_have_needed_skill = all("sing low pitch notes" in s.skills for s in singers)
            guitarists_have_needed_skill = all("play metal" in g.skills for g in guitarists)

        elif curr_concert.genre == "Jazz":
            drummers_have_needed_skill = all("play the drums with drum brushes" in d.skills for d in drummers)
            singers_have_needed_skill = all(["sing high pitch notes", "sing low pitch notes"] in s.skills for s in singers)
            guitarists_have_needed_skill = all("play jazz" in g.skills for g in guitarists)


        if drummers_have_needed_skill and singers_have_needed_skill and guitarists_have_needed_skill:
            profit = (curr_concert.audience * curr_concert.ticket_price) - curr_concert.expenses
            return f"{band_name} gained {profit:.2f}$ from the {curr_concert.genre} concert in {concert_place}."
        else:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")







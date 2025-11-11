from webbrowser import Error

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:

    VALID_TYPES_OF_CLIMBERS = {
        "ArcticClimber" : ArcticClimber,
        "SummitClimber": SummitClimber
    }

    VALID_TYPES_OF_PEAKS = {
        "ArcticPeak": ArcticPeak,
        "SummitPeak": SummitPeak,
    }

    def __init__(self):
        self.climbers: list[BaseClimber] = []
        self.peaks: list = [BasePeak]


    def register_climber(self, climber_type: str, climber_name: str) -> str:

        try:
            new_climber = self.VALID_TYPES_OF_CLIMBERS[climber_type](climber_name)

        except KeyError:
            return f"{climber_type} doesn't exist in our register."


        try:
            next(filter(lambda c: c.name == climber_name, self.climbers))
            return f"{climber_name} has been already registered."

        except StopIteration:
            self.climbers.append(new_climber)
            return f"{climber_name} is successfully registered as a {climber_type}."


    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int) -> str:
        try:
            new_peak = self.VALID_TYPES_OF_PEAKS[peak_type](peak_name, peak_elevation)

        except KeyError:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."


    def check_gear(self, climber_name: str, peak_name: str, gear: list[str]) -> str:
        """
        Verifying if every climber has the required gear for each peak.
        """
        climber: BaseClimber = next((c for c in self.climbers if c.name == climber_name), None)
        peak: BasePeak = next((p for p in self.peaks if p.name == peak_name), None)
        if gear == peak.recommended_gear:
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        missing_gear = [g for g in sorted(peak.recommended_gear) if g not in gear]

        return (f"{climber_name} is not prepared to climb {peak_name}. "
                f"Missing gear: {', '.join(missing_gear)}.")


    def perform_climbing(self, climber_name: str, peak_name: str):
        """
        The method is responsible for allowing the climber to conquer a specific peak.
        """
        try:
            climber: BaseClimber = next(filter(lambda c: c.name == climber_name, self.climbers))
        except StopIteration:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak: BasePeak = next(filter(lambda p: p.name == peak_name, self.peaks))
        except StopIteration:
            return f"Peak {peak_name} is not part of the wish list."


        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        elif not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics (self):
        pass


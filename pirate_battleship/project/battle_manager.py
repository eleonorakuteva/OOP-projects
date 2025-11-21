from project.battleships.base_battleship import BaseBattleship
from project.zones.base_zone import BaseZone
from project.zones.royal_zone import RoyalZone
from project.zones.pirate_zone import PirateZone


class BattleManager:

    VALID_ZONES = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}


    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        pass

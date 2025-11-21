from project.battleships.base_battleship import BaseBattleship
from project.zones.base_zone import BaseZone
from project.zones.royal_zone import RoyalZone
from project.zones.pirate_zone import PirateZone
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship

class BattleManager:

    VALID_ZONES = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}
    VALID_SHIP_TYPE = {"RoyalBattleship": RoyalBattleship, "PirateBattleship": PirateBattleship}

    def __init__(self):
        self.zones: list[BaseZone] = []
        self.ships: list[BaseBattleship] = []

    def add_zone(self, zone_type: str, zone_code: str):
        try:
            new_zone = self.VALID_ZONES[zone_type](zone_code)

            if new_zone in self.zones:
                raise Exception("Zone already exists!")

            self.zones.append(new_zone)
            return f"A zone of type {zone_type} was successfully added."

        except KeyError:
            raise Exception("Invalid zone type!")

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        try:
            new_ship = self.VALID_SHIP_TYPE[ship_type](name, health, hit_strength)
            self.ships.append(new_ship)
            return f"A new {ship_type} was successfully added."

        except KeyError:
            raise Exception(f"{ship_type} is an invalid type of ship!")


    def add_ship_to_zone(self, zone: BaseZone, ship: BaseBattleship):
        pass

    def remove_battleship(self, ship_name: str):
        pass

    def start_battle(self, zone: BaseZone):
        pass

    def get_statistics(self):
        result = [f"Available Battleships: {len(self.ships)}"]

        available_ship_names = [s.name for s in self.ships]
        if available_ship_names:
            result.append(f"#{', '.join(available_ship_names)}#")

        result.append("***Zones Statistics:***")
        result.append(f"Total Zones: {self.zones}")

        sorted_zones_code_asc = sorted(self.zones, key=lambda z: z.code)

        for zone in sorted_zones_code_asc:
            result.append(zone.zone_info())



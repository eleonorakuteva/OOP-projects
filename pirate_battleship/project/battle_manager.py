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

    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):
        if zone.volume <= 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health == 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            # if ship in battle zone is_available = False
            return f"Ship {ship.name} is not available and could not participate!"

        #ship can participate:
        if zone.type != ship.type:
            ship.is_attacking = False

        elif zone.type == ship.type:
            ship.is_attacking = True

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."


    def remove_battleship(self, ship_name: str):
        ship = next((s for s in self.ships if s.name == ship_name), None)
        if ship is None:
            return "No ship with this name!"

        # check if the ship participates in a zone
        if not ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):

        if not zone:
            pass

        attacker_ships:list = [ship for ship in zone.ships if ship.is_attacking]
        target_ships: list = [ship for ship in zone.ships if not ship.is_attacking]

        if not attacker_ships or not target_ships:
            return f"Not enough participants. The battle is canceled."

        if attacker_ships and target_ships:

            max_hit_strength = 0
            attacker = None
            for ship in attacker_ships:
                if ship.hit_strength > max_hit_strength:
                    max_hit_strength = ship.hit_strength
                    attacker = ship

            max_health = 0
            target = None
            for ship in target_ships:
                if ship.health > max_health:
                    max_health = ship.health
                    target = ship

            attacker.attack()
            target.take_damage(attacker)

            if target.health == 0:
                zone.ships.remove(target)
                self.ships.remove(target)
                return f"{target.name} lost the battle and was sunk."

            if attacker.ammunition == 0:
                zone.ships.remove(attacker)
                self.ships.remove(attacker)
                return f"{attacker.name} ran out of ammunition and leaves."

            return "Both ships survived the battle."


    def get_statistics(self):
        available_manager_ships = [s for s in self.ships if s.is_available]

        result = [f"Available Battleships: {len(available_manager_ships)}"]

        available_ship_names = [s.name for s in available_manager_ships]

        if available_ship_names:
            result.append(f"#{', '.join(available_ship_names)}#")

        result.append("***Zones Statistics:***")
        result.append(f"Total Zones: {len(self.zones)}")

        sorted_zones_code_asc: list = sorted(self.zones, key=lambda z: z.code)

        for zone in sorted_zones_code_asc:
            string = zone.zone_info()
            result.append(string)

        return '\n'.join(result)


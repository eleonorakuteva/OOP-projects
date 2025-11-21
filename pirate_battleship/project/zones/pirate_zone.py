from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code=code, volume=self.INITIAL_VOLUME)

    def zone_info(self):
        result = ["@Pirate Zone Statistics@",
                  f"Code: {self.code}; Volume: {self.volume}"]

        royalships_count = sum(s for s in self.ships if type(self).__name__ == "RoyalBattleship")

        result.append(
            f"Battleships currently in the Pirate Zone: {len(self.ships)}, {royalships_count} out of them are Pirate Battleships.")

        if self.ships:
            result.append(f"#{', '.join(self.get_ships())}#")

        return "\n".join(result)

    @property
    def type(self):
        return "pirate"


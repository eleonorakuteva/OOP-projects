from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):

    INITIAL_VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code=code, volume=self.INITIAL_VOLUME)

    def zone_info(self):
        result = ["@Royal Zone Statistics@",
                  f"Code: {self.code}; Volume: {self.volume}"]

        pirateships_count = sum(s for s in self.ships if type(self).__name__ == "PirateBattleship")

        result.append(f"Battleships currently in the Royal Zone: {len(self.ships)}, {pirateships_count} out of them are Pirate Battleships.")

        if self.ships:
            result.append(f"#{', '.join(self.get_ships())}#")



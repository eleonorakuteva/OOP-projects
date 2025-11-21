from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    INITIAL_VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code=code, volume=self.INITIAL_VOLUME)

    def zone_info(self):
        result = ["@Pirate Zone Statistics@",
                  f"Code: {self.code}; Volume: {self.volume}"]

        royalships_count = len([s for s in self.ships if s.type == "royal"])

        result.append(
            f"Battleships currently in the Pirate Zone: {len(self.ships)}, {royalships_count} out of them are Royal Battleships.")

        if self.ships:
            list_with_sorted_ships = self.get_ships()
            result.append(f"#{', '.join(s.name for s in list_with_sorted_ships)}#")

        return "\n".join(result)

    @property
    def type(self):
        return "pirate"


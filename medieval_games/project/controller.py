from project.player import Player
from project.supply.supply import Supply


class Controller:

    VALID_TYPES_SUSTENANCE = ["Food", "Drink"]

    def __init__(self):
        self.players: list[Player] = []
        self.supplies: list[Supply] = []

    def add_player(self, *players: Player):

        successfully_added_players_name = []
        for player in players:
            if player not in self.players:
                successfully_added_players_name.append(player.name)
                self.players.append(player)
        return f"Successfully added: {', '.join(successfully_added_players_name)}"


    def add_supply(self, *supplies: Supply):

        # for supply in supplies:
        self.supplies.extend(supply for supply in supplies)


    def sustain(self, player_name: str, sustenance_type: str):
        curr_player = next((p for p in self.players if p.name == player_name), None)

        # If the player is not in the players list, ignore the command.
        if curr_player is None:
            pass

        # •	The valid sustenance types are "Food" and "Drink". In any other case, ignore the command.
        if sustenance_type not in self.VALID_TYPES_SUSTENANCE:
            pass

        list_curr_sustenance = [s for s in self.supplies if s.type == sustenance_type]

        if not list_curr_sustenance:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        # If the player doesn't need sustenance, it won't be appropriate to waste a supply
        if not curr_player.need_sustenance:
            return f"{player_name} have enough stamina."

        # Use the last supply added from the given type to sustain the player
        # (increase his stamina with the supply's energy value and remove the supply from the list)
        # and return the message "{player_name} sustained successfully with {supply_name}."
        # A player always uses the whole amount (units) of the given supply,
        # but his stamina cannot enhance above 100 (it should be set to 100).

        curr_sustenance = list_curr_sustenance.pop()
        gained_stamina = curr_sustenance.energy + curr_player.stamina
        curr_player.stamina = min(100, gained_stamina)
        return f"{player_name} sustained successfully with {curr_sustenance.name}."

    









    def duel(self, first_player_name: str, second_player_name: str):
        pass

    def next_day(self):
        pass

    def __str__(self) -> str:
        return "nothing"

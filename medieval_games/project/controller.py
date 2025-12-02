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
        self.supplies.extend(supplies)


    def sustain(self, player_name: str, sustenance_type: str):
        curr_player = next((p for p in self.players if p.name == player_name), None)

        # If the player is not in the players list, ignore the command.
        if curr_player is None:
            return None

        # The valid sustenance types are "Food" and "Drink". In any other case, ignore the command.
        if sustenance_type not in self.VALID_TYPES_SUSTENANCE:
            return None

        has_curr_sustenance = next((s for s in self.supplies if s.type == sustenance_type), None)

        if has_curr_sustenance is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        # If the player doesn't need sustenance, it won't be appropriate to waste a supply
        if not curr_player.need_sustenance:
            return f"{player_name} have enough stamina."

        # Use the last supply added from the given type to sustain the player
        # (increase his stamina with the supply's energy value and remove the supply from the list)
        # and return the message "{player_name} sustained successfully with {supply_name}."
        # A player always uses the whole amount (units) of the given supply,
        # but his stamina cannot enhance above 100 (it should be set to 100).

        last_sustenance = None
        for i in range(len(self.supplies) -1, 0, -1):
            if self.supplies[i].type == sustenance_type:
                last_sustenance = self.supplies.pop(i)
                break
        gained_stamina = last_sustenance.energy + curr_player.stamina
        curr_player.stamina = min(100, gained_stamina)
        return f"{player_name} sustained successfully with {last_sustenance.name}."



    def duel(self, first_player_name: str, second_player_name: str):
        """
        There will be no case where both players will have equal stamina values at the beginning or in the end.
        The players will always exist in the players list.
        """

        first_player = next((p for p in self.players if p.name == first_player_name), None)
        second_player = next((p for p in self.players if p.name == second_player_name), None)

        msg = self._if_players_can_participate_in_duel(first_player, second_player)
        if msg:
            return '\n'.join(msg)

        if first_player < second_player:
            return self._attack(first_player, second_player)
        else:
            return self._attack(second_player, first_player)


    # def next_day(self):
    #     for p in self.players:
    #         if p.stamina - (p.age * 2) < 0:
    #             p.stamina = 0
    #         else:
    #             p.stamina -= (p.age * 2)
    #     for p in self.players:
    #         self.sustain(p.name, "Food")
    #         self.sustain(p.name, "Drink")

    def next_day(self):
        for player in self.players:

            reduced_amount = player.stamina - (player.age * 2)
            player.stamina = max(0, reduced_amount)

            for sustenance_type in self.VALID_TYPES_SUSTENANCE:
                self.sustain(player.name, sustenance_type)


    def __str__(self) -> str:
        result = []

        for player in self.players:
            result.append(str(player))

        for supply in self.supplies:
            result.append(supply.details())

        return '\n'.join(result)

    @staticmethod
    def _if_players_can_participate_in_duel(player1, player2):
        result = []
        if player1.stamina == 0:
            result.append(f"Player {player1.name} does not have enough stamina.")
        if player2.stamina == 0:
            result.append(f"Player {player2.name} does not have enough stamina.")
        return result




    @staticmethod
    def _attack(attacker, take_damage):

        take_damage.stamina -= attacker.stamina / 2

        if attacker.stamina - (take_damage.stamina / 2) <= 0:
            attacker.stamina = 0

        else:
            attacker.stamina -= take_damage.stamina / 2

        if attacker < take_damage:
            return f"Winner: {take_damage.name}"
        else:
            return f"Winner: {attacker.name}"




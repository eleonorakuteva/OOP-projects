from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):

    INITIAL_AMMUNITION = 100
    AMMUNITION_PER_ATTACK = 25

    def __init__(self,name: str, health: int, hit_strength: int):
        super().__init__(name=name, health= health, hit_strength=hit_strength, ammunition=self.INITIAL_AMMUNITION)


    def attack(self):
        ammunition_after_attack = self.ammunition - self.AMMUNITION_PER_ATTACK
        self.ammunition = max(0, ammunition_after_attack)
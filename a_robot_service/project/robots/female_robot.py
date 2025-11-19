from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):

    WEIGHT = 7
    INCREASE_WEIGHT_PER_EATING = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, FemaleRobot.WEIGHT)

    def eating(self):
        self.weight += FemaleRobot.INCREASE_WEIGHT_PER_EATING
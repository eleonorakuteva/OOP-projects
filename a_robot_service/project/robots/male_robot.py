from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):

    WEIGHT = 9
    INCREASE_WEIGHT_PER_EATING = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, MaleRobot.WEIGHT)

    def eating(self):
        self.weight += MaleRobot.INCREASE_WEIGHT_PER_EATING
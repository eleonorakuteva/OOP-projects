from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    def __init__(self, name: str, speed: int):
        super().__init__(name=name, speed=speed)

    @property
    def max_speed(self):
        return 120 # km/h

    @property
    def increases_speed_by_train(self):
        return 2

    def train(self):
        self.speed += self.increases_speed_by_train


# a = Appaloosa("horse", 115)
# print(a.train())
# print(a.speed)
# print(a.train())
# print(a.speed)
# print(a.train())

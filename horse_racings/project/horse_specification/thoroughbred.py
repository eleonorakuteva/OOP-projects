from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    def __init__(self, name: str, speed: int):
        super().__init__(name=name, speed=speed)

    @property
    def max_speed(self):
        return 140  # km/h

    @property
    def increases_speed_by_train(self):
        return 3





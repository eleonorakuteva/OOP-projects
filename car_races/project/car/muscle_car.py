from project.car.car import Car


class MuscleCar(Car):

    def min_speed_limit(self):
        return 250

    def max_speed_limit(self):
        return 450
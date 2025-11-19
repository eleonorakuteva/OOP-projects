from project.robots.base_robot import BaseRobot
from project.services.base_service import BaseService


class RobotsManagingApp:

    def __init__(self):
        self.robots: list[BaseRobot] = []
        self.services: list[BaseService] = []

    def add_service(self, service_type: str, name: str):
        pass

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        pass

    def add_robot_to_service(self, robot_name: str, service_name: str):
        pass

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        pass

    def feed_all_robots_from_service(self, service_name: str):
        pass

    def service_price(self, service_name: str):
        pass

    def __str__(self):
        pass

main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))

print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))



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
        result = []
        for service in self.services:
            result.append(str(service))

        return '\n'.join(result)





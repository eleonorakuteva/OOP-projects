from project.robots.base_robot import BaseRobot
from project.services.base_service import BaseService
from project.services.secondary_service import SecondaryService
from project.services.main_service import MainService
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot



class RobotsManagingApp:

    VALID_SERVICES = {"SecondaryService": SecondaryService,
                      "MainService": MainService,
                      }

    VALID_ROBOTS = {"MaleRobot": MaleRobot,
                    "FemaleRobot": FemaleRobot,
                    }

    def __init__(self):
        self.robots: list[BaseRobot] = []
        self.services: list[BaseService] = []

    def add_service(self, service_type: str, name: str) -> str:
        try:
            new_service = self.VALID_SERVICES[service_type](name)
            self.services.append(new_service)
            return f"{service_type} is successfully added."
        except KeyError:
            return "Invalid service type!"

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        try:
            new_robot = self.VALID_ROBOTS[robot_type](name, kind, price)
            self.robots.append(new_robot)
            return f"{robot_type} is successfully added."
        except KeyError:
            return "Invalid robot type!"

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_object_by_name(robot_name, self.robots)
        service: BaseService = self.find_object_by_name(service_name, self.services)

        if not self.check_suitable_services(robot, service):
            return "Unsuitable service."

        if not self.server_has_capacity(service):
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."


    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service: BaseService = self.find_object_by_name(service_name, self.services)
        robot: BaseRobot = self.find_object_by_name(robot_name, service.robots)

        if robot is None:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."


    def feed_all_robots_from_service(self, service_name: str):
        service: BaseService = self.find_object_by_name(service_name, self.services)

        count_robots_in_service = len(service.robots)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {count_robots_in_service}."


    def service_price(self, service_name: str):
        service: BaseService = self.find_object_by_name(service_name, self.services)

        total_price = sum(robot.price for robot in service.robots)
        return f"The value of service {service_name} is {total_price:.2f}."


    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())

        return '\n'.join(result)

    @staticmethod
    def find_object_by_name(name, collection):
        object_ = next((o for o in collection if o.name == name), None)
        return object_


    @staticmethod
    def check_suitable_services(robot_object, service_object):
        if isinstance(robot_object, FemaleRobot) and isinstance(service_object, SecondaryService):
            return True
        elif isinstance(robot_object, MaleRobot) and isinstance(service_object, MainService):
            return True
        return False


    @staticmethod
    def server_has_capacity(service_object: BaseService):
        if len(service_object.robots) < service_object.capacity:
            return True
        return False





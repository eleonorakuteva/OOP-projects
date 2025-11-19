from project.services.base_service import BaseService


class MainService(BaseService):

    CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, MainService.CAPACITY)

    def details(self) -> str:
        result = [f"{self.name} Main Service:"]
        if self.robots:
            all_robots = [robot.name for robot in self.robots]
            result.append(f"Robots: {' '. join(all_robots)}")
        else:
            result.append("Robots: none")
        return '\n'.join(result)

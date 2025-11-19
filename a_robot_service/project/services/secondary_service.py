from project.services.base_service import BaseService


class SecondaryService(BaseService):

    CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, SecondaryService.CAPACITY)

    def details(self) -> str:
        result = [f"{self.name} Secondary Service:"]
        if self.robots:
            all_robots = [robot.name for robot in self.robots]
            result.append(f"Robots: {' '. join(all_robots)}")
        else:
            result.append("Robots: none")
        return '\n'.join(result)
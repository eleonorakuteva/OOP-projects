from project.services.base_service import BaseService


class SecondaryService(BaseService):

    CAPACITY = 15

    def __init__(self, name):
        super().__init__(name, SecondaryService.CAPACITY)

    def details(self) -> str:
        robots = " ".join([r.name for r in self.robots]) if self.robots else "none"
        return f"{self.name} Secondary Service:\nRobots: {robots}"

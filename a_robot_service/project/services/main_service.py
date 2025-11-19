from project.services.base_service import BaseService


class MainService(BaseService):

    CAPACITY = 30

    def __init__(self, name):
        super().__init__(name, MainService.CAPACITY)

    @property
    def service_type(self) -> str:
        return "Main"

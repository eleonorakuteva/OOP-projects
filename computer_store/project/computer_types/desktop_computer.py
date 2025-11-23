from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer= manufacturer, model=model)


    @property
    def max_ram(self) -> int:
        return 128 #GB

    @property
    def valid_processors(self) -> dict[str: int]:
        return {"AMD Ryzen 7 5700G": 500,
                "Intel Core i5-12600K": 600,
                "Apple M1 Max": 1800}

    @property
    def type_computer(self):
        return "desktop computer"

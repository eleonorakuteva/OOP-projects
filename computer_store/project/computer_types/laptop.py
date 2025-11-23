from project.computer_types.computer import Computer


class Laptop(Computer):

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer=manufacturer, model=model)

    @property
    def max_ram(self):
        return 64

    @property
    def valid_processors(self) -> dict[str: int]:
        return {"AMD Ryzen 9 5950X": 900,
                "Intel Core i9-11900H": 1_050,
                "Apple M1 Pro": 1_200}

    @property
    def type_computer(self):
        return "laptop"
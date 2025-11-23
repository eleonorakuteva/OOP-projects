from project.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS = {"AMD Ryzen 9 5950X": 900,
                  "Intel Core i9-11900H": 1_050,
                  "Apple M1 Pro": 1_200}

    MAX_RAM = 64  # GB

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer=manufacturer, model=model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")

        if self.MAX_RAM:
            pass

        else:
            pass
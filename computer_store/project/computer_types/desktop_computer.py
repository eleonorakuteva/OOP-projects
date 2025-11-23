from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    PROCESSORS = {"AMD Ryzen 7 5700G": 500,
                  "Intel Core i5-12600K": 600,
                  "Apple M1 Max": 1800}

    MAX_RAM = 128 #GB

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer= manufacturer, model=model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.PROCESSORS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if self.MAX_RAM:
            pass

        else:
            pass

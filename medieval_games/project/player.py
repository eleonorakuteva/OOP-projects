

class Player:

    NEEDED_AGE = 12
    ALL_PLAYER_NAMES: list[str] = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.need_sustenance: bool = self._need_sustenance

    @property
    def _need_sustenance(self):
        if self.__stamina == 100:
            return False
        return True


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name not valid!")

        if value in self.ALL_PLAYER_NAMES:
            raise Exception(f"Name {value} is already used!")

        self.ALL_PLAYER_NAMES.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < self.NEEDED_AGE:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        if self.__stamina > 100 or self.__stamina < 0:
            raise ValueError("Stamina not valid!")
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value > 100 or value < 0:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"


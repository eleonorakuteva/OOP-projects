class Waiter:
    def __init__(self, name:str, id_:int):
        self.name = name
        self.id = id_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The waiter name cannot be an empty string")
        self.__name = value


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value.isdigit() and len(value) == 8:
            self.__id = value
        else:
            raise ValueError("The id must contain 8 digits.")


class Waiter:
    def __init__(self, name:str, id_:int):
        self.name = name
        self.id = id_


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if value.isdigit() and len(value) == 10:
            self.__id = value

class Pet:
    def __init__(self, name:str, species:str, age:int):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

    def pet_dict(self):
        return {self.species : {"name" : self.name,
                                "age" : self.age,}
                }

    def search_by_species(self, species_key):
        matches = [value for species, value in self.pet_dict() if species == species_key]
        return matches

    def __repr__(self):
        return f"{self.name}, the {self.species}, age {self.age}."
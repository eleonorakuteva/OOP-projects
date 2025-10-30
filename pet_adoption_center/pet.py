


class Pet:
    all_pets:dict[str,{str, bool|int|str}] = {}

    def __init__(self, name:str, species:str, age:int):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

        # Add this pet to the shared class-level dictionary
        Pet.all_pets.setdefault(species, []).append({
            "name": name,
            "age": age,
            "is_adopted": self.is_adopted
        })


    def __repr__(self):
        return f"{self.name}, the {self.species}, age {self.age}."
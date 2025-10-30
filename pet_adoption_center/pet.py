def get_all_registered_pets() -> str:
    all_pets = [f"({species}) {animal["name"]} - age: {animal["age"]}" for species, pet_info in Pet.all_pets.items()  for animal in pet_info]
    return '\n'.join(all_pets)


class Pet:
    all_pets:dict[str,{str, bool|int|str}] = {}

    def __init__(self, name:str, species:str, age:int):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted:bool = False

        # Add this pet to the shared class-level dictionary
        Pet.all_pets.setdefault(species, []).append({
            "name": name,
            "age": age,
            "is_adopted": self.is_adopted
        })


    def __repr__(self) -> str:
        return f"{self.name}, the {self.species}, age {self.age}"


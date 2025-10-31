class Pet:
    all_pets: dict[str, list[dict[str, bool|int|str]]] = {}


    def __init__(self, name:str, species:str, age:int) -> None:
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted:bool = False
        self.is_in_adoption_center = False

        # Add this pet to the shared class-level dictionary
        Pet.all_pets.setdefault(species, []).append({
            "name": name,
            "age": age,
            "is_adopted": self.is_adopted
        })


    def __str__(self) -> str:
        return f"{self.name}, the {self.species.lower()}, age {self.age}"

    @classmethod
    def get_all_registered_pets(cls) -> str:
        all_pets = [
            f"({species}) {animal['name']} - age: {animal['age']}"
            for species, pet_info in cls.all_pets.items()
            for animal in pet_info
        ]
        return '\n'.join(all_pets)


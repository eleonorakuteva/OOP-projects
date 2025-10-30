from pet import Pet

class AdoptionCenter:

    def __init__(self, name:str, list_of_pets:list = None):
        self.name = name
        self.list_of_pets:list[Pet] = list_of_pets if list_of_pets is not None else []

    def __repr__(self):
        return (f"{self.name} is a adoption center, where you can adopt your future pet!\n"
                f"{self.list_available_pets()} ")

    def list_available_pets(self):
        available_pets = [f"{pet}" for pet in self.list_of_pets]
        return (f"Available pets you can adopt:\n-> "
                f"{"\n-> ".join(available_pets)}")


    def search_by_species(self, species_key):
        pets_with_curr_species = [f"{pet.name} - {pet.age} years old." for pet in self.list_of_pets if pet.species == species_key]
        if pets_with_curr_species:
            return f"In adoption center {self.name} we have {len(pets_with_curr_species)} animals with species: {species_key}."+ '\n -> ' +'\n -> '.join(pets_with_curr_species)
        return f"In adoption center {self.name} currently we don't have animals with species: {species_key}."


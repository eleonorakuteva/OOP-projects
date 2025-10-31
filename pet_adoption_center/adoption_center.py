from pet import Pet

class AdoptionCenter:

    def __init__(self, name:str, list_of_pets:list = None) -> None:
        self.name = name
        self.list_of_pets:list[Pet] = list_of_pets if list_of_pets is not None else []

    def __str__(self):
        return (f"{self.name} is an adoption center, where you can adopt your future pet!\n"
                f"{self.list_available_pets()} ")

    def list_available_pets(self):
        available_pets = [f"{pet}" for pet in self.list_of_pets]
        if available_pets:
            return (f"Available pets you can adopt in {self.name}:\n-> "
                    f"{'\n-> '.join(available_pets)}")
        else:
            return f"Currently Adoption center - {self.name} does not have animals to adopt."


    def search_by_species(self, species_key:str) -> str:
        pets_with_curr_species = [f"{pet.name} - {pet.age} years old."
                                  for pet in self.list_of_pets if pet.species.lower() == species_key.lower()]
        if pets_with_curr_species:
            return f"In adoption center {self.name} we have {len(pets_with_curr_species)} animals with species: {species_key.title()}."+ '\n -> ' +'\n -> '.join(pets_with_curr_species)
        return f"In adoption center {self.name} currently we don't have animals with species: {species_key.title()}."


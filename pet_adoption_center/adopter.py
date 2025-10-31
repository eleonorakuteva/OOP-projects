from pet import Pet
from adoption_center import AdoptionCenter

class Adopter:
    def __init__(self, name:str, adopted_pets_by_user:Pet = None) -> None:
        self.name = name
        self.adopted_pets_by_user: list[Pet] = adopted_pets_by_user if adopted_pets_by_user is not None else []

    def adopt_pet(self, pet:Pet, center:AdoptionCenter) -> str:
        if pet in center.list_of_pets:
            self.adopted_pets_by_user.append(pet)
            center.list_of_pets.remove(pet)
            pet.is_adopted = True
            pet.is_in_adoption_center = False
            return f"{self.name} ({type(self).__name__}) successfully adopted {pet}"
        return (f"The {pet.species.lower()} {pet.name.title()} is NOT in Adoption center - {center.name}.\n"
                  f"{self.name} ({type(self).__name__}) can NOT adopt it from there.")

    def return_pet(self, pet:Pet, center:AdoptionCenter) -> str:
        if pet in self.adopted_pets_by_user:
            pet.is_in_adoption_center = True
            pet.is_adopted = False
            center.list_of_pets.append(pet)
            self.adopted_pets_by_user.remove(pet)
            return f"{self.name} ({type(self).__name__}) successfully returned {pet} to adoption center - {center.name.title()}."
        else:
            return f"{self.name} ({type(self).__name__}) can not return pet, that don't own."


    def user_adopted_pets(self) -> str:
        if self.adopted_pets_by_user:
            adopted_pets = [f"{pet}" for pet in self.adopted_pets_by_user]
            return f"{self.name} ({type(self).__name__}) adopted the following animals:\n -> {"\n -> ".join(adopted_pets)}"
        else:
            return f"{self.name} ({type(self).__name__}) has no adopted pet yet."


    def __str__(self) -> str:
        return (f"{type(self).__name__} name: {self.name}.\n"
                f"{self.user_adopted_pets()}")
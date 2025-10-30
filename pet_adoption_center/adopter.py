class Adopter:
    def __init__(self, name:str, adopted_pets_by_user = None):
        self.name = name
        self.adopted_pets_by_user = adopted_pets_by_user if adopted_pets_by_user is not None else []

    def adopt_pet(self, pet, center):
        if pet in center.list_of_pets:
            self.adopted_pets_by_user.append(pet)
            center.list_of_pets.remove(pet)
            print(f"You successfully adopted {pet}")
        else:
            print(f"The {pet.species.lower()} {pet.name.title()} is NOT in Adoption center - {center.name}.\n"
                  f"You can NOT adopt it from there.")

    def return_pet(self, pet, center):
        if pet in self.adopted_pets_by_user:
            center.list_of_pets.append(pet)
            self.adopted_pets_by_user.remove(pet)
            print(f"You successfully returned {pet} to adoption center - {center.name.title()}.")
        else:
            print(f"You can not return pet, that you don't own.")

    def user_adopted_pets(self):
        if len(self.adopted_pets_by_user) >= 1:
            adopted_pets = [f"{pet}" for pet in self.adopted_pets_by_user]
            return f"The adopter {self.name} adopted the following animals:\n-> {"\n-> ".join(adopted_pets)}"
        else:
            return f"{adopter1.name.title()} has no adopted pet yet."


    def __repr__(self):
        return (f"Adopter name: {self.name}.\n"
                f"{self.user_adopted_pets()}")
"""
Project name: Pet Adoption Center Management System

System for a pet adoption center that manages pets, adopters, and staff members.
The center keeps track of available pets, and adopters can adopt or return pets.
Staff (workers) can add or remove pets from the center.
"""




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
        matches = {species_key for species_key, value in self.pet_dict()}
        return matches

    def __repr__(self):
        return f"{self.name}, the {self.species}, age {self.age}."

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

class Worker(Adopter):

    def __init__(self, name:str, worker_id:str, adopted_pets_by_user = None):
        super().__init__(name, adopted_pets_by_user)
        self._worker_id = worker_id

    def is_id_valid(self):
        return len(self._worker_id) == 8 and self._worker_id.isdigit()

    def add_pet(self, pet, center):
        if self.is_id_valid():
            center.list_of_pets.append(pet)

    def remove_pet(self, pet, center):
        if self.is_id_valid():
            if pet in center.list_of_pets:
                return center.list_of_pets.remove(pet)
            else:
                print(f"The {pet.species.lower()} {pet.name.title()} is NOT in Adoption center - {center.name}.\n"
                      f"Worker can not remove it from adoption center.")

    def __repr__(self):
        return (f"Worker name: {self.name}.\n"
                f"Worker Id: {self._worker_id}, valid = {self.is_id_valid()}.")


if __name__ == "__main__":
    center1 = AdoptionCenter("SunnyPaws")


    pet1 = Pet("Bella", "Dog", 3)
    pet2 = Pet("Luna", "Cat", 1)
    pet3 = Pet("Max", "Dog", 2)


    worker = Worker("James", "10001023")

    worker.add_pet(pet1, center1)
    worker.add_pet(pet2, center1)
    print(center1.list_available_pets())

    adopter1 = Adopter("Ciara")
    adopter1.adopt_pet(pet1, center1)
    adopter1.adopt_pet(pet3,center1)
    adopter1.return_pet(pet1, center1)
    # adopter1.adopt_pet(pet2,center1)
    print(adopter1.user_adopted_pets())
    adopter1.return_pet(pet3,center1)
    adopter1.adopt_pet(pet1,center1)

    print(adopter1)




    # print(center1.list_available_pets())
    # adopter1.adopt_pet(pet1, center1)
    # print(worker)
    # print(adopter1)


    # adopter1 = Adopter("Maria", None)
    # worker.add_pet(pet1, adoption_center)
    # worker.add_pet(pet2, adoption_center)
    #
    # adoption_center.list_available_pets()
    #
    # adopter.adopt_pet(pet1, adoption_center)
    # adoption_center.list_available_pets()
    #
    # # adopter.return_pet(pet1, adoption_center)
    # # adoption_center.list_available_pets()

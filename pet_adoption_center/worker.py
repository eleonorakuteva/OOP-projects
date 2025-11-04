from adopter import Adopter
from pet import Pet
from adoption_center import AdoptionCenter

class Worker(Adopter):

    def __init__(self, name:str, worker_id:str, adopted_pets_by_user = None) -> None:
        super().__init__(name, adopted_pets_by_user)
        self.worker_id = worker_id

    @property
    def worker_id(self):
        return self.__worker_id

    @worker_id.setter
    def worker_id(self, value):
        if len(value) == 8 and value.isdigit():
            self.__worker_id = value

    def is_id_valid(self) -> bool:
        return len(self.__worker_id) == 8 and self.__worker_id.isdigit()

    def add_pet(self, pet:Pet, center:AdoptionCenter) -> None:
        if self.is_id_valid() and not pet.is_in_adoption_center:
            pet.is_in_adoption_center = True
            center.list_of_pets.append(pet)

    def remove_pet(self, pet:Pet, center:AdoptionCenter) -> str:
        if self.is_id_valid():
            if pet in center.list_of_pets:
                center.list_of_pets.remove(pet)
                pet.is_in_adoption_center = False
                return f"{pet} is successfully removed from Adoption center - {center.name}"
            return (f"The {pet.species.lower()} {pet.name.title()} is NOT in Adoption center - {center.name}.\n"
                      f"Worker can not remove it from adoption center.")
        return f"Worker does not have valid id."


    def __str__(self) -> str:
        return (f"Worker name: {self.name}.\n"
                f"Worker Id: {self.__worker_id}, valid = {self.is_id_valid()}.")


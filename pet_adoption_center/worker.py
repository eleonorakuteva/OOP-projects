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
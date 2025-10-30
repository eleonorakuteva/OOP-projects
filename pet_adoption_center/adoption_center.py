from pet import Pet

class AdoptionCenter:

    def __init__(self, name:str, list_of_pets:list = None):
        self.name = name
        self.list_of_pets:list [Pet] = list_of_pets if list_of_pets is not None else []

    def __repr__(self):
        return (f"{self.name} is a adoption center, where you can adopt your future pet!\n"
                f"{self.list_available_pets()} ")

    def list_available_pets(self):

        available_pets = [f"{pet}" for pet in self.list_of_pets]

        return (f"Available pets you can adopt:\n-> "
                f"{"\n-> ".join(available_pets)}")
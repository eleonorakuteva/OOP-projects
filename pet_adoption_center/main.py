from adoption_center import AdoptionCenter
from pet import Pet


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

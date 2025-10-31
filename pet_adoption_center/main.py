from pet import Pet
from adoption_center import AdoptionCenter
from adopter import Adopter
from worker import Worker


def main():
    print("=== 🐾 Welcome to the Pet Adoption Center Simulation! ===\n")

    # --- 1. Create Pets ---
    luna = Pet("Luna", "Cat", 3)
    maxy = Pet("Maxy", "Dog", 5)
    bella = Pet("Bella", "Rabbit", 2)
    charlie = Pet("Charlie", "Dog", 4)

    print("All registered pets so far:")
    print(Pet.get_all_registered_pets())
    print("\n")

    # --- 2. Create Adoption Center ---
    center = AdoptionCenter("Happy Tails", [luna, maxy])
    print(center)
    print("\n")

    # --- 3. Search pets by species ---
    print(center.search_by_species("dog"))
    print("\n")

    # --- 4. Create Adopter ---
    john = Adopter("John")
    print(john.user_adopted_pets())
    print("\n")

    # --- 5. John adopts a pet ---
    print(john.adopt_pet(maxy, center))
    print(john.user_adopted_pets())
    print("\n")

    # --- 6. John tries to adopt a pet not in the center ---
    print(john.adopt_pet(bella, center))
    print("\n")

    # --- 7. John returns a pet ---
    print(john.return_pet(maxy, center))
    print(center.list_available_pets())
    print("\n")

    # --- 8. Create Worker ---
    emma = Worker("Emma", "12345678")
    print(emma)
    print("\n")

    # --- 9. Worker adds a new pet to the center ---
    emma.add_pet(bella, center)
    print(center.list_available_pets())
    print("\n")

    # --- 10. Worker removes a pet ---
    print(emma.remove_pet(luna, center))
    print(center.list_available_pets())
    print("\n")

    print("=== ✅ End of Simulation ===")


if __name__ == "__main__":
    main()

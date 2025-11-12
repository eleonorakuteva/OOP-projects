
# 🐾 Project name: Pet Adoption Center Management System

A simple Object-Oriented Programming (OOP) project built in Python that simulates the management of a pet adoption center.
It demonstrates classes, inheritance, encapsulation, and class-level data management.

---

### 📘 Overview

The project models the real-world relationships between:
- **Pets** — Animals available for adoption.
- **Adoption Centers** — Places where pets can be added, listed, and adopted.
- **Adopters** — People who adopt or return pets.
- **Workers** — Special users who can manage animals in the center.

---

## 🧱 Project Structure

pet_adoption_center (project)/  
│   
├── pet.py   
├── adoption_center.py   
├── adopter.py   
├── worker.py   
├── main.py - for testing   
└── README.md   

---

## 🐶 Classes Overview

### `Pet`
Represents an individual pet.

**Attributes:**
- `name` (str)
- `species` (str)
- `age` (int)
- `is_adopted` (bool)
- `is_in_adoption_center` (bool)
- `Pet.all_pets` (class-level dict of all registered pets)

---

### `AdoptionCenter`
Represents a pet adoption center.

**Key Methods:**
- `list_available_pets()` — Shows available pets.
- `search_by_species(species_key)` — Lists pets by species.

---

### `Adopter`
Represents a user who can adopt or return pets.

**Key Methods:**
- `adopt_pet(pet, center)`
- `return_pet(pet, center)`
- `user_adopted_pets()`

---

### `Worker (inherits from Adopter)`
Represents a worker who can manage pets in the adoption center.

**Key Methods:**
- `is_id_valid()`
- `add_pet(pet, center)`
- `remove_pet(pet, center)`

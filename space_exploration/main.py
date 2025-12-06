from project.space_agency import SpaceAgency

# Create an instance of the Space Agency Manager
manager = SpaceAgency()

# Add astronauts (engineers & scientists)
print(manager.add_astronaut("EngineerAstronaut", "02345", 780_000.0))
print(manager.add_astronaut("EngineerAstronaut", "1234", 500_000.0))
print(manager.add_astronaut("EngineerAstronaut", "789123", 800_000.0))
print(manager.add_astronaut("EngineerAstronaut", "45678999", 702_000.0))
print(manager.add_astronaut("ScientistAstronaut", "321654", 401_000.0))
print(manager.add_astronaut("ScientistAstronaut", "6543211", 490_000.0))
print(manager.add_astronaut("ScientistAstronaut", "334654", 600_000.0))
print(manager.add_astronaut("ScientistAstronaut", "034654", 395_000.0))
print()

# Add stations
print(manager.add_station("MaintenanceStation", "Lunar-Base"))
print(manager.add_station("ResearchStation", "ISS-3"))
print(manager.add_station("ResearchStation", "Mars-Habitat"))
print()

# Assign astronauts to stations
print(manager.assign_astronaut("Lunar-Base", "EngineerAstronaut"))
print(manager.assign_astronaut("Lunar-Base", "EngineerAstronaut"))
print(manager.assign_astronaut("Lunar-Base", "ScientistAstronaut"))
print(manager.assign_astronaut("ISS-3", "ScientistAstronaut"))
print(manager.assign_astronaut("ISS-3", "ScientistAstronaut"))
print(manager.assign_astronaut("ISS-3", "EngineerAstronaut"))
print(manager.assign_astronaut("ISS-3", "EngineerAstronaut"))
print()

# Conduct training sessions
print(manager.train_astronauts(manager.stations[0], 0))
print(manager.train_astronauts(manager.stations[0], 1))
print(manager.train_astronauts(manager.stations[0], 2))
print(manager.train_astronauts(manager.stations[0], 3))
print(manager.train_astronauts(manager.stations[0], 3))
print(manager.train_astronauts(manager.stations[1], 0))
print(manager.train_astronauts(manager.stations[2], 1))
print()

# Retire an astronaut
print(manager.retire_astronaut(manager.stations[2], "334654"))
print(manager.retire_astronaut(manager.stations[0], "02345"))
print(manager.stations[0].astronauts[0].id_number, manager.stations[0].astronauts[0].stamina)
print(manager.retire_astronaut(manager.stations[0], "111111"))
print(manager.retire_astronaut(manager.stations[1], "45678999"))
print()

# Perform an agency-wide update
print(manager.agency_update(500_000.0))
print()

# Check astronaut salaries after the update
print(manager.stations[0].astronauts[0].salary)
print(manager.stations[0].astronauts[1].salary)
print(manager.stations[0].astronauts[2].salary)
print()
print(manager.stations[1].astronauts[0].salary)
print(manager.stations[1].astronauts[1].salary)
print(manager.stations[1].astronauts[2].salary)
print()
print(manager.astronauts[0].salary)

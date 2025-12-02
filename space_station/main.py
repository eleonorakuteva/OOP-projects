from project.space_station import SpaceStation

space = SpaceStation()
# add astronaut
print(space.add_astronaut("Geodesist", "name"))
print(space.add_astronaut("Geodesist", "name_test"))
print(space.add_astronaut("Meteorologist", "name"))
print(space.add_astronaut("Meteorologist", "name_2"))
print(space.add_astronaut("Geodesist", "name_3"))
print(space.add_astronaut("Biologist", "name_4"))
# print(space.add_astronaut("Biologist", "name_5"))
# print(space.add_astronaut("Biologist", "name_6"))
print([a.name for a in space.astronaut_repository.astronauts])


# retire astonaut
# print(space.retire_astronaut("invalid"))
print(space.retire_astronaut("name_test"))
print([a.name for a in space.astronaut_repository.astronauts])


# add planet
print(space.add_planet("planet", "a, b, c, d, e, f, g, h, i ,j ,k ,l, m, n, o, p, q, r"))
print(space.add_planet("planet_test", "e"))
print([p.items for p in space.planet_repository.planets])

# recharge_oxygen
print([a.oxygen for a in space.astronaut_repository.astronauts])
print(space.recharge_oxygen())
print([a.oxygen for a in space.astronaut_repository.astronauts])

# send_on_mission
# print(space.send_on_mission("invalid_name"))
print(space.send_on_mission("planet"))

print(space.report())

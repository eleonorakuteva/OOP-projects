

# Create an instance of FlowerShopManager
manager = FlowerShopManager()

# Add plants
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Rose", 15.50, 200, "Spring"))
print(manager.add_plant("Flower", "Tulip", 12.00, 150, "Spring"))
print(manager.add_plant("Flower", "Tulip", 12.00, 150, "Spring"))
print(manager.add_plant("Flower", "Lily", 20.00, 180, "Summer"))
print(manager.add_plant("LeafPlant", "Cactus", 8.00, 50, "M"))
print(manager.add_plant("LeafPlant", "Cactus", 8.00, 50, "M"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Fern", 6.50, 100, "S"))
print(manager.add_plant("LeafPlant", "Snake Plant", 12.00, 200, "L"))
print(manager.add_plant("LeafPlant", "Snake Plant", 12.00, 200, "L"))
print()

# Add clients
print(manager.add_client("RegularClient", "Alice Johnson", "1234567890"))
print(manager.add_client("RegularClient", "Bob Smith", "0987654321"))
print(manager.add_client("BusinessClient", "Greenhouse Inc.", "5647382910"))
print(manager.add_client("BusinessClient", "CoolGarden Plc.", "9647382910"))
print(manager.add_client("RegularClient", "Peter Johnson", "382910"))
print()

# Perform sales
print(manager.sell_plants("1234567890", "Rose", 3))
print(manager.sell_plants("0987654321", "Tulip", 2))
print(manager.sell_plants("5647382910", "Cactus", 1))
print()

# Get shop report
print(manager.shop_report())
print()

# Perform sales
print(manager.sell_plants("1234567890", "Lily", 2))
print(manager.sell_plants("0987654321", "Fern", 1))
print(manager.sell_plants("5647382910", "Snake Plant", 2))
print()

# Remove a plant
print(manager.remove_plant("Nonexistent"))
print(manager.remove_plant("Cactus"))
print()

# Get shop report
print(manager.shop_report())
print()

# Remove clients who have no orders
print(manager.remove_clients())
print(manager.remove_clients())

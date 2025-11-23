from project.computer_store_app import ComputerStoreApp


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))


# Output
# Created Apple Macbook with Apple M1 Pro and 64GB RAM for 1800$.
# Apple Macbook with Apple M1 Pro and 64GB RAM sold for 10000$.

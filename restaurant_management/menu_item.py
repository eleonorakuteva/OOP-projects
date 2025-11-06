class MenuItem:
    """
    Represents a single item (e.g., Pizza, Coke, Tiramisu).
    Stores name, category, price.
    """
    categories_list = ["Starter", "Main", "Dessert", "Drink"]

    def __init__(self, name:str, category:str, price:float):
        self.name = name
        self.category = category
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The item name cannot be an empty string")
        self.__name = value


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        if value not in MenuItem.categories_list:
            raise ValueError('The category must be between these options ["Starter", "Main", "Dessert", "Drink"]')
        self.__category = value


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0.0:
            raise ValueError("The price cannot be zero or less than zero.")
        self.__price = value
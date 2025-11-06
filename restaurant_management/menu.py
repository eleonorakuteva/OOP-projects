from menu_item import MenuItem


class Menu:
    """
    Contains a collection dict of MenuItem objects.
    Adds and removes items.
    Displays the full restaurant menu grouped by category.
    """
    def __init__(self) -> None:
        self.menu :dict[MenuItem.category: str, dict[MenuItem.name: str, MenuItem.price: float]] = {}


    def display_menu(self):
        result = [f"{7 * '='} MENU {7 * '='}".center(40)]
        for category, item_dict in self.menu.items():
            result.append(f"{5 * '='} {category} {5 * '='}".center(40))
            for dish_, price in item_dict.items():
                result.append(f"{dish_} : {price:.2f}".center(40))

        return '\n'.join(result)

    def add_dish(self, dish: MenuItem):
        if dish.category not in self.menu.keys():
            self.menu[dish.category] = {}

        if dish.name in self.menu[dish.category].items():
            return f"{dish.name.title()} is already in the menu!"

        self.menu[dish.category][dish.name] = dish.price
        return f"{dish.name.title()} is successfully added to the menu!"

    def remove_dish(self, dish: MenuItem):
        try:
            del self.menu[dish.category][dish.name]
            if len(self.menu[dish.category]) == 0:
                del self.menu[dish.category]
            return "The dish is successfully removed from the menu."
        except KeyError:
            return "The dish is not in the menu. So it cannot be removed."


cake = MenuItem("cake", "Dessert", 9.99)
pizza = MenuItem("Margaritta", "Main", 19.99)
menu = Menu()
print(menu.add_dish(cake))
print(menu.add_dish(pizza))
print(menu.display_menu())
print(menu.remove_dish(pizza))
print(menu.display_menu())


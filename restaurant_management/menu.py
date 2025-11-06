from menu_item import MenuItem


class Menu:
    """
    Contains a collection dict of MenuItem objects.
    Adds, removes, and retrieves items.
    Displays the full restaurant menu grouped by category.
    """
    def __init__(self) -> None:
        self.menu :dict[MenuItem.category: str, dict[MenuItem.name: str, MenuItem.price: float]] = {}


    def display_menu(self):
        result = []
        for category, item_dict in self.menu.items():
            result.append(f"{5 * '='} {category} {5 * '='}")
            for dish, price in item_dict.items():
                result.append(f"    -> {dish} : {price:.2f}")

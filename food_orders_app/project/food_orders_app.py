from project.client import Client
from project.meals.meal import Meal
from project.meals.starter import Starter
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish


class Another:

    def __init__(self, name, price):
        self.name = name
        self.price = price



class FoodOrdersApp:

    MINIMUM_MEALS_IN_MENU = 5

    def __init__(self):
        self.menu: list[Meal] = []
        self.clients_list: list[Client] = []

    def register_client(self, client_phone_number: str):
        client_in_clients_list = next((c for c in self.clients_list if c.phone_number == client_phone_number),None)

        if client_in_clients_list:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."


    def add_meals_to_menu(self, *meals: Meal):
        # there always be given meals with different names
        for meal in meals:
            if isinstance(meal, Meal):
                self.menu.append(meal)
        # print([p.name for p in self.menu])

    def show_menu(self):
        if len(self.menu) < self.MINIMUM_MEALS_IN_MENU:
            raise Exception("The menu is not ready!")

        result = [meal.details() for meal in self.menu]
        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        curr_client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)

        if curr_client is None:
            new_client = Client(client_phone_number)
            self.clients_list.append(new_client)



"""
from project.food_orders_app import FoodOrdersApp
from project.meals.starter import Starter
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish

"""

food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
another = Another("another", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
french_toast,
    hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))


print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
# additional_food = {"Risotto with Wild Mushrooms": 2,
#                    "Tortilla with Beef and Pork": 2}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
# print(food_orders_app.finish_order("0899999999"))
# print(food_orders_app)







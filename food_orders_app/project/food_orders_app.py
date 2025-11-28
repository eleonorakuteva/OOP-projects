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
    VALID_MEAL_TYPES = {
        "Starter": Starter,
        "MainDish": MainDish,
        "Dessert": Dessert
    }

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
        self._is_menu_ready()

        result = [meal.details() for meal in self.menu]
        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):

        self._is_menu_ready()

        curr_client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)

        if curr_client is None:
            new_client = Client(client_phone_number)
            self.clients_list.append(new_client)
            curr_client = new_client

        client_order: list[list] = []
        order_successful = True

        for meal_name, order_quantity in meal_names_and_quantities.items():

            names_match = [meal for meal in self.menu if meal_name == meal.name]

            if not names_match:
                order_successful = False
                raise Exception(f"{meal_name} is not on the menu!")

            meal_type = names_match[0].__class__.__name__
            quantity_match = next((meal for meal in names_match if order_quantity <= meal.quantity), None)


            if quantity_match is None:
                order_successful = False

                raise Exception(f"Not enough quantity of {meal_type}: {meal_name}!")

            client_meal = self.VALID_MEAL_TYPES[meal_type](meal_name, quantity_match.price, order_quantity)

            # remove_order_quantity_from_the_menu
            quantity_match.quantity -= order_quantity

            client_order.append([quantity_match.name, quantity_match.price, order_quantity])
            curr_client.shopping_cart.append(client_meal)

        if order_successful:

            client_bill = sum(quant * price for name, price, quant in client_order)
            curr_client.bill += client_bill

            meal_names = ', '.join(meal.name for meal in curr_client.shopping_cart)

            return f"Client {client_phone_number} successfully ordered {meal_names} for {curr_client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        curr_client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)


        if curr_client is None:
            # print("there is no client with that phone_number")
            pass


        if not curr_client.shopping_cart:
            raise Exception("There are no ordered meals!")

        # print("====================================")
        # print("client_shopping_cart")
        # print([f"{m.name}: {m.quantity}" for m in curr_client.shopping_cart])
        # print("menu:")
        # print([f"{m.name}: {m.quantity}" for m in self.menu])


        for meal in curr_client.shopping_cart:

            list_of_menu_names = [meal.name for meal in self.menu]
            if meal.name in list_of_menu_names:
                curr_meal_in_menu = next(meal_in_menu for meal_in_menu in self.menu if meal_in_menu.name == meal.name)
                # append only quantity
                curr_meal_in_menu.quantity += meal.quantity
                continue

            elif meal.name not in list_of_menu_names:
                # append whole product
                self.menu.append(meal)
                continue

        curr_client.shopping_cart = []
        curr_client.bill = 0

        # print("client_shopping_cart")
        # print([m.name for m in curr_client.shopping_cart])
        # print("menu:")
        # print([f"{m.name}: {m.quantity}" for m in self.menu])

        return f"Client {curr_client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        curr_client = next((c for c in self.clients_list if c.phone_number == client_phone_number), None)

        if curr_client is None:
            # print("there is no client with that phone_number")
            pass


    def _is_menu_ready(self):
        if len(self.menu) < self.MINIMUM_MEALS_IN_MENU:
            raise Exception("The menu is not ready!")




"""
from project.food_orders_app import FoodOrdersApp
from project.meals.starter import Starter
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish

"""

food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
print(food_orders_app.register_client("0899999991"))
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
# food = {"Hummus and Avocado Sandwich": 5,
#         "Risotto with Wild Mushrooms": 1,
#         "Chocolate and Violets": 4}
#
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))

print(food_orders_app.cancel_order('0899999999'))

# print(food_orders_app.finish_order("0899999999"))
# print(food_orders_app)







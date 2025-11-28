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

        if not curr_client.shopping_cart:
            raise Exception("There are no ordered meals!")


        curr_client.shopping_cart = []
        total_paid_money = curr_client.bill
        curr_client.bill = 0
        curr_client.receipt_id += 1

        return f"Receipt #{curr_client.receipt_id} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        number_of_listed_meals = len(self.menu)
        number_of_clients = len(self.clients_list)
        return f"Food Orders App has {number_of_listed_meals} meals on the menu and {number_of_clients} clients."


    def _is_menu_ready(self):
        if len(self.menu) < self.MINIMUM_MEALS_IN_MENU:
            raise Exception("The menu is not ready!")














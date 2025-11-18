from project.user import User
from project.route import Route
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:

    VALID_VEHICLES_TYPE: dict = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan,
    }

    def __init__(self):
        self.users: list[User] = []
        self.vehicles: list[BaseVehicle] = []
        self.routes: list[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            next(u for u in self.users if u.driving_license_number == driving_license_number)
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            new_user = User(first_name, last_name, driving_license_number)
            self.users.append(new_user)
            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"


    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        try:
            new_vehicle = self.VALID_VEHICLES_TYPE[vehicle_type](brand, model, license_plate_number)
        except KeyError:
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            have_vehicle = next(v for v in self.vehicles if v.license_plate_number == license_plate_number)
            return f"{license_plate_number} belongs to another vehicle."
        except StopIteration:
            self.vehicles.append(new_vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        try:
            have_route_with_same_start_and_end_point = next(r for r in self.routes if r.start_point == start_point and r.end_point == end_point)
            if have_route_with_same_start_and_end_point.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            elif have_route_with_same_start_and_end_point.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            elif have_route_with_same_start_and_end_point.length > length:
                have_route_with_same_start_and_end_point.is_locked = True

                route_id = len(self.routes) + 1
                shorter_route = Route(start_point, end_point, length, route_id)
                self.routes.append(shorter_route)
                return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

        except StopIteration:
            route_id = len(self.routes) + 1
            new_route = Route(start_point, end_point, length, route_id)
            self.routes.append(new_route)
            return f"{start_point}/{end_point} - {length} km is unlocked and available to use."




    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        route = next((r for r in self.routes if r.route_id == route_id), None)

        if user and vehicle and route:

            if user.is_blocked:
                return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

            if vehicle.is_damaged:
                return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

            if route.is_locked:
                return f"Route {route_id} is locked! This trip is not allowed."

            vehicle.drive(route.length)

            if is_accident_happened:
                vehicle.change_status()
                user.decrease_rating()
            elif not is_accident_happened:
                user.increase_rating()

            return str(vehicle)


    def repair_vehicles(self, count: int):
        repaired_count = 0

        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        if len(damaged_vehicles) <= count:
            for v in damaged_vehicles:
                repaired_count += 1
                v.change_status()
                v.recharge()

        else:
            sorted_damaged_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))
            for vehicle in sorted_damaged_vehicles[:count]:
                repaired_count += 1
                vehicle.change_status()
                vehicle.recharge()

        return f"{repaired_count} vehicles were successfully repaired!"


    def users_report(self):
        result = ["*** E-Drive-Rent ***"]
        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        for u in sorted_users:
            result.append(str(u))
        return '\n'.join(result)


# for testing:

app = ManagingApp()
print(app.register_user( 'Tisha', 'Reenie', '7246506' ))
print(app.register_user( 'Bernard', 'Remy', 'CDYHVSR68661'))
print(app.register_user( 'Mack', 'Cindi', '7246506'))
print(app.upload_vehicle('PassengerCar', 'Chevrolet', 'Volt', 'CWP8032'))
print(app.upload_vehicle( 'PassengerCar', 'Volkswagen', 'e-Up!', 'COUN199728'))
print(app.upload_vehicle('PassengerCar', 'Mercedes-Benz', 'EQS', '5UNM315'))
print(app.upload_vehicle('CargoVan', 'Ford', 'e-Transit', '726QOA'))
print(app.upload_vehicle('CargoVan', 'BrightDrop', 'Zevo400', 'SC39690'))
print(app.upload_vehicle('EcoTruck', 'Mercedes-Benz', 'eActros', 'SC39690'))
print(app.upload_vehicle('PassengerCar', 'Tesla', 'CyberTruck', '726QOA'))
print(app.allow_route('SOF', 'PLD', 144))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('BUR', 'VAR', 87))
print(app.allow_route('SOF', 'PLD', 184))
print(app.allow_route('BUR', 'VAR', 86.999))
print(app.make_trip('CDYHVSR68661', '5UNM315', 3, False))
print(app.make_trip('7246506', 'CWP8032', 1, True))
print(app.make_trip('7246506', 'COUN199728', 1, False))
print(app.make_trip('CDYHVSR68661', 'CWP8032', 3, False))
print(app.make_trip('CDYHVSR68661', '5UNM315', 2, False))
print(app.repair_vehicles(2))
print(app.repair_vehicles(20))
print(app.users_report())

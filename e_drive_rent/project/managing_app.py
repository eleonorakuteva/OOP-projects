from project.user import User
from project.route import Route
from project.vehicles.base_vehicle import BaseVehicle


class ManagingApp:
    def __init__(self):
        self.users: list[User] = []
        self.vehicles: list[BaseVehicle] = []
        self.routes: list[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        pass

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        pass

    def allow_route(self, start_point: str, end_point: str, length: float):
        pass

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        pass

    def repair_vehicles(self, count: int):
        pass

    def users_report(self):
        pass
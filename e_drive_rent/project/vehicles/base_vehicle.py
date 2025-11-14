from abc import ABC, abstractmethod


class BaseVehicle:

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage
        self.battery_level: int = 100
        self.is_damaged: bool = False


    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not value.strip():
            raise ValueError("Brand cannot be empty!")
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value:str):
        if not value.strip():
            raise ValueError("Model cannot be empty!")
        self.__model = value
        
    @property
    def license_plate_number(self):
        return self.__license_plate_number
    
    @license_plate_number.setter
    def license_plate_number(self, value: str):
        if not value.strip():
            raise ValueError("License plate number is required!")
        self.__license_plate_number = value

    @abstractmethod
    def drive(self, mileage: float):
        pass

    def recharge(self):
        self.battery_level = 100

    def __str__(self):
        return (f"{self.brand} {self.model} "
                f"License plate: {self.license_plate_number} "
                f"Battery: {self.battery_level}% "
                f"Status: {'Damaged' if self.is_damaged else 'OK'}")


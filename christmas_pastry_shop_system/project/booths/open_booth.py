from project.booths.booth import Booth


class OpenBooth(Booth):

    PRICE_RESERVATION_PER_PERSON: float = 2.5

    def __init__(self, booth_number: int,  capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.PRICE_RESERVATION_PER_PERSON
        self.is_reserved = True

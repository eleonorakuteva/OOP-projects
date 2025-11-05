from room import Room

class Hotel:
    def __init__(self, name:str) -> None:
        self.name = name
        self.rooms:list[Room] = []

    @property
    def guests(self):
        return sum(r.guests for r in self.rooms)

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")


    def add_room(self, room:Room):
        return self.rooms.append(room)


    def take_room(self, room_number:int, people:int):
        room_with_curr_number = next((r for r in self.rooms if r.number == room_number), None)
        if room_with_curr_number:
            return room_with_curr_number.take_room(people)


    def free_room(self, room_number:int) -> None:
        room_with_curr_number = next((r for r in self.rooms if r.number == room_number), None)
        if room_with_curr_number:
            return room_with_curr_number.free_room()

    def status(self) -> str:
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(free_rooms)}\n"
                f"Taken rooms: {', '.join(taken_rooms)}")

# ==========================
# hotel = Hotel.from_stars(5)
#
# first_room = Room(1, 3)
# second_room = Room(2, 2)
# third_room = Room(3, 1)
#
# hotel.add_room(first_room)
# hotel.add_room(second_room)
# hotel.add_room(third_room)
#
# hotel.take_room(1, 4)
# hotel.take_room(1, 2)
# hotel.take_room(3, 1)
# hotel.take_room(3, 1)
#
# print(hotel.status())
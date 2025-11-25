from project.band_members.musician import Musician


class Drummer(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    @property
    def available_skills_for_type_of_musician(self) -> list[str]:
        return ["play the drums with drumsticks",
                "play the drums with drum brushes",
                "read sheet music"]


from project.movie_specification.movie import Movie


class Action(Movie):

    MINIMUM_AGE_RESTRICTIONS = 12

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = None):
        if age_restriction is None:
            age_restriction = self.MINIMUM_AGE_RESTRICTIONS
        super().__init__(title, year, owner, age_restriction=age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value: int):
        if value < self.MINIMUM_AGE_RESTRICTIONS:
            raise ValueError("Action movies must be restricted for audience under 12 years!")
        self.__age_restriction = value


    @property
    def type(self):
        return "Action"
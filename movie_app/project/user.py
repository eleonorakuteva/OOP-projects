from project.movie_specification.movie import Movie


class User:

    MINIMUM_ALLOWED_AGE = 6

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked: list[Movie] = []
        self.movies_owned: list[Movie] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value: str):
        if not value.strip():
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < self.MINIMUM_ALLOWED_AGE:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = [f"Username: {self.username}, Age: {self.age}"]

        if self.movies_liked:
            result.append("Liked movies:")
            for movie in self.movies_liked:
                result.append(movie.details())
        else:
            result.append("No movies liked.")


        if self.movies_owned:
            result.append("Owned movies:")
            for movie in self.movies_owned:
                result.append(movie.details())

        else:
            result.append("No movies owned.")

        return '\n'.join(result) 


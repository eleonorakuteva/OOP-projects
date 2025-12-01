from logging import raiseExceptions

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: list[Movie] = []
        self.users_collection: list[User] = []


    def register_user(self, username: str, age: int):
        user = self._find_user_by_username(username)
        if user:
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."


    def upload_movie(self, username: str, movie: Movie):
        """
        Only the owner of the given movie can upload it.
        The method adds the movie to the user's movies_owned list as well as the movies_collection list
        """

        curr_user = self._find_user_by_username(username)
        if curr_user is None:
            raise Exception("This user does not exist!")

        if movie.owner != curr_user:
            raise Exception(f"{curr_user.username} is not the owner of "
                            f"the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        curr_user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."


    def edit_movie(self, username: str, movie: Movie, **kwargs):
        """
        Only the owner of the movie given can edit it.
        You will always be given usernames of registered users.
        In this method, as kwargs you can receive one or more key-value pairs.
        Each key will be a movie's attribute name ("title", "year", or "age_restriction"), and the value will be the new value for that attribute.
        You will not receive anything different from the keys mentioned above.
        The method edits the movie attributes with the given values.
        """

        curr_user = self._find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != curr_user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        print(movie.__dict__)
        for attribute in kwargs:
            if attribute in movie.__dict__:
                pass

        return f"{username} successfully edited {movie.title} movie."


    def delete_movie(self, username: str, movie: Movie):
        """
        Only the owner of the movie given can delete it.
        You will always be given usernames of registered users.
        This method deletes the movie given in both movies_collection and user's movies_owned lists.
        """
        curr_user = self._find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner != curr_user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        curr_user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        """
        Owners cannot like their own movies.
        You will always be given usernames of registered users and uploaded movies.
        This method increases the value of the movie attribute likes by 1
        and adds the movie to the user's list movies_liked
        """

        curr_user = self._find_user_by_username(username)
        if movie.owner == curr_user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in curr_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        curr_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        """
        Only the user who has liked the movie can dislike it.
        You will always be given usernames of registered users and uploaded movies.
        This method decreases the value of the movie attribute likes by 1
        and removes that movie from the user's movies_liked list.
        """

        curr_user = self._find_user_by_username(username)
        if movie not in curr_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        curr_user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."


    def display_movies(self):
        pass


    def __str__(self):
        pass





    def _find_user_by_username(self, username) -> User | None:
        user = next((u for u in self.users_collection if u.username == username), None)
        return user
from project.movie_specification.movie import Movie
from project.user import User

class MovieApp:

    def __init__(self):
        self.movies_collection: list[Movie] = []
        self.users_collection: list[User] = []


    def register_user(self, username: str, age: int):
        curr_user = self._find_user_by_username(username)
        if curr_user:
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."


    def upload_movie(self, username: str, curr_movie: Movie):
        """
        Only the owner of the given movie can upload it.
        The method adds the movie to the user's movies_owned list as well as the movies_collection list
        """

        curr_user = self._find_user_by_username(username)
        if curr_user is None:
            raise Exception("This user does not exist!")

        if curr_movie.owner != curr_user:
            raise Exception(f"{curr_user.username} is not the owner of "
                            f"the movie {curr_movie.title}!")

        if curr_movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        curr_user.movies_owned.append(curr_movie)
        self.movies_collection.append(curr_movie)
        return f"{username} successfully added {curr_movie.title} movie."


    def edit_movie(self, username: str, curr_movie: Movie, **kwargs):
        """
        Only the owner of the movie given can edit it.
        You will always be given usernames of registered users.
        In this method, as kwargs you can receive one or more key-value pairs.
        Each key will be a movie's attribute name ("title", "year", or "age_restriction"), and the value will be the new value for that attribute.
        You will not receive anything different from the keys mentioned above.
        The method edits the movie attributes with the given values.
        """

        curr_user = self._find_user_by_username(username)

        if curr_movie not in self.movies_collection:
            raise Exception(f"The movie {curr_movie.title} is not uploaded!")

        if curr_movie.owner != curr_user:
            raise Exception(f"{username} is not the owner of the movie {curr_movie.title}!")

        # Edit the movie attributes with the given kwargs
        for attribute, value in kwargs.items():
            setattr(curr_movie, attribute, value)

        return f"{username} successfully edited {curr_movie.title} movie."


    def delete_movie(self, username: str, curr_movie: Movie):
        """
        Only the owner of the movie given can delete it.
        You will always be given usernames of registered users.
        This method deletes the movie given in both movies_collection and user's movies_owned lists.
        """
        curr_user = self._find_user_by_username(username)

        if curr_movie not in self.movies_collection:
            raise Exception(f"The movie {curr_movie.title} is not uploaded!")

        if curr_movie.owner != curr_user:
            raise Exception(f"{username} is not the owner of the movie {curr_movie.title}!")

        self.movies_collection.remove(curr_movie)
        curr_user.movies_owned.remove(curr_movie)
        return f"{username} successfully deleted {curr_movie.title} movie."

    def like_movie(self, username: str, curr_movie: Movie):
        """
        Owners cannot like their own movies.
        You will always be given usernames of registered users and uploaded movies.
        This method increases the value of the movie attribute likes by 1
        and adds the movie to the user's list movies_liked
        """

        curr_user = self._find_user_by_username(username)
        if curr_movie.owner == curr_user:
            raise Exception(f"{username} is the owner of the movie {curr_movie.title}!")

        if curr_movie in curr_user.movies_liked:
            raise Exception(f"{username} already liked the movie {curr_movie.title}!")

        curr_movie.likes += 1
        curr_user.movies_liked.append(curr_movie)
        return f"{username} liked {curr_movie.title} movie."

    def dislike_movie(self, username: str, curr_movie: Movie):
        """
        Only the user who has liked the movie can dislike it.
        You will always be given usernames of registered users and uploaded movies.
        This method decreases the value of the movie attribute likes by 1
        and removes that movie from the user's movies_liked list.
        """

        curr_user = self._find_user_by_username(username)
        if curr_movie not in curr_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {curr_movie.title}!")

        curr_movie.likes -= 1
        curr_user.movies_liked.remove(curr_movie)
        return f"{username} disliked {curr_movie.title} movie."


    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda m: (-m.year, m.title))

        if not sorted_movies:
            return "No movies found."

        result = []
        for movie in sorted_movies:
            result.append(movie.details())

        return '\n'.join(result)


    def __str__(self):

        all_users = "All users: "
        if self.users_collection:
            all_users += ', '.join(user.username for user in self.users_collection)
        else:
            all_users += "No users."

        all_movies = "All movies: "
        if self.movies_collection:
            all_movies += ', '.join(m.title for m in self.movies_collection)
        else:
            all_movies += "No movies."

        return f"{all_users}\n{all_movies}"


    def _find_user_by_username(self, username) -> User | None:
            user = next((u for u in self.users_collection if u.username == username), None)
            return user



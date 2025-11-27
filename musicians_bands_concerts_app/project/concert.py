class Concert:

    VALID_GENRE = ["Metal", "Rock", "Jazz"]
    MINIMUM_AUDIENCE: int = 1
    MINIMUM_PRICE_PER_TICKET: float = 1.0
    MINIMUM_EXPENSES: float = 0.0
    MINIMUM_CHAR_LONG_PLACE = 2

    def __init__(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.genre = genre
        self.audience = audience
        self.ticket_price = ticket_price
        self.expenses = expenses
        self.place = place

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value: str):
        if value not in self.VALID_GENRE:
            raise ValueError(f"Our group doesn't play {value}!")
        self.__genre = value

    @property
    def audience(self):
        return self.__audience

    @audience.setter
    def audience(self, value: int):
        if value < self.MINIMUM_AUDIENCE:
            raise ValueError("At least one person should attend the concert!")
        self.__audience = value

    @property
    def ticket_price(self):
        return self.__ticket_price

    @ticket_price.setter
    def ticket_price(self, value: float):
        if value < self.MINIMUM_PRICE_PER_TICKET:
            raise ValueError("Ticket price must be at least 1.00$!")
        self.__ticket_price = value

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value: float):
        if value < self.MINIMUM_EXPENSES:
            raise ValueError("Expenses cannot be a negative number!")
        self.__expenses = value

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value: str):
        if len(value.strip()) < self.MINIMUM_CHAR_LONG_PLACE:
            raise ValueError("Place must contain at least 2 chars. It cannot be empty!")
        self.__place = value

    def __str__(self):
        return f"{self.genre} concert at {self.place}."


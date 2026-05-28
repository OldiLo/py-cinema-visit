from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int = None, hall_number: int = None) -> None:
        self.hall_number = number if number is not None else hall_number
        self.number = number if number is not None else hall_number

    def movie_session(
        self, movie_name: str, customers: list[Customer], cleaning_stuff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.hall_number}.')
        for customer in customers:
            customer.watch_movie(movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_stuff.clean_hall(self.hall_number)

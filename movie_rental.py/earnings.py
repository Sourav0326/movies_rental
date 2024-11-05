from rentals import rented_movies


def calculate_rental_earnings():
    total_earnings = 0
    for movies in rented_movies.values():
        for movie in movies:
            total_earnings += movie[2]
    return total_earnings
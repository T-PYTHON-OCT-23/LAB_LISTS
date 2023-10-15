def averageMovie(movie):
    filteredMovies = []
    for title, year, ratings in movie:
        averageRating = sum(ratings) / len(ratings)
        if averageRating >= 6.0:
            filteredMovies.append((title, year, averageRating))
            for title, year, averageRating in filteredMovies:
               print(f" {title} ({year})- Average Rating: {averageRating:.2f}")






movies = [("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
          ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
          ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
          ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
          ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
          ("The Room", 2003, [1, 2, 3, 4, 5, 1])]
averageMovie(movies)
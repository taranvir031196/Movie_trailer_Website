"""Stores details of movies and displays them on a website."""
import media
import fresh_tomatoes


"""Six Movie objects, initialising these objects with title, storyline,
   poster image link, video trailer link and release date."""
the_revenant = media.Movie("The Revenant",
                           "Hugh Glass,is injured and abandoned by the crew",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
                           "https://www.youtube.com/watch?v=LoebZZ8K5N0")


inception = media.Movie("Inception",
                        "Movie about dreams of the target",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")


La_La_land = media.Movie("La La Land",
                         "A Story of a pianoist",
                         "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                         "https://www.youtube.com/watch?v=0pdqf4P9MB8")

the_Martian = media.Movie("The Martian",
                          "A Story of an astronaut stuck on mars",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

the_avengers = media.Movie("The Avengers",
                           "An American superhero based film",
                           "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")

Moonlight = media.Movie("Moonlight",
                        "A life of young man chiron growing in miami",
                        "https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png",
                        "https://www.youtube.com/watch?v=9NJj12tJzqc")

# list of objects of the class Movie is created in order to create a webpage using fresh_tomatoes module.
# using the open_movies_page(movies) function in fresh_tomatoes is used to
# create a webpage containing list of all above defined objects.
movies = [the_revenant, inception, La_La_land,
          the_Martian, the_avengers, Moonlight]
fresh_tomatoes.open_movies_page(movies)

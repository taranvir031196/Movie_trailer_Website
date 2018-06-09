import webbrowser


class Movie():
    """This class provides a way to store movie related information
    Attributes:
        title: The title of the movie
        storyline: A short description of what the movie is about
        poster_image_url: The URL address of a poster of the movie
        trailer_youtube_url: A link page that shows the trailer of the movie
    """

    def __init__(self, movie_title, storyline, poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # instance method defined
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

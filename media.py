# class webbrowser from std lib is imported
import webbrowser


class Movie():

    # pre-defined variable__doc__
    """This is a moive trailer demonstrator"""

    # define class variable VALID_RATINGS for possible ratings of the movies
    VALID_RATINGS = ["g", "pg", "pg-13", "r"]

    # define the constructor that takes arguments
    # movie_title,movie_storyline, poster_image, trailer_youtube
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # define a class function named show_trailer that opens the trailer
    # link using default webbrowser of the system
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

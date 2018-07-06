import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    # Movie Class Constructor
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title  # Movie Title
        self.storyline = movie_storyline  # Movie Storyline
        self.poster_image_url = poster_image  # Movie Poster Image
        self.trailer_youtube_url = trailer_youtube  # Movie Trailer

    # Show Movie Trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

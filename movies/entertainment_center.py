import fresh_tomatoes
import media


"""Create movie objects with information of each movie
   (Title, Storyline, Poster and Trailer) """

hidden_figures = media.Movie("Hidden Figures",  # Movie title
                             # Movie Storyline
                             "American biographical drama film about "
                             "black female mathematicians who worked at NASA",
                             # Movie Poster image
                             "https://upload.wikimedia.org/wikipedia/en/4/4f/The_official_poster_for_the_film_Hidden_Figures%2C_2016.jpg",  # noqa
                             # Movie Trailer
                             "https://www.youtube.com/watch?v=5wfrDhgUMGI")

the_bucket_list = media.Movie("The Bulket List",
                              "Two terminally ill men on their road trip "
                              "with a wish list of things to do before "
                              "they 'kick the bucket'",
                              "https://upload.wikimedia.org/wikipedia/en/2/20/Bucket_list_poster.jpg",  # noqa
                              "https://www.youtube.com/watch?v=vc3mkG21ob4")

moneyball = media.Movie("Moneyball",
                        "The general manager of a baseball team and "
                        "his assistent faced with the franchise's "
                        "limited budget for players, build a team of "
                        "undervalued talent by taking a sophisticated "
                        "sabermetric approach towards scouting "
                        "and analyzing players.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Moneyball_Poster.jpg",  # noqa
                        "https://www.youtube.com/watch?v=-4QPVo0UIzc")


the_godfather = media.Movie("The Godfather",
                            "Italian gangsters leaders of a "
                            "New York crime family",
                            "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",  # noqa
                            "https://www.youtube.com/watch?v=sY1S34973zA")


the_blind_side = media.Movie("The Blind Side",
                             "The story of a NFL offensive lineman "
                             "called Michael Oher",
                             "https://upload.wikimedia.org/wikipedia/en/6/60/Blind_side_poster.jpg",  # noqa
                             "https://www.youtube.com/watch?v=gvqj_Tk_kuM")


darkest_hour = media.Movie("Darkest Hour",
                           "Winston Churchill in his early days as "
                           "Prime Minister of England",
                           "https://upload.wikimedia.org/wikipedia/en/3/38/Darkest_Hour_poster.png",  # noqa
                           "https://www.youtube.com/watch?v=LtJ60u7SUSw")

# Creates a list with movies objects
movies = [hidden_figures, moneyball, the_godfather, the_blind_side,
          darkest_hour, the_bucket_list]

# Open webpage with movies in the list
fresh_tomatoes.open_movies_page(movies)

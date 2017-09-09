# media and fresh_tomatoes are imported
# enabling using of defined variables and functions
import media
import fresh_tomatoes

# instance terminator under class Movie
terminator = media.Movie("Terminator 2",
                        "Bad ass robot",
                        "http://www.chud.com/wp-content/uploads/2015/06/T2-Poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=lYOoWCv_PYE")
# instance god under class Movie
god = media.Movie("Godfather",
                   "An offer you cannot refuse",
                   "http://vignette1.wikia.nocookie.net/godfather/images/e/e0/The_Godfather_Logo.png/revision/latest?cb=20111102175214",  # NOQA
                   "https://www.youtube.com/watch?v=sY1S34973zA")
# instance metal under class Movie
metal = media.Movie("Through the Never",
                   "Metallica",
                   "https://upload.wikimedia.org/wikipedia/en/b/bd/Metallica_Through_the_Never_film.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=N4IhWJ8r7_4")
# instance iron under class Movie
iron = media.Movie("Iron Man",
                   "Rich ass against the world",
                   "http://4.bp.blogspot.com/-iConLAboNUs/TsSSRCxZ5AI/AAAAAAAAGfU/S887s09UkGU/s1600/acdc2.jpg",  # NOQA
                   "https://www.youtube.com/watch?annotation_id=annotation_1710640575&feature=iv&src_vid=ttzxpmZUb9M&v=x6o94iDQrBU")  # NOQA

# creates an array of instances of type class Movie
movies = [terminator, god, metal, iron]

# generates a trailer page for the movies and open with default browser
fresh_tomatoes.open_movies_page(movies)

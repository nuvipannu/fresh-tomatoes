from media import Movie
import fresh_tomatoes

"""
## Movie class parameters
  - title
  - my comment
  - poster image
  - trailer
  - my rating
  - genre
  - running time
"""

scarface = Movie("Scarface",
                     "Most quoted gangster movie out there",
                     "images/scarface.jpg",
                     "https://www.youtube.com/watch?v=7pQQHnqBa2E",
                     5,
                     "Crime",
                     170)

frozen = Movie("Frozen",
               "The music soundtrack is so good.. Let it go xD",
               "images/frozen.jpg",
               "https://www.youtube.com/watch?v=TbQm5doF_Uc",
               5,
               "Animation",
               102)

black_swan = Movie("Black Swan",
                   "This is the best female performance ever",
                   "images/black_swan.jpg",
                   "https://www.youtube.com/watch?v=5jaI1XOB-bs",
                   5,
                   "Thriller",
                   108)

inception = Movie("Inception",
                  "A dream in a dream in a dream.. Whoa!",
                  "images/inception.jpg",
                  "http://youtu.be/8hP9D6kZseM",
                  5,
                  "Thriller",
                  148)

love_actually = Movie("Love Actually",
                      "Lots of great + famous actors",
                      "images/love_actually.jpg",
                      "http://youtu.be/KdzH6a-XEGM",
                      5,
                      "Romantic Comedy",
                      135)

wolf_of_wall_street = Movie("The Wolf of Wall Street",
                            "Awesome movie. DiCaprio is the man!",
                            "images/wolf.jpg",
                            "http://youtu.be/iszwuX1AK6A",
                            4.5,
                            "Drama",
                            179)

constantine = Movie("Constantine",
                    "This is Constantine, John Constantine... a$$hole",
                    "images/constantine.jpg",
                    "http://youtu.be/ivee8cm55Ao",
                    5,
                    "Fantasy",
                    120)

a_lot_like_love = Movie("A Lot Like Love",
                        "A lot like love story",
                        "images/alot_like_love.jpg",
                        "http://www.youtube.com/watch?v=1qLUMSbrlDE",
                        5,
                        "Romantic Comedy",
                        106)

penguins_of_madagascar = Movie("Penguins of Madagascar",
                               "Cute and cuddly penguins! :) <3",
                               "images/penguins.jpg",
                               "http://youtu.be/KHGHEpUeUwo",
                               4,
                               "Animation",
                               92)

x_men_dofp = Movie("X-MEN: Days of Future Past",
                   "Wolverine goes back in time",
                   "images/xmen_dofp.jpg",
                   "http://youtu.be/pK2zYHWDZKo",
                   4,
                   "Action",
                   132)

dark_knight = Movie("Dark Knight",
                   "The best crime and thriller movie of all time!",
                   "images/dark_knight.jpg",
                   "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                   5.0,
                   "Crime",
                   152)

pirates = Movie("Pirates of the Caribbean: The Curse of the Black Pearl",
                   "The first and best of all four POC's",
                   "images/pirates.jpg",
                   "https://www.youtube.com/watch?v=0Z1XpfbuZOA",
                   5.0,
                   "Action",
                   143)

# List of all movies
movies = [
    scarface,
    frozen,
    black_swan,
    inception,
    love_actually,
    wolf_of_wall_street,
    constantine,
    a_lot_like_love,
    penguins_of_madagascar,
    x_men_dofp,
    dark_knight,
    pirates,
]

def main():
    """
    Main function of this module
    Create a new HTML file with movie data
    This will open a new page in your browser
    """
    fresh_tomatoes.open_movies_page(movies)

# Executed if this module is ran as a primary module
if __name__ == "__main__":
    main()

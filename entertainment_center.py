"""This is a module used for the Movies Trailer website for Udacity's
Full Stack Web Developer Nanodegree Program - Project 1.
This module uses the fresh_tomatoes.py file provided by Udacity.
Movies are defined below using the Movie class defined in media.py.
The below was created with the help from the Coding the Movie
Website lesson from Udacity. Note that fresh_tomatoes.py
and media.py need to be in the same folder as this file."""

import media
import fresh_tomatoes


# The movies' title, story line, URL image, and URL trailer are defined
zoolander = media.Movie("Zoolander",
                        "A not so bright male model tasked to"
                        " save the Prime Minister",
                        "https://upload.wikimedia.org/wikipedia/"
                        "en/7/7c/Movie_poster_zoolander.jpg",
                        "https://www.youtube.com/watch?v=YtQq0T3ExLs")

blindside = media.Movie("The Blindside",
                        "The story of an adopted African-American foster"
                        "teenager who becomes a successful NFL player",
                        "https://upload.wikimedia.org/wikipedia/en/6/60"
                        "/Blind_side_poster.jpg",
                        "https://www.youtube.com/watch?v=dJ3kwMq18-8")

tangled = media.Movie("Tangled",
                      "Disney's story of Rapunzel",
                      "https://upload.wikimedia.org/wikipedia/en/a/a8/"
                      "Tangled_poster.jpg",
                      "https://www.youtube.com/watch?v=ip_0CFKTO9E")

ironman = media.Movie("Iron Man",
                      "Story of Tony Stark played by Robert Downey"
                      "Jr. as Marvel's Iron Man Superhero",
                      "https://upload.wikimedia.org/wikipedia/en/7/70"
                      "/Ironmanposter.JPG",
                      "https://www.youtube.com/watch?v=KAE5ymVLmZg")

rascals = media.Movie("The Little Rascals",
                      "A comedy based on a group of neighborhood children"
                      " and their attempt to win a race car derby",
                      "https://upload.wikimedia.org/wikipedia/en/6/6f/"
                      "Little_rascals_ver2.jpg",
                      "https://www.youtube.com/watch?v=qcOB45HMVzE")

monsters = media.Movie("Monster's Inc.",
                       "Pixar's child-friendly story of a monster"
                       "world powered by the screams of children",
                       "https://upload.wikimedia.org/wikipedia/en/"
                       "6/63/Monsters_Inc.JPG",
                       "https://www.youtube.com/watch?v=cvOQeozL4S0")

# fresh_tomatoes.py creates a website based on an array of defined movies
movies = [zoolander, blindside, tangled, ironman, rascals, monsters]
fresh_tomatoes.open_movies_page(movies)

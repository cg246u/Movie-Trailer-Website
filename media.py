"""This is a module used for the Movies Trailer website for Udacity's
Full Stack Web Developer Nanodegree Program - Project 1.
Below is a Python class that stores the movie title, storyline,
a URL link to an image of the movie, and a URL link
to the trailer of the movie. The structure was defined from
the help of Udacity's Designing the Movie Website lesson."""

import webbrowser


class Movie():

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # variables for movie title, story line, poster URL, and trailer URL
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # uses webbrowser module to open the movie trailer
        webbrowser.open(self.trailer_youtube_url)


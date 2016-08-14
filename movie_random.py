__author__ = 'Orka'

import random

class MovieRandom(object):
    def __init__(self, movie_list):
        self.movie_list = movie_list

    def return_random_movie(self):
        if type(self.movie_list) is list:
            list_length = len(self.movie_list)
            random_number = random.randrange(list_length)
            random_movie = self.movie_list[random_number]
            return random_movie
        elif self.movie_list == 'No movie of this length.':
            return self.movie_list
        else:
            return 'Movie list is empty'
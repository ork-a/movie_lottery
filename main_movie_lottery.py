__author__ = 'Orka'
from movie_list import MovieList
from movie_random import MovieRandom
from remove_chosen_movie_from_list import RemoveChosenMovieFromList
from save_list_to_CSV import SaveListToCSV
from length_limit import LengthLimit

file_name = 'cinema.csv'
function = 'r+'
filename_save = 'cinema.csv'
function_save = 'w'


class LaunchMovieLottery(object):
    def __init__(self, limit_low=None, limit_high=None):
        self.limit_low = limit_low
        self.limit_high = limit_high
        self.full_list = None

    def movie_list(self):
        # creates movies list without sequels
        movie_list = MovieList(file_name, function)
        self.return_movie_list = movie_list.return_movie_list()
        self.full_list = movie_list.return_full_list()
        return [self.return_movie_list, self.full_list]

    def limit_list(self):
        self.movie_list()
        # limit the movie_list - returns list of movies limited to the specified length
        limit_length = LengthLimit(self.return_movie_list, self.limit_low, self.limit_high)
        self.shorten_list = limit_length.return_asked_length()
        # returns: 'No movie of this length.'

    def return_movie(self):
        self.limit_list()
        # draw a movie from movie list and print it
        movie_random = MovieRandom(self.shorten_list)
        self.temp_movie_random = movie_random.return_random_movie()
        return self.temp_movie_random

    def remove_and_save(self, the_movie):
        full_list = self.movie_list()[1]

        try:
            # remove chosen movie from movie list and allow the next movie in the series in next lottery
            remove = RemoveChosenMovieFromList(the_movie, full_list)
            new_movie_list = remove.remove_movie()

            # save to CSV
            save_doc = SaveListToCSV(new_movie_list, filename_save, function_save)
            save_doc.save_file()

        except ValueError:
            # Movie not exists
            pass

__author__ = 'Orka'


class RemoveChosenMovieFromList(object):
    def __init__(self, movie, movie_list):
        self.movie = movie
        self.movie_list = movie_list

    def remove_movie(self):
        list_number = self.movie_list.index(self.movie)
        self.movie_list.remove(self.movie)
        if self.movie_list[list_number-1][3] == 1:
            self.movie_list[list_number-1][3] = 0
        return self.movie_list

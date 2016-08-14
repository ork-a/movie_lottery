__author__ = 'Orka'
import csv

class MovieList(object):
    def __init__(self, file_name, function):
        self.file_name = file_name
        self.function = function

    def return_movie_list(self):
        with open(self.file_name, self.function) as movies:
            movies = csv.reader(movies)
            movie_list = []
            for row in movies:
                if row != []:
                    if row[3] != '1' and row[1] != '' and row[1] != 'not found':
                        movie_list.append(row)
            return movie_list

    def return_full_list(self):
        with open(self.file_name, self.function) as movies:
            movies = csv.reader(movies)
            full_movie_list = []
            for row in movies:
                if row != []:
                    full_movie_list.append(row)
            return full_movie_list


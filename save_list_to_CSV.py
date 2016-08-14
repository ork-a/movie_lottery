__author__ = 'Orka'
import csv

class SaveListToCSV(object):
    def __init__(self, movie_list, filename_save, function_save):
        self.movie_list = movie_list
        self.filename_save = filename_save
        self.function_save = function_save


    def save_file(self):
        with open(self.filename_save, self.function_save, newline='') as movies:
            writer = csv.writer(movies, delimiter = ',')
            writer.writerows(self.movie_list)
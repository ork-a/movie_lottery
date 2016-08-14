__author__ = 'Orka'
from min_max_length import check_max_min_length
from check_input import check_input

class LengthLimit():
    def __init__(self, movie_list, low_limit = None, up_limit = None):
        self.movie_list = movie_list
        self.low_limit = low_limit
        self.up_limit = up_limit
        self.low_limit, self.up_limit = check_input(self.low_limit, self.up_limit)

    def return_asked_length(self):
        if self.movie_list != []:
            #check the length of shortest and longest movie
            minimum, maximum = check_max_min_length(self.movie_list)

            #check if the input is integer
            self.low_limit, self.up_limit = check_input(self.low_limit, self.up_limit)

            #check if the input is of correct length
            if self.low_limit >= minimum or self.up_limit <= maximum:
                shorten_list = []
                min_list = []
                max_list = []
                for each in self.movie_list:
                    if int(each[4]) >= self.low_limit:
                        min_list.append(each)
                    if int(each[4]) <= self.up_limit:
                        max_list.append(each)
                for one in min_list:
                    if one in max_list:
                        shorten_list.append(one)
                if len(shorten_list) > 0:
                    return shorten_list
                else:
                    return 'No movie of this length.'

            else:
                #user specified limits are incorrect: returns full list of movies
                return self.movie_list
        else:
            return None






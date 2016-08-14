__author__ = 'Orka'

def check_max_min_length(movie_list):
    if len(movie_list) > 0:
        duration_list = []
        for each in movie_list:
            duration_list.append(int(each[4]))
        minimum = min(duration_list)
        maximum = max(duration_list)
        return minimum, maximum
    else:
        return 0, 0
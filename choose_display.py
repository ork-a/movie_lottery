__author__ = 'Orka'
from find_movie_picture import FindMoviePicture


class ChooseDisplay(object):
    def __init__(self, the_movie):
        self.the_movie = the_movie

    def choose_display(self):
        # chooses the picture and text to be displayed
        if self.the_movie == 'No movie of this length.':
            image = 'wrong-length.jpg'
        elif self.the_movie == 'Movie list is empty':
            image = 'emptylist.jpg'
        else:
            image = 'resized.jpg'
            # find and download movie poster
            temp = ' '.join([self.the_movie[1], '(' + str(self.the_movie[2]) + ')'])
            movie_picture = FindMoviePicture(temp)
            movie_picture.resize_poster()
            self.the_movie = self.the_movie[1]
        return [image, self.the_movie]

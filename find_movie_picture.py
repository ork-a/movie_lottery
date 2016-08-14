__author__ = 'Orka'
import urllib.request
from find_movie_length import FindMovieLength
import os
from resize_image import ResizeImage

class FindMoviePicture(object):
    def __init__(self, movie):
        self.movie = movie
        self.url = None
        self.image = None

    def search_picture_url(self):
        movie_url = FindMovieLength(self.movie).search_url()
        if movie_url != 'movie not found':
            with urllib.request.urlopen(movie_url) as HTML:
                html = HTML.read()
            html = str(html)
            cut = html.find("http://ia")
            html = html[cut:]
            cut = html.find('.jpg') + len('.jpg')
            if cut >= len('.jpg') and cut < 300:
                picture_url = html[:cut]
                url = picture_url[:picture_url.find('_V1') + len('_V1')] + '_.jpg'
                return url
            else:
                return 'No picture found...'
        else:
            return 'No movie found...'

    def clean_and_download(self):
        #remove previously downloaded file
        if os.path.isfile('temporary.jpg'):
            os.remove('temporary.jpg')
        #downloads image for current movie
        picture_url = self.search_picture_url()
        if picture_url == 'No picture found...' or picture_url == 'No movie found...':
            return picture_url
        else:
            self.image = urllib.request.urlretrieve(picture_url, 'temporary.jpg')

    def resize_poster(self):
        #choose picture
        pic_choice = self.clean_and_download()
        if pic_choice == 'No picture found...':
            my_picture = 'no_picture.jpg'
        elif pic_choice == 'No movie found...':
            my_picture = 'no_movie.jpg'
        else:
            my_picture = 'temporary.jpg'

        #remove previously resized file
        if os.path.isfile('resized.jpg'):
            os.remove('resized.jpg')

        #resize and save
        resized = ResizeImage(my_picture)
        resized_image = resized.resize_image()
        resized_image.save('resized.jpg')
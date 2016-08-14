__author__ = 'Orka'
#from tkinter import *
#from tkinter import ttk
from PIL import ImageTk, Image


class ResizeImage(object):
    def __init__(self, image):
        self.image = image

    def resize_image(self):
        #get the size of the image
        with Image.open(self.image) as im:
            width, height = im.size
            new_height = 500
            new_width = width/(height/new_height)
            size = int(new_width), int(new_height)

        #resize image
        original = Image.open(self.image)
        resized = original.resize(size, Image.ANTIALIAS)
        return resized
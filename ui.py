__author__ = 'Orka'

from tkinter import *
from tkinter import ttk
from main_movie_lottery import LaunchMovieLottery
from min_max_length import check_max_min_length
from check_input import check_input
from PIL import ImageTk, Image
from choose_display import ChooseDisplay


# remove unnecessary repeats (e.g. creating movie list twice!)
# add button for adding movies from the app, instead of editing .csv
# add button for updating the length of movies
# when saving, move movies with not found length at the beginning of the list for manual input
# find why the picture is not destroyed!
# add button "do you want to remove the movie from the list?)

class App(Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master, padding='5')
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.movie_name = ttk.Label()
        self.movie_picture = ttk.Label(image='')
        self.create_checkbox()
        self.my_state = 'disabled'
        self.create_entry()
        self.create_button()

    def create_checkbox(self):
        # self.limit = BooleanVar()
        self.check = Checkbutton(self,
                                 text='Limit movie length',
                                 height=2,
                                 width=18,
                                 command=self.state_update)
        self.check.grid(row=0, column=0, columnspan=2, sticky=N)

    def create_entry(self):
        self.entry_low = StringVar()
        self.entry_up = StringVar()

        self.low = Entry(self,
                         width=6,
                         textvariable=self.entry_low,
                         state=self.my_state)
        self.low.grid(row=1, column=0, sticky=E)

        self.up = Entry(self,
                        width=6,
                        textvariable=self.entry_up,
                        state=self.my_state)
        self.up.grid(row=1, column=1, sticky=W)

    def state_update(self):
        movie_list = LaunchMovieLottery().movie_list()
        minimum, maximum = check_max_min_length(movie_list[0])

        if self.my_state == 'disabled':
            self.my_state = 'normal'
            self.check.config(text='Limit movie length: \n' + str(minimum) + ' - ' + str(maximum))
        else:
            self.my_state = 'disabled'
            self.check.config(text='Limit movie length:')

        self.low.config(state=self.my_state)
        self.up.config(state=self.my_state)

    def get_entry(self):
        if self.low['state'] == 'normal':
            low_value, high_value = self.entry_low.get(), self.entry_up.get()
        else:
            low_value, high_value = None, None
        low_value, high_value = check_input(low_value, high_value)
        movie_lottery = LaunchMovieLottery(low_value, high_value)
        my_movie = movie_lottery.return_movie()  # returns movie as list
        self.display_movie_name_and_picture(my_movie)
        return (my_movie)

    def create_button(self):
        self.button = ttk.Button(self,
                                 text="Draw movie",
                                 width=12,
                                 command=lambda: self.get_entry()
                                 ).grid(column=0, row=2, columnspan=2, pady=10, sticky=N)

    def display_movie_name_and_picture(self, the_movie):
        self.movie_name.destroy()
        self.movie_picture.destroy()

        # choose display
        display = ChooseDisplay(the_movie)
        movie_info = display.choose_display()
        image, message = movie_info[0], movie_info[1]

        self.movie_name = ttk.Label(self, font=(None, 16), text=message)
        my_image = Image.open(image)
        poster = ImageTk.PhotoImage(my_image)
        display = ttk.Label(self, image=poster)
        display.my_image = poster

        # remove movie from the list and save
        movie_list = LaunchMovieLottery()
        movie_list.remove_and_save(the_movie)

        # display title and picture
        self.movie_name.grid(row=0, rowspan=2, column=3)
        display.grid(row=2, column=3, rowspan=3)


root = Tk()
root.title("Movie lottery")
root.geometry("550x575")
app = App(root)
root.mainloop()

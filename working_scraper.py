"""

import pandas as pd
from pandas import DataFrame
import requests
from google.colab import files
import tkinter as tk

page = requests.get("https://en.wikipedia.org/wiki/List_of_American_and_Canadian_cities_by_number_of_major_professional_sports_franchises").text
df = pd.read_html(page, flavor="bs4")[1]
print(df)
df.to_csv("sports_teams_city_state.csv", index=False)

files.download('sports_teams_city_state.csv')

"""


# GUI portion

import tkinter as tk
from tkinter import *
import pandas as pd
#from pandas import DataFrame
import requests
#from google.colab import files

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)  # create the canvas
canvas1.pack()

entry1 = tk.Entry(root)  # create the entry box
canvas1.create_window(150, 100, window=entry1)


def insert_number():  # add a function/command to be called by the button (i.e., button1 below)
    global x1  # add 'global' before the variable x1, so that you can use that variable outside of the command/function if ever needed
    x1 = str(entry1.get())  # store the data input by the user as a variable x1

    PATH = r'/Users/ryanpatton/CS361/sports_teams_city_state' + x1 + '.csv'
    read_cities = pd.read_csv(PATH)  # read the csv file using the 'PATH' varibale
    df = DataFrame(read_cities,
                   columns=['Metropolitan area', 'Country', 'Pop.rank', 'Population (2016 est.)[8]', 'B4', 'NFL', 'MLB', 'NBA', 'NHL', 'B6', 'MLS', 'CFL'])  # assign column names
    print(df)


button1 = tk.Button(root, text='Input City/State to import file', command=insert_number, bg='green',
                    fg='white')  # button to call the 'insert_number' command above
canvas1.create_window(150, 140, window=button1)

root.mainloop()
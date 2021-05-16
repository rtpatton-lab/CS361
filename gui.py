import pandas as pd
from pandas import DataFrame
import requests
import tkinter as tk
from tkinter import *

# GUI portion

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)  # create the canvas
canvas1.pack()

entry1 = tk.Entry(root)  # create the entry box
canvas1.create_window(150, 100, window=entry1)


def insert_text():  # add a function/command to be called by the button (i.e., button1 below)

    PATH = r'sports_teams_city_state.csv'
    read_cities = pd.read_csv(PATH)  # read the csv file using the 'PATH' variable
    df = read_cities.loc[read_cities['Metropolitan area'].isin(['Austin'])].values[0]
    #df = DataFrame(read_cities,
    #               columns=['Metropolitan area', 'Country', 'Pop.rank', 'Population (2016 est.)[8]', 'B4', 'NFL', 'MLB', 'NBA', 'NHL', 'B6', 'MLS', 'CFL'])  # assign column names
    print(df)


button1 = tk.Button(root, text='Input City/State to import file', command=insert_text, bg='green',
                    fg='white')  # button to call the 'insert_text' command above
canvas1.create_window(150, 140, window=button1)

root.mainloop()
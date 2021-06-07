import pandas as pd
from pandas import DataFrame
import requests
import tkinter as tk
from tkinter import *

# GUI portion

root = tk.Tk()

root.title("Sports Teams Searched by City")

# this section of code specifies the size of the terminal window,
# and the size of the data entry area and output area

root.geometry("300x300")

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

top_frame_entry = tk.Entry(root)
canvas1.create_window(150, 100, window=top_frame_entry)
top_frame_entry.pack(side="top", fill="x", padx=50, pady=10)

bottom_frame_entry = Frame(root, bg="grey")
bottom_frame_entry.pack(side="top", fill="x", padx=10, pady=10)


def insert_text():
    """
    this function reads csv file from working_scraper and creates functionality of GUI
    to interact with csv data
    """
    PATH = r'sports_teams_city.csv'
    read_cities = pd.read_csv(PATH)  # read the csv file using the 'PATH' variable
    df = read_cities.loc[read_cities['Metropolitan area'].isin(['Austin'])].values[0]
    #df = DataFrame(read_cities,
    #               columns=['Metropolitan area', 'Country', 'Pop.rank', 'Population (2016 est.)[8]', 'B4', 'NFL', 'MLB', 'NBA', 'NHL', 'B6', 'MLS', 'CFL'])  # assign column names
    print(df)


button1 = tk.Button(root, text='Input City/State to import file', command=insert_text, bg='green',
                    fg='white')  # button to call the 'insert_text' command above
canvas1.create_window(150, 140, window=button1)

scroll = Scrollbar(bottom_frame_entry)

answer = Text(bottom_frame_entry, font=("Arial", 18), fg="red",
              width=55, height=20, bd=5, yscrollcommand=scroll.set)
answer.pack(side="left", fill="y")
scroll.pack(side="left", fill="y")

lab = Label(frame,text=yourData)
lab.pack()

root.mainloop()
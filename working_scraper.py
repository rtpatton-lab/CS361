import pandas as pd
from pandas import DataFrame
import requests
import html5lib

page = requests.get("https://en.wikipedia.org/wiki/List_of_American_and_Canadian_cities_by_number_of_major_professional_sports_franchises").text
df = pd.read_html(page, flavor="bs4")[1]
print(df)
df.to_csv("sports_teams_city.csv", index=False) # sample comment for testing pushing



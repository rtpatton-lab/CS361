"""
# import package
import wikipedia

# specify title of page
wiki = wikipedia.page('Sports in the United States by state')

# extract the text
text = wiki.content
print(text)

import pandas as pd
import requests
from bs4 import BeautifulSoup

wikiurl = "https://en.wikipedia.org/wiki/List_of_American_and_Canadian_cities_by_number_of_major_professional_sports_franchises"
table_class = "wikitable sortable jquery-tablesorter"
response = requests.get(wikiurl)
print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
indiatable = soup.find('table', {'class':'wikitable'})

df = pd.read_html(str(indiatable))
df = pd.DataFrame(df[0])
print(df.head)
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_American_and_Canadian_cities_by_number_of_major_professional_sports_franchises"
resp = requests.get(url)

tables = pd.read_html(resp.text)

target = tables[1].iloc[:]
target

tables[0].to_csv("sports_teams_cities_states.csv")








import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import re

#get page
page = requests.get("https://nuernberg.digital/festival/programm")
#parse page
soup = BeautifulSoup(page.content, 'html.parser')

#get events details
event_names = soup.select('li.EventList__item .Card__text h3.EventCard__title')
event_names = [en.get_text() for en in event_names]

#konvert to panda Dataframe
events = pd.DataFrame({"Eventname": event_names})

print (events)



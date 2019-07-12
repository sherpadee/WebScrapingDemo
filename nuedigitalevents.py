import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import re
import matplotlib.pyplot as fig

#get page
page = requests.get("https://nuernberg.digital/festival/programm")
page.content

#parse page
soup = BeautifulSoup(page.content, 'html.parser')

#get events details
event_names = soup.select('li.EventList__item .Card__text h3.EventCard__title')
event_names = [en.get_text() for en in event_names]

event_dates = soup.select('li.EventList__item .Card__text div.EventCard__details .EventCard__details-date time[itemprop="startDate"] .daterange')
event_dates = [int(re.search(r'\d+', ed.get_text()).group()) for ed in event_dates]

event_times = soup.select('li.EventList__item .Card__text div.EventCard__details .EventCard__details-date')
event_times = [ed.get_text() for ed in event_times]

event_locations = soup.select('li.EventList__item .Card__text div.EventCard__details .EventCard__details-location')
event_locations = [el.get_text() for el in event_locations]

#event_url = soup.select('li.EventList__item .Card__text a[itemprop="url"]')
#event_url = ['https://nuernberg.digital'+eu['href'] for eu in event_url]

#konvert to panda Dataframe
events = pd.DataFrame({
"Eventname": event_names,
"Datum": event_dates,
"Uhrzeit": event_times,
"Location" : event_locations
#,"url": event_url
})

allevents = events.sort_values(by=['Datum','Uhrzeit'])
allevents = allevents.drop_duplicates()
allevents = allevents.drop_duplicates(subset='Eventname', keep='first')
allevents['Zeile'] = allevents.reset_index().index

 #print events
print(tabulate(allevents, headers='keys', tablefmt='grid'))
print ("Total: {0} Events".format(len(allevents)))

#todays events
events =  events.loc[events['Datum'] == 16]
events = events.sort_values(by=['Datum','Uhrzeit'])
events['Zeile'] = events.reset_index().index

print(tabulate(events, headers='keys', tablefmt='grid'))
print ("Total: {0} Events".format(len(events)))

#events per day
counts = pd.DataFrame(allevents.groupby('Datum').size().rename('Anzahl'))
print(tabulate(counts, headers='keys', tablefmt='grid'))

plot = counts.plot(kind="bar",  title= 'Nürnberg Digital Festival 2019 - Events', figsize=[10, 6])
fig = plot.get_figure()
fig.savefig("events.png", transparent=True)
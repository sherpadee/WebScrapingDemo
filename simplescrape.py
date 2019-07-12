#Data : https://de.wikipedia.org/wiki/Liste_der_L%C3%A4nder_nach_Internetnutzern
#

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

res = requests.get("https://de.wikipedia.org/wiki/Liste_der_L%C3%A4nder_nach_Internetnutzern")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))
print( tabulate(df[0], headers='keys', tablefmt='psql') )

with open('InternetUsersWorldWide.json', encoding='utf-8', mode='w') as file:
    df[0].to_json(file, force_ascii=False)
    file.close()

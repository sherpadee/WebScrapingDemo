
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
import re

#get page
page = requests.get("https://nuernberg.digital/festival/programm")
#parse page
soup = BeautifulSoup(page.content, 'html.parser')
print(page.content)


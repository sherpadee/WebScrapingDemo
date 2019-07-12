from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import re
import pandas as pd
from tabulate import tabulate
import os

#launch url
url = "http://kanview.ks.gov/PayRates/PayRates_Agency.aspx"

options = Options()
options.headless = True

# create a new Firefox session
driver = webdriver.Firefox(options=options ) #, executable_path=r'C:\Utility\BrowserDrivers\geckodriver.exe'))
driver.implicitly_wait(30)
driver.get(url)

#After opening the url above, Selenium clicks the specific agency link
python_button = driver.find_element_by_id('MainContent_uxLevel1_Agencies_uxAgencyBtn_33') #FHSU
python_button.click() #click fhsu link

#Selenium hands the page source to Beautiful Soup
soup_level1 = BeautifulSoup(driver.page_source, 'html.parser')

datalist = [] #empty list
x = 0 #counter

#Beautiful Soup finds all Job Title links on the agency page and the loop begins
for link in soup_level1.find_all('a', id=re.compile("^MainContent_uxLevel2_JobTitles_uxJobTitleBtn_")):
    
    #Selenium visits each Job Title page
    python_button = driver.find_element_by_id('MainContent_uxLevel2_JobTitles_uxJobTitleBtn_' + str(x))
    python_button.click() #click link
    
    #Selenium hands of the source of the specific job page to Beautiful Soup
    soup_level2=BeautifulSoup(driver.page_source, 'html.parser')

    #Beautiful Soup grabs the HTML table on the page
    table = soup_level2.find_all('table')[0]
    
    #Giving the HTML table to pandas to put in a dataframe object
    df = pd.read_html(str(table),header=0)
    
    #Store the dataframe in a list
    datalist.append(df[0])
    
    #Ask Selenium to click the back button
    driver.execute_script("window.history.go(-1)") 
    
    #increment the counter variable before starting the loop over
    x += 1
    
    #end loop block
    
#loop has completed

#end the Selenium browser session
driver.quit()

#combine all pandas dataframes in the list into one big dataframe
result = pd.concat([pd.DataFrame(datalist[i]) for i in range(len(datalist))],ignore_index=True)

#convert the pandas dataframe to JSON
json_records = result.to_json(orient='records')

#pretty print to CLI with tabulate
#converts to an ascii table
print(tabulate(result, headers=["Employee Name","Job Title","Overtime Pay","Total Gross Pay"],tablefmt='psql'))

print(tabulate(result["Total Gross Pay"].argmax(), headers=["Employee Name","Job Title","Overtime Pay","Total Gross Pay"],tablefmt='psql'))

#get current working directory
#path = os.getcwd()

#open, write, and close the file
f = open( "fhsu_payroll_data.json","w") #FHSU
f.write(json_records)
f.close()

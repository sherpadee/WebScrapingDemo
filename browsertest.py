from selenium import webdriver
import time
import os

ext = ''
if os.name == 'nt':
    ext = '.exe'

cwd = os.getcwd()
##edge (windows only)
#browser = webdriver.Edge(executable_path = cwd +'/msedgedriver' + ext)
#browser.get('https://www.google.com') 
#time.sleep(5)
#browser.quit()

##firefox
browser = webdriver.Firefox(executable_path = cwd + '/geckodriver' + ext)
browser.get('https://www.google.com') 
time.sleep(5)
browser.quit()

##chrome
browser = webdriver.Chrome(executable_path = cwd + '/chromedriver' + ext)
browser.get('https://www.google.com') 
time.sleep(5)
browser.quit()

##safari (osx only)
#browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')    
#browser.get('https://www.google.com')
#time.sleep(5)
#browser.quit()


browser = webdriver.Chrome(executable_path = cwd + '/chromedriver' + ext)
browser.get('https://nuernberg.digital/festival/jobboerse') 
time.sleep(1)
total_width = browser.execute_script("return document.body.offsetWidth")
total_height = browser.execute_script("return document.body.scrollHeight")
browser.set_window_size(total_width, total_height)
browser.save_screenshot("nuedigital.png")
#alternate method
#site = browser.find_element_by_tag_name('body')
#site.screenshot('nuedigital.png')
cookie_ok_button= browser.find_element_by_class_name('CallToAction.CallToAction--primary')
cookie_ok_button.click()
site = browser.find_element_by_class_name('JobList')
site.screenshot('nuedigitaljobs.png')
browser.quit()
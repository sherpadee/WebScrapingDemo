from selenium import webdriver
import time

##edge (windows only)
#browser = webdriver.Edge(executable_path = './msedgedriver')
#browser.get('https://www.google.com') 
#time.sleep(5)
#browser.quit()

##firefox
browser = webdriver.Firefox(executable_path = './geckodriver')
browser.get('https://www.google.com') 
time.sleep(5)
browser.quit()

##chrome
browser = webdriver.Chrome(executable_path = './chromedriver')
browser.get('https://www.google.com') 
time.sleep(5)
browser.quit()

##safari (osx only)
#browser = webdriver.Safari(executable_path = '/usr/bin/safaridriver')    
#browser.get('https://www.google.com')
#time.sleep(5)
#browser.quit()

import unittest

class ChromeBrowserTest(unittest.TestCase):

    chrome_browser = None
    page_url = ''

    # Class setup method.
    @classmethod
    def setUpClass(cls):
        ChromeBrowserTest.chrome_browser = webdriver.Chrome(executable_path = './chromedriver')
        print('Browser start.')

    # Class teardown method
    @classmethod
    def tearDownClass(cls):
        if(ChromeBrowserTest.chrome_browser!=None):
            ChromeBrowserTest.chrome_browser.quit()
            print('Browser quit.')
        else:
            print('Browser is not started.')   
    
    # This is the test function.    
    def browse_page(self):
        if(self.chrome_browser!=None and len(self.page_url)>0):
            self.chrome_browser.get(self.page_url)
            print("Browser browse page.")
            time.sleep(10)
        else:
            print('Browser is not started or page_url is empty.')       

if __name__ == '__main__':
    ChromeBrowserTest.page_url = 'https://www.google.com'
    # Create a TestSuite object.
    test_suite = unittest.TestSuite()

    # Add test function in the suite.
    test_suite.addTest(ChromeBrowserTest('browse_page'))

    # Run test suite and get test result.
    testResult = unittest.TestResult()
    
    test_suite.run(testResult)
    print(testResult)

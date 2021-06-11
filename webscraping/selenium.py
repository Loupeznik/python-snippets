from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

'''
Snippet for basic webscraping with selenium
'''

## DRIVER SETUP ##
options = Options()
options.headless = True
DRIVER_PATH = '/opt/webdriver/chromedriver' # Path to your chromedriver binary
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

## SCRAPER FLOW ##
driver.get('https://yourpage.com')

# Wait until the page loads completely
try:
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, 'element_xpath')))
except TimeoutException:
    print('Timed out waiting for page to load')
    driver.quit()

# Scrape the desired element
element = driver.find_element_by_xpath('element_xpath')
print(element)

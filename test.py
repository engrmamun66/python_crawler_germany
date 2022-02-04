import imp
from math import ceil
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


open_browser = False

if not open_browser:     
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    ser = Service("chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=options)


driver.get('https://www.youtube.com/results?search_query=Autofinanzierung')
time.sleep(5)
contents = driver.find_elements(By.TAG_NAME, 'h3')
for each in contents:    
    print(each.text)






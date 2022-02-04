from ast import keyword
from json.tool import main
from posixpath import islink
from sqlite3 import TimeFromTicks
from tkinter import Grid
from warnings import catch_warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import datetime
import time
import random
import string
import re


#google_link_list = [] , google_title_list = [] , google_price_list = [] , google_anbieter_list = [] , youtube_link_list = [] , youtube_title_list = [] , youtube_price_list = [] , youtube_seller_list = [] ,

def read_ads(input_keyword, open_browser=False):
    screen_id = random.randint(1, 9999999999)
    screen_id = random.choice(string.ascii_letters) + random.choice(
        string.ascii_letters) + str(screen_id) + random.choice(string.ascii_letters)
    stamp = str(datetime.now().strftime('%H_%M_%S %Y_%m_%d'))
    # setup input and outputs
    google_link_list = []
    google_title_list = []
    google_price_list = []
    google_anbieter_list = []
    google_ident_list = []
    youtube_link_list = []
    youtube_title_list = []
    youtube_price_list = []
    youtube_seller_list = []
    youtube_ident_list = []
    brand_list = []
    rank_list = []
    id_list = []
    rank = 0


    
    if not open_browser:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        ser = Service("chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=ser, options=options)
    else:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

    # =======================================
    # =======================================
    # ========== WITH YOUTUBE ===============
    # =======================================
    # =======================================
    driver.get(
        "https://www.youtube.com/results?search_query={}".format(input_keyword))
    # content = driver.page_source.encode('utf-8').strip()
    # soup = BeautifulSoup(content, 'lxml')

    # ==================================
    # =========== Youtube Textanzeige Ad
    # ==================================
    # https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium
    if 1:

        #contents = soup.find_all('div', id='sparkles-body')
        print('---------------------------------------------------------------')
        myContents = driver.find_elements_by_id('contents')

        print('-----step::1')
        print(myContents)
   
       

        # rank = 0
        # for eachBlock in contents:
        #     print(
        #         f'--{input_keyword}----------------------------------------------------------------------------')
        #     block = eachBlock.find('div', id='contents')
        #     title = (block.find('h3').get_text())
        #     print(block.find('div', id='website-text').get_text())

        # print(block.find('div', id='sparkles-container').find('h3').get_text())

        # try:
        #     link1 = block.find('div', id='website-text').get_text()
        # except:
        #     link1 = ''
        # try:
        #     link2 = block.find('div', id='display-url').get_text()
        # except:
        #     link2 = ''

        # link = link1 + link2 #

        # try: title = block.find('h3', id='title').get_text()
        # except: title = ''

        # print( f"=============Youtube Textanzeige Ad===============\nlink : {link}\nTitle : {title}\nAnbieter : {nlink}\nkeyword: {input_keyword}")




    # close web driver
    driver.close()
    # setup output
    output = [google_link_list, google_title_list, google_price_list, google_anbieter_list, brand_list, google_ident_list, stamp,
              id_list, rank_list, youtube_link_list, youtube_title_list, youtube_price_list, youtube_seller_list, youtube_ident_list]
    #print(output)
    print([len(google_link_list), len(google_title_list), len(google_price_list), len(google_anbieter_list), len(
        brand_list), len(google_ident_list), len(youtube_price_list), len(youtube_seller_list), ])
    return output


if __name__ == "__main__":
    read_ads("Autofinanzierung")

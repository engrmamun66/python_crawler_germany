from ast import keyword
from posixpath import islink
from sqlite3 import TimeFromTicks
from warnings import catch_warnings
from selenium import webdriver
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


    def getPriceFromTitle(title=''):
        myTitle = title.strip().replace('    ', '   ').replace('   ', '  ').replace(
        '  ', ' ').replace(' €', '€').replace('*, \d', ',\d')
        result = ''
        if('€' in myTitle):
            for x in myTitle.split():
                if('€' in x):
                    result = x            
        return result


    # open_browser = 1
    if not open_browser:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(
            'chromedriver_win32/chromedriver.exe', options=options)
    else:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

    # =======================================
    # =======================================
    # ========== WITH GOOGLE ================
    # =======================================
    # =======================================
    driver.get("https://www.google.de/search?q={}".format(input_keyword))
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')

    # ==============================
    # =========== Google Shopping Ad
    # ============================== 
    if 1:
        contents = soup.find_all('div', class_='mnr-c pla-unit')
        rank = 0
        for eachBlock in contents:
            try:            
                link = eachBlock.find('div', class_='ropLT').find('a')['href']
            except: link = ''

            try: title = eachBlock.find('div', class_='r4awE').get_text()
            except: title = '' 

            # try: price = eachBlock.find('span', class_='e10twf').get_text()
            try: price = eachBlock.find('span', text=re.compile(".*€.*")).get_text()
            except:
                price = '€0.00'

            try: anbieter = eachBlock.find('div', class_='LbUacb').find('span').get_text()
            except: anbieter = ''

            try: ident_von = eachBlock.find('div', class_='Qp6aMc').get_text()
            except: ident_von = ''

            print(f"=============Google Shopping Ad===============\nlink : {link}\nTitle : {title}\nPrice : {price}\nAnbieter : {anbieter}\nident_von : {ident_von}\keyword: {input_keyword}")

            if(
                # len(link) and link[0:4] == 'http'and 
                len(title)
               and len(price)
               and len(anbieter)
               and len(ident_von)
               ):
                rank += 1
                rank_list.append(str(rank))
                google_link_list.append(str(link))
                google_title_list.append(str(title))
                google_price_list.append(price)
                google_anbieter_list.append(str(anbieter))
                brand_list.append(str(ident_von))
                google_ident_list.append("Google Shopping Ad")
                id_list.append(str(screen_id) + "_g")


    # =================================
    # =========== Google Textanzeige Ad
    # =================================
    if 1:
        contents = soup.find_all('div', class_='uEierd')
        rank = 0
        for eachBlock in contents:
            try: link = eachBlock.find('span', role="text").get_text()
            except: link = ''        

            try: title = eachBlock.find('div', role='heading', class_='CCgQ5').find('span').get_text() #Note: may be change class_ name
            except: title=''            

            try: 
                price = getPriceFromTitle(title)
            except: price=''            

            try: anbieter = eachBlock.find('div', class_='v5yQqb').find('a')['href'] 
            except: anbieter = link
            
            print(f"=============Google Textanzeige Ad===============\nlink : {link}\nTitle : {title}\nPrice : {price}\nAnbieter : {anbieter}\nkeyword: {input_keyword}")

            if(len(link) and link[0:4] == 'http'
            and len(title) 
            and len(anbieter) 
            and anbieter[0:4] == 'http'
            ):
                rank += 1
                rank_list.append(str(rank))
                google_link_list.append(str(link))
                google_title_list.append(str(title))
                google_price_list.append(str(price))
                google_anbieter_list.append(str(anbieter))
                google_ident_list.append("Google Textanzeige")
                id_list.append(str(screen_id) + "_g")







    # =======================================
    # =======================================
    # ========== WITH YOUTUBE ===============
    # =======================================
    # =======================================
    driver.get("https://www.youtube.com/results?search_query={}".format(input_keyword))
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')


    # ==================================
    # =========== Youtube Textanzeige Ad
    # ==================================
    if 1:
        contents = soup.find_all('div', class_='uEierd')
        rank = 0
        for eachBlock in contents:
            pass









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
    read_ads("sommerreifen")

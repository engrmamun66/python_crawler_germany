from ast import keyword
from posixpath import islink
from sqlite3 import TimeFromTicks
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
        ser = Service("chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=ser, options=options)
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
    if 0:
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


            if(
            len(link) and link[0:4] == 'http'
            and len(title)
            and len(price)
            and len(anbieter)
            and len(ident_von)
               ):
                print(f"=============Google Shopping Ad===============\nlink : {link}\nTitle : {title}\nPrice : {price}\nAnbieter : {anbieter}\nident_von : {ident_von}\keyword: {input_keyword}")
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
    if 0:
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
            

            if(
            len(link) and link[0:4] == 'http'
            and len(title) 
            and len(anbieter) 
            and anbieter[0:4] == 'http'
            ):
                print(f"=============Google Textanzeige Ad===============\nlink : {link}\nTitle : {title}\nPrice : {price}\nAnbieter : {anbieter}\nkeyword: {input_keyword}")
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
    youtube_content = driver.page_source.encode('utf-8').strip()
    youtube_soup = BeautifulSoup(youtube_content, 'lxml')
    # print(youtube_soup)
    


    # ==================================
    # =========== Youtube Textanzeige Ad
    # ==================================
    if 1:
        print('I am here.')
        # youtube_contents = youtube_soup.find_all('div', class_='contents')

        # youtube_contents = youtube_soup.find_all('div', class_='style-scope ytd-item-section-renderer sparkles-light-cta')
        youtube_contents = youtube_soup.find_all('div', class_='style-scope ytd-section-list-renderer')
        # youtube_contents = youtube_soup.find_all('ytd-item-section-renderer', class='style-scope ytd-section-list-renderer')
        # youtube_contents = youtube_soup.find_all('ytd-item-section-renderer', class_='style-scope ytd-section-list-renderer')
        print(len(youtube_contents))
        print(youtube_contents)

        # if youtube_contents != None:
        #     for i in youtube_contents:
        #         if i.get_attribute('class') == "style-scope ytd-section-list-renderer":
        #             youtube_contents = i
        #             break
        # print(len(youtube_contents))
        # rank = 0
        # for eachBlock in youtube_contents:

        # for i in youtube_contents.find_elements_by_xpath("./*"):
            # print('i am in loop')
            # try: link = eachBlock.find('span', role="text").get_text()
            # except: link = ''

            # try: title = eachBlock.find('div', class_='style-scope ytd-promoted-sparkles-web-renderer').find('h3').get_text()
            # try: title = eachBlock.find('h3', id='title').get_text()
            # try: title = i.find_element_by_xpath('//h3[@id="title"]').text
            # try: title = eachBlock.find_element_by_xpath('//h3[@id="title"]').text
            # except: title=''

            # print("title: "+str(title))

        # additional_ad_elements = driver.find_elements_by_id("contents")
        # if additional_ad_elements != None:
        #     for i in additional_ad_elements:
        #         if i.get_attribute('class') == "style-scope ytd-section-list-renderer":
        #             additional_ad_elements = i
        #             break
        #     rank = 0
        #     for i in additional_ad_elements.find_elements_by_xpath("./*"):
        #         try:
        #             title = i.find_element_by_xpath('//h3[@id="title"]').text
        #         except : title = ''
        #         print("title: "+str(title))

    if 0:
        # contents = soup.findAll('div', id='contents')[1].find_all('div', id='contents').find_all('div', id='sparkles-container
        # contents = soup.findAll( id='contents', limit=1) #working
        contents = soup.find_all('div', id='sparkles-container')
        print((contents))
        # print('len(contents)')
        # print(len(contents))

        rank = 0
        for eachBlock in contents:
            print(f'--{input_keyword}----------------------------------------------------------------------------')
            block = eachBlock.find('div', id='contents')
            title = (block.find('h3').get_text())
            print(block.find('div', id='website-text').get_text())

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
    read_ads("sommerreifen")

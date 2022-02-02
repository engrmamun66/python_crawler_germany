from ast import keyword
from warnings import catch_warnings
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import time
import random
import string

#google_link_list = [] , google_title_list = [] , google_price_list = [] , google_seller_list = [] , youtube_link_list = [] , youtube_title_list = [] , youtube_price_list = [] , youtube_seller_list = [] ,


def read_ads(input_keyword, open_browser=False):
    screen_id = random.randint(1, 9999999999)
    screen_id = random.choice(string.ascii_letters) + random.choice(
        string.ascii_letters) + str(screen_id) + random.choice(string.ascii_letters)
    stamp = str(datetime.now().strftime('%H_%M_%S %Y_%m_%d'))
    # setup input and outputs
    google_link_list = []
    google_title_list = []
    google_price_list = []
    google_seller_list = []
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

    # open_browser = 1
    if not open_browser:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(
            'chromedriver_win32/chromedriver.exe', options=options)
    else:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

    # ===== WITH GOOGLE
    driver.get("https://www.google.de/search?q={}".format(input_keyword))
    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')

    # =========== Google Text Ad
    contents = soup.find_all('div', class_='uEierd')

    for eachBlock in contents:
        try: link = eachBlock.find('span', role="text").get_text()
        except: link = ''        

        try: title = eachBlock.find('div', role='heading', class_='CCgQ5').find('span').get_text() #Note: may be change class_ name
        except: title=''

        try: Anbieter = eachBlock.find('div', class_='v5yQqb').find('a')['href'] 
        except: Anbieter = link
        
        print(f"link : {link}\nTitle : {title}\nAnbieter : {Anbieter}")

   

    # close web driver
    driver.close()
    # setup output
    output = [google_link_list, google_title_list, google_price_list, google_seller_list, brand_list, google_ident_list, stamp,
              id_list, rank_list, youtube_link_list, youtube_title_list, youtube_price_list, youtube_seller_list, youtube_ident_list]
    #print(output)
    print([len(google_link_list), len(google_title_list), len(google_price_list), len(google_seller_list), len(
        brand_list), len(google_ident_list), len(youtube_price_list), len(youtube_seller_list), ])
    return output


if __name__ == "__main__":
    read_ads("sommerreifen")

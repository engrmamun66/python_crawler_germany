# Supreme bot SBV1 with Selenium
from audioop import add
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from datetime import datetime 
import time
import random
import string

#google_link_list = [] , google_title_list = [] , google_price_list = [] , google_seller_list = [] , youtube_link_list = [] , youtube_title_list = [] , youtube_price_list = [] , youtube_seller_list = [] ,


def read_ads(input_keyword,driver):
    screen_id = random.randint(1,9999999999)
    screen_id = random.choice(string.ascii_letters)+ random.choice(string.ascii_letters) + str(screen_id) + random.choice(string.ascii_letters)
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
    #options.add_argument('headless')
    driver.set_window_size(700, 1080) # set window size to 700*1080 pixel

    # CRAWL YOUTUBE -------------------------------------------------------------------------------------------------------------------------
    # navigate to Youtube website and click away the windows
    driver.get("https://www.youtube.com/results?search_query={}".format(input_keyword))
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button'))).click()
        # just in case but doesnt have to be clicked when already clicked from by the google crawl
        #WebDriverWait(driver,5).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://consent.google.com']")))
        #WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"///*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button/span"))).click()
        pass
    except Exception as e:
        pass
    driver.switch_to.default_content()

    # Youtube Shopping Ad
    # finding the ad section on the website if nothing found return empty lists
    # ad_elements = None
    # trys_youtube = 10 # number of tries to receive a result with ads
    # while True:
    #     if trys_youtube <= 0: break
    #     trys_youtube -= 1
    #     try:
    #         time.sleep(1)
    #         ad_elements_list = driver.find_element_by_id("items")
    #         print(f"---->>>>>>>>>>>>>>> Reached Here-0")
    #         for i in ad_elements_list: 
    #             # style-scope ytd-item-section-renderer
    #             if i.get_attribute('class') == "style-scope yt-horizontal-list-renderer": 
    #                 ad_elements = i
    #                 break
    #     except Exception as err: 
    #         print(f"---->>>>>>>>>>>>>>> Reached Here-00")           
    #         pass
    if 1:

        try:
            searchbar.send_keys(Keys.RETURN)
        except Exception as e:
            pass

        ad_elements_list = driver.find_element_by_id("items")

        time.sleep(5)
        ad_elements = ad_elements_list.find_elements_by_css_selector("[class='style-scope yt-horizontal-list-renderer']")
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> --- Youtube Shopping Ad'+ str(len(ad_elements)))

        _except = lambda param: '__not-found: res_'+ str(param)

        for i in ad_elements:
            print("Youtube Shopping Ad")
            try:
                res_1 = i.find_element_by_css_selector("[id='title-link']").get_attribute("href")
            except:
                res_1 =_except(1)

            try:
                res_2 = i.find_element_by_css_selector("[id='title-text']").get_attribute("title")
                res_3 = i.find_element_by_css_selector("[id='secondary-text']").get_attribute("title")
                res_4 = i.find_element_by_css_selector("[id='body-text']").get_attribute("title")
            except:
                res_2 =_except(1)

            try:
                res_3 = i.find_element_by_css_selector("[id='secondary-text']").get_attribute("title")
                res_4 = i.find_element_by_css_selector("[id='body-text']").get_attribute("title")
            except:
                res_3 =_except(1)

            try:
                res_4 = i.find_element_by_css_selector("[id='body-text']").get_attribute("title")
            except:
                res_4 =_except(1)

            # only add the results to the lists when all information was read properly
            rank += 1
            rank_list.append(rank)
            google_link_list.append(res_1)
            google_title_list.append(res_2)
            google_price_list.append(res_3)
            google_seller_list.append(res_4)
            google_ident_list.append("Youtube Shopping Ad")
            id_list.append(screen_id + "_yt")
            print("Yotube ad")


    # close web driver
    driver.close()
    # setup output
    output = [google_link_list, google_title_list, google_price_list, google_seller_list,brand_list, google_ident_list ,stamp , id_list, rank_list, youtube_link_list, youtube_title_list, youtube_price_list, youtube_seller_list, youtube_ident_list]
    print(output)
    print([len(google_link_list),len(google_title_list),len(google_price_list),len(google_seller_list),len(brand_list),len(google_ident_list),len(youtube_price_list),len(youtube_seller_list),])
    return output





if __name__ == "__main__":
    PATH = "chromedriver_win32/chromedriver.exe" #  path to chrome driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(executable_path=PATH, chrome_options=options)
    read_ads("Gaming PC",driver)
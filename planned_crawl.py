from tkinter import *
from datetime import datetime
import crawler_arnav_dont_touch
import xlsxwriter
from selenium import webdriver
import os


def crawl(keyword,driver):
    return crawler_arnav_dont_touch.read_ads(keyword,driver)

def safe(results):
    time_now = str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
    workbook = xlsxwriter.Workbook('crawl_' + time_now + '.xlsx')
    stopwords = open("stopwords.txt")
    stopwords = stopwords.readlines()
    worksheet = workbook.add_worksheet("Crawlresults")
    #worksheet = workbook.add_worksheet("Anleitung")
    worksheet.write('A1', "Screen ID")# google result
    worksheet.write('B1', "Rank")# google result
    worksheet.write('C1', "Datum/Uhrzeit")# google result
    worksheet.write('D1', "Keyword")# google result
    worksheet.write('E1', "Link")# google result
    worksheet.write('F1', "Titel")# google result
    worksheet.write('G1', "Preis")# youtube result
    worksheet.write('H1', "Anbieter")# youtube result
    worksheet.write('I1', "Ad Anbieter")# youtube result
    worksheet.write('J1', "Ad Type")# youtube result
    #print("--------------------------------------", len(result))
    zahl = 1
    for i, (keyword, result) in enumerate(results.items()):
        for j in range(0, len(result[0])):
                stopword = 0
                for word in stopwords: 
                    if word in result[0][j] or word in result[3][j]:
                        print("stopword-----------")
                        stopword = 1
                        zahl -=1
                        break
                    else:
                        continue
                zahl +=1
                if stopword == 0:
                    try:
                        print(zahl)
                        worksheet.write('A{}'.format(zahl), result[7][j]) # screen id
                        worksheet.write('B{}'.format(zahl), result[8][j])# rank
                        worksheet.write('C{}'.format(zahl), result[6]) #datum uhrzeit
                        worksheet.write('D{}'.format(zahl), keyword) #datum uhrzeit
                        worksheet.write('E{}'.format(zahl), result[0][j])# google result
                        worksheet.write('F{}'.format(zahl), result[1][j])# google result
                        worksheet.write('G{}'.format(zahl), result[2][j])# google result
                        worksheet.write('H{}'.format(zahl), result[3][j])# google result
                        worksheet.write('J{}'.format(zahl), result[5][j])# google ident result
                        worksheet.write('I{}'.format(zahl), result[4][j])# Von Google / ..
                        

                        
                        
                        #print(results[5][j])
                        ''' V2 not needed
                        if j < len(result[5]):
                            worksheet.write('H{}'.format(j+1), j+1)# rank
                        worksheet.write('I{}'.format(j+1), result[5][j])# youtube result
                        worksheet.write('J{}'.format(j+1), result[6][j])# youtube result
                        worksheet.write('K{}'.format(j+1), result[7][j])# youtube result
                        worksheet.write('L{}'.format(j+1), result[8][j])# youtube result
                        worksheet.write('M{}'.format(j+1), result[9][j])# youtube result
                        '''
                    except:
                        continue
    workbook.close()
    return

try:
    # Directory
    directory = "Webcrawler"
    # Parent Directory path
    parent_dir = "C:/"
    # Path
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
except:
    pass
    
try:
    # Directory
    directory = "Screens"
    # Parent Directory path
    parent_dir = "C:/Webcrawler"
    # Path
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
except:
    pass

keywords = open(r'keywords.txt','r', encoding='utf8') 
results = {}
for keyword in keywords.readlines():
        PATH = "chromedriver_win32/chromedriver.exe" #  path to chrome driver
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        driver = webdriver.Chrome(executable_path=PATH, chrome_options=options)
        try:
            results[keyword] = crawler_arnav_dont_touch.read_ads(keyword,driver)
            '''if len(results[keyword][0]) > 0:         debug
                break'''
        except Exception as e:
            driver.close()
            pass
safe(results)


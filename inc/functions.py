from sqlite3 import TimeFromTicks


def isAd(text):
    return "Ad " in text or "VISIT SITE" in text


def exclude(line):
    if 'Showing results' in line: line = ''
    return line

def titleCleaner(title):
    alphabets = 'zxcvbnm,./asdfghjkl;\\qwertyuiop[]1234567890-=!#%^&*()_+QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?'
    title = title.replace("VISIT SITE", "")
    title = title.replace("[4", "")
    title = title.replace("[erty", "")
    title = title.replace("[erty", "")
    title = title.replace("    ", " ")
    title = title.replace("   ", " ")
    title = title.replace(" ", " ")
    title = title.replace("®", " ")
    title = title.split('...')[0]
    title = title.lstrip(" -“@!~$%^&*(){}[]\"'|\\/?<,>.`+*©")
    title = title.rstrip(" -“@!~$%^&*(){}[]\"'|\\/?<,>.`+*©")
    return title

def getTitle(text):
    arr = text.split('\n')
    title = ''
    for line in arr:
        line = exclude(line)
        line = line.lstrip('@ ')
        if('Ad' in line): break
        title += " " + line
    theTitle = title.split('Visit')[0]
    return titleCleaner(theTitle)

def getLink(text):
    arr = text.split('\n')
    title = ''
    url = ''
    for line in arr:
        if('http' in line): 
            for word in line.split(" "):               
                if 'http' in word:
                    url = word
                    break
    return url.strip()


def getPrice(text):
    arr = text.split('\n')
    title = ''
    url = ''
    for line in arr:
        if('http' in line): 
            for word in line.split(" "):               
                if 'http' in word:
                    url = word
                    break
    return url.strip()

   
def readAds(text):
    ads = []
    singleAd = ''
    for line in text.split('\n'):
        singleAd += '\n' + line
        if "http" in line:
            ads.append(singleAd)
            singleAd = ''
 
    c = len(ads)
    print(f"------------------------------\n\nTotle ad is : {c}")
    return ads;

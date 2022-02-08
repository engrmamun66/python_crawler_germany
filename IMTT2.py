
from typing import Iterator
from inc.withimage import imgtotext
from inc.functions import isAd, readAds, getTitle, getLink



imgMap_1 = "190:1500, 0:1500"

imageText = imgtotext(imagename='try-6.png', image_index=1,
                      positionMap=imgMap_1, showimage=False, printText=False)
if isAd(imageText):    
    ads = readAds(imageText)
    if len(ads):
        for ad in ads:
            title = getTitle(ad)
            link = getLink(ad)
            print(f'\nTitle: {title}\nLink: {link}\n')
else: 
    print(f'This is not an add !!!')
    pass


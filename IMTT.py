# https://pysource.com/2020/04/23/text-recognition-ocr-with-tesseract-and-opencv/
#pip install opencv-python
#pip install numpy
#pip install pytesseract
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 1. Load the image
img = cv2.imread("bg.jpg")
text = pytesseract.image_to_string(img)
print(text)

# cv2.imshow('Img', img)
# cv2.waitKey(0)
# https://stackoverflow.com/questions/37745519/use-pytesseract-ocr-to-recognize-text-from-an-image
# #

import cv2
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread("pic_1644164401.jpg", 1)
# image = cv2.imread("sample4.jpg", 1)
cv2.imshow('image', image)
cv2.waitKey()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.waitKey()
blur = cv2.GaussianBlur(gray, (3,3), 0)
cv2.imshow('blur', blur)
cv2.waitKey()
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow('thresh', thresh)
cv2.waitKey()

# Morph open to remove noise and invert image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
cv2.imshow('opening', opening)
cv2.waitKey()
invert = 255 - opening

# Perform text extraction
data = pytesseract.image_to_string(invert, lang='eng', config='-c tessedit_char_whitelist=0123456789 --psm 6')
print(data)

cv2.imshow('thresh', thresh)
cv2.imshow('opening', opening)
cv2.imshow('invert', invert)
cv2.waitKey()

#import cv2
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("pic_1644164401.jpg")  # img is the path of the image 
im = im.convert("RGBA")
#cv2.imshow('RGBA', im)
#cv2.waitKey()
newimdata = []
datas = im.getdata()

for item in datas:
    if item[0] < 112 or item[1] < 112 or item[2] < 112:
        newimdata.append(item)
    else:
        newimdata.append((255, 255, 255))
im.putdata(newimdata)
#cv2.imshow('im', im)
#cv2.waitKey()

im = im.filter(ImageFilter.MedianFilter())
#cv2.imshow('MedianFilter', im)
#cv2.waitKey()
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
#cv2.imshow('Contrast', im)
#cv2.waitKey()
im = im.convert('1')
#cv2.imshow('1', im)
#cv2.waitKey()
# im.save('temp2.jpg')
text = pytesseract.image_to_string(im,config='-c tessedit_char_whitelist=0123456789 --psm 6', lang='eng')
print(text)
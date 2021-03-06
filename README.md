# OpenCV
## Installation
Verwende Python3 als Standard:
```
sudo apt-get install python-is-python3
```
Evtl python2 entfernen (noch nicht gemacht):
https://askubuntu.com/questions/1242702/how-to-remove-python-2-from-ubuntu-20-04

## pip3
```
sudo apt install python3-pip
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1
```
update pip (als normaler User):
```
pip install -U pip
```
OCR https://www.geeksforgeeks.org/license-plate-recognition-with-opencv-and-tesseract-ocr/?ref=lbp
```
pip install pytesseract
pip install opencv-python
sudo apt-get install tesseract-ocr tesseract-ocr-deu 

cd ~/Software/OpenCV/detecting-and-ocring-digits
python ocr_digits.py --image apple_support.png
```
## display_ocr
https://github.com/arturaugusto/display_ocr

Nice programm to change OCR parameters and see the effect immediately. (Slider for "Filter" not used in code ...)

Copied `letsgodigital.traineddata` to `/usr/share/tesseract-ocr/4.00/tessdata/` for global use.

Added some image manipulation functions. 
Needs fine tuned parameters to recognize my LCD photo!
Screenshot: ![display_ocr](assets/Bildschirmfoto_2022-02-20_17-58-26.png)


## gImageReader
https://wiki.ubuntuusers.de/gImageReader/

Screenshot: ![gImageReader](assets/Bildschirmfoto_2022-02-20_16-49-37.png)
Working pretty well when cropping the right section manually :-)

## tesseract
See shell script [test1/espcam_ocr.sh](test1/espcam_ocr.sh), reading all pic*.jpg from [assets](assets).

As well as the pictures seem to be pretty comparable, the results are heavily different...

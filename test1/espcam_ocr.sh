#!/bin/bash
#
# espcam-Bilder vom Wärmezähler auswerten
#
 
for f in `ls //media/ras3/pi/esp-cam/pic_1645354*.jpg`
do
   ls -l $f 
  
   convert $f -crop 330x112+100+48 out.jpg
   
   tesseract out.jpg - -l letsgodigital --psm 7
   fim out.jpg
done

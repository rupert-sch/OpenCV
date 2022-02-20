#!/bin/bash
#
# espcam-Bilder vom Wärmezähler auswerten
#
 
for f in `ls ../assets/pic_*.jpg`
do
   ls -l $f 
  
   convert $f -crop 330x112+100+48 out.jpg
   
   tesseract out.jpg - -l letsgodigital --psm 7
   fim out.jpg
done

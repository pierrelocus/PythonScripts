#!/usr/bin/python3

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os

import os
filelist=os.listdir('.')
nfile = open('documents.txt', 'w+')
for fichier in filelist[:]:
    if (fichier.endswith(".png")):
        nfile.write(pytesseract.image_to_string(Image.open(fichier), lang='fra'))


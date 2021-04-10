#!/usr/bin/python3

#use in command line : python3 download_script.py

#This program downloads a file and overwrites the local file it is
# saved to if the file already exists

import requests
import os

#replace url with the url you want to download from inside quotation marks
url = 'https://terrapinworks.umd.edu/sites/default/files/images/UMD_ENG_Ctr_CMYK.svg'

#replace with file path you want the downloaded file to save to inside quotation marks
file_path = "UMD_ENG_Ctr_CMYK.svg"

r = requests.get(url, allow_redirects=True)

if os.path.exists(file_path):
    os.remove(file_path)
    open(file_path, "wb").write(r.content)
else:
    open(file_path, "wb").write(r.content)

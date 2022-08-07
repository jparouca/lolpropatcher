# Serach for zip files from page, download, extract and clean folder if sucessfull
from bs4 import BeautifulSoup
from zipfile import ZipFile
from io import BytesIO
import os,sys,requests
import urllib.request

mainurl = "http://leagueskin.net/p/download-mod-skin-2020-chn/"

# Setup BeautifulSoup
r = requests.get(mainurl)
soup = BeautifulSoup(r.content, "html.parser")

# Get download link from tag id
def get_zip_url():
    for x in soup.find_all(id="link_download3"):
        file_link = x.get('href')
        return file_link
    return None

# Download and extract zip file on current file script directory 
def download_extract():
    file_link = get_zip_url()
    if file_link is not None:
        urllib.request.urlretrieve(file_link, "lolpro.zip")
        with ZipFile (os.getcwd() + "\lolpro.zip", 'r') as zip:
            zip.extractall()
        os.remove(os.getcwd() + "\lolpro.zip")
        return True
    else:
        return False
download_extract()
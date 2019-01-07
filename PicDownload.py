# -*- coding:utf-8 -*-

import os
import time
import urllib.parse
from urllib.request import Request, urlopen

G_URL = "https://www.xxxx.com"
G_INDEX_LIMIT = 30001

def lfn_download_photo(startIndex):
    while startIndex < G_INDEX_LIMIT:
        fileno = str(startIndex)
        param = '/fileDownload.dev?attachFileNo=' + fileno

        request = Request(G_URL + param)
        response = urlopen(request)

        header = response.getheader('Content-Disposition')
        location = (str(header).find('filename='))

        if(location == -1):
            startIndex = startIndex + 1
            continue
        else:
            filename = (str(header)[location+9:])
            filename = filename.strip('\"')
            filename = urllib.parse.unquote(filename)

            print("index : " + str(startIndex) + ", filename : " + filename)

            foutput = open('./profile_pic/' + filename, 'wb')
            foutput.write(response.read())
            startIndex = startIndex + 1
        time.sleep(1)
if __name__ == '__main__':
    print("<<<<< lfn_download_photo() is start >>>>>")
    lfn_download_photo(20254)
    print("<<<<< lfn_download_photo() is completed >>>>>")

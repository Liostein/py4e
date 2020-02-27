

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# ask input values
url = input('Enter url- ')

#if len(url)<1 :
#     url =  "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
count = int(input('Enter count:'))
position = int(input('Enter position:')) - 1


#repeat times = count - 1 , repeat time =0 when count = 1
while count >= 0:
    # this is a guardian
    #print(count)
    html = urllib.request.urlopen(url, context=ctx).read()
    print('Retreving:',url)
    # get last_retrieve url for the last_name
    url_last_retrieve = url
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    #print(tags[2].get('href', None))
    url = tags[position].get('href', None)
    # while loop
    count = count - 1

# this is a guardian
#print(url_last_retrieve)
last_name = (url_last_retrieve.split("_")[-1]).split(".")[0]
print(last_name)

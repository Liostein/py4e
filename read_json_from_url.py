# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
#test sample url
#if len(url)<1: url='http://py4e-data.dr-chuck.net/comments_42.json'


#read url content as str
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# this is guardian
#print(data)


# load json
try:
    js = json.loads(data)
except:
    js = None

# this is guardian
if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

#check json contents
#print(json.dumps(js, indent=4))

#try read count value
#js['comments'][0]['count']

#initiate value of count and sum to zero
count=0
sum=0

# for loop to sum all the count value
for item in js['comments']:
    sum += int(item['count'])
    count +=1
    #this print is guardian
    #print('sum:',sum,'count',count)
print('sum:',sum,'count',count)

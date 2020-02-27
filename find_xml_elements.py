import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#read url data
url = input('Enter location: ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
# there are guardians
#print('Retrieved', len(data), 'characters')
print(data.decode())

#   make a tree under <>
tree = ET.fromstring(data)

# xpath .//element name, select all chosen elements in the entire tree
results = tree.findall('.//count')
total = 0
for item in results:
    total = total + int(item.text)
   print("count:",item.text,"total:",total)

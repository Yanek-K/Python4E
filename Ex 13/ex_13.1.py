import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl 
import re

url = input("Enter Url")
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
print("Retrieving Url", url)

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lst = list()

xm = urllib.request.urlopen(url, context = ctx).read().decode()
print("Retrieved", len(xm), 'characters')

tree = ET.fromstring(xm)
counts = tree.findall('comments/comment')
print("Count:", len(counts))

total = 0 
 
for item in counts: 
  count = item.find('count').text
  count = int(count)
  total += count
print("Sum", total)
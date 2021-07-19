import urllib
from bs4 import BeautifulSoup
import ssl 
import re

# Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

count = int(input("Enter count: "))
position = int(input("Enter position: "))
times = 0
lst = list()

while times < count:
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')

# Find all of the anchor tags
  tags = soup("a")
  url = tags[int(position - 1)].get('href', None)
  times = times + 1
  name = re.findall("known_by_([A-Z]\S*)\.", url)
  lst.append(name)
print(lst[count - 1])

  
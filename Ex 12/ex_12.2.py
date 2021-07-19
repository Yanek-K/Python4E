import urllib.request
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode - ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

spans = soup('span')
final = list()
for span in spans:
  lst = span.contents[0]
  final.append(int(lst))
print(sum(final))
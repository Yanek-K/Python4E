import urllib.request
import ssl
import json
import re

url = input("Enter Location: ")
if len(url) < 1 : url = "http://py4e-data.dr-chuck.net/comments_42.json"
print("Retrieving", url)

# Ignore SSL Certificate Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


lst = list()
data = urllib.request.urlopen(url, context=ctx)
data = data.read().decode()
jsonData = json.loads(data)
for comment in jsonData["comments"]:
  lst.append(comment['count'])
print(sum(lst))


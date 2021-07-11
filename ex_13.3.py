import urllib.request, urllib.parse, urllib.error
import ssl 
import json

# Ignore SSL Certificates
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceUrl = "http://py4e-data.dr-chuck.net/json?"

while True:
  address = input("Enter Location: ")
  if len(address) < 1 : address = "South Federal University"

  parms = dict()
  parms['address'] = address
  parms["key"] = 42
  url = serviceUrl + urllib.parse.urlencode(parms)

  print("Retrieving", url)
  uh = urllib.request.urlopen(url, context=ctx)
  data = uh.read().decode()
  print("Retrieved", len(data), 'characters')

  try: 
    js = json.loads(data)
  except: 
    js = None 

  if not js or "status" not in js or js['status'] != "OK":
    print("----Failure to Retrieve---")
    print(data)
    continue
  
  print(json.dumps(js, indent = 4))

  placeId = js['results'][0]['place_id']

  print("Place id", placeId)
  break
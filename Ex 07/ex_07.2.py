fname = input("Enter file name: ")
try:
  fh = open(fname)
except:
  print("Error, Please enter a valid file name")
  quit()

count = 0
total = 0
for line in fh:
  line.rstrip()
  if not line.startswith("X-DSPAM-Confidence: "):
    continue

  count = count + 1
  num = (line[20:27])

  total = total + float(num)
  average = total / count
  
print("Average span confidence:", average)

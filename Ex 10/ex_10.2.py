fname = input("Enter file name: ")
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)

di = dict()
lst = list()
for line in fhand : 
  if line.startswith("From "):
    wrd = line.split()
    h = wrd[5]
    h = h.split(":")
    hours = h[0]
    lst.append(hours)
for num in lst:
  di[num] = di.get(num, 0) + 1
for hour, count in sorted(di.items()):
  y = di.items()
  print(y)
  print(hour, count)
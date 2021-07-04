fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fhand = open(fname)


di = dict()
for lin in fhand: 
  lin = lin.rstrip()
  wrd = lin.split()
  if len(wrd) < 3 or not wrd[0] == "From":
    continue
  print (wrd)
  for w in wrd:
    di[w] = di.get(w, 0) + 1
    print(w, di[w])

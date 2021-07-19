fname = input ("Enter file name: ")
if len(fname) < 1 : fname = 'romeo.txt'
hand = open(fname)

di = dict()

# add items to dictionary
for lin in hand:
  lin = lin.rstrip()
  wds = lin.split()
  for w in wds:
    di[w] = di.get(w, 0) + 1 
    # print(w, di[w])
    

# find the maximum
largest = -1
word = None
for k, v in di.items() : 
  if v > largest : 
    largest = v
    word = k
print(largest, word)

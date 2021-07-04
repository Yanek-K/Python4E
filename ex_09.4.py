# Get File
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fhand = open(fname)


# Filter through lines and add email addresses to dictionary
di = dict()
lst = []

for lin in fhand: 
  lin = lin.rstrip()
  wrd = lin.split()
  if len(wrd) < 3 or not wrd[0] == "From":
    continue
  lst.append(wrd[1])
for w in lst:
  di[w] = di.get(w, 0) + 1


# loop through dicitionary and find count of highest number of emails
largest = -1
word = None
for k,v in di.items() :
  if v > largest:
    largest = v
    word = k
print(word, largest)

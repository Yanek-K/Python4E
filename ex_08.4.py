fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
  str = line.rstrip().split()
  for item in str:
    if item not in lst:
      lst.append(item)

lst.sort()
print(lst)
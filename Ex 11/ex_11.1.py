import re

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum.txt"
fhand = open(fname)
inp = fhand.read()

lst = list()
num = re.findall('[0-9]+', inp)
for number in num:
  final = float(number)
  lst.append(final)
# if len(num) != 1 : continue
print(sum(lst))



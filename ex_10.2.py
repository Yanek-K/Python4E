fhand = input("Enter File Name")
if len(fhand) < 1 : fhand = 'mbox-short.txt'
f = open(fhand)

lst = list()
di = dict()
for line in f: 
  if line.startswith("From "):
    wrd = line.split()
    h = wrd[5]
    
    h = h.split(":")
    hours = h[0]
    lst.append(hours)
for num in lst:
  di[num] = di.get(num, 0) + 1
for hour, count in sorted(di.items()):
  print(hour, count)
    
# handle = open('mbox-short.txt')
# x_list = list()
# x_l = dict()

# count = list
# for line in handle:
#    if line.startswith("From "):
#         words = line.split()
#         colon_col = words[5]
         
#         x,y,z = colon_col.split(":")
#         x_list.append(x)

# for num in x_list:
#     if num not in x_l:
#         x_l[num] = 1
#     else:
#         x_l[num] += 1


# for key, val in list(sorted(x_l.items())):
#     print(key,val)
largest = None
smallest = None
while True:
  sNum = (input("Enter a number: "))
  if sNum == "done":
    break
  try:
    fNum = int(sNum)
  except:
    print("Invalid input")
    continue
  
  if largest is None:
    largest = fNum
  elif fNum > largest:
    largest = fNum

  if smallest is None:
    smallest = fNum
  elif fNum < smallest:
    smallest = fNum
  

print("Maximum is", largest)
print("Minimum is", smallest)
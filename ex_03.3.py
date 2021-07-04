stringGrade = input("Enter Score: ")
floatGrade = float(stringGrade)
if floatGrade > 1:
  print("Error, please enter a grade between 0 and 1")
elif floatGrade >= 0.9:
  print("A")
elif floatGrade >= 0.8:
  print("B")
elif floatGrade >= 0.7:
  print("C")
elif floatGrade >= 0.6:
  print("D")
elif floatGrade < 0.6:
  print("F")


stringHrs = (input("Enter Hours: ")) 
stringRate = (input("Enter Rate: "))
try:
  floatHrs = float(stringHrs)
  floatRate = float(stringRate)
except:
  print("Error, please enter numeric input")
  quit()

if floatHrs <= 40:
  grossPay = floatHrs * floatRate
else:
  regPay = 40 * floatRate
  otp = (floatHrs - 40) * (floatRate * 1.5)
  grossPay = (regPay) + (otp)
print (grossPay)
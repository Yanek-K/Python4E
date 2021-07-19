hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hrs <= 40:
  grossPay = hrs * rate
else:
  regPay = 40 * rate
  otp = (hrs - 40) * (rate * 1.5)
  grossPay = (regPay) + (otp)
print (grossPay)
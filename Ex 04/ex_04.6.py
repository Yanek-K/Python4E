def computePay(h, r):
  if h <= 40:
    return h * r
  else:
    regPay = 40 * r
    otp = (h - 40) * (r * 1.5)
    grossPay = (regPay) + (otp)
    return grossPay

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = computePay(hrs, rate)
print("Pay", pay)

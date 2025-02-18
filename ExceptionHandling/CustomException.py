class PinError(Exception):
    pass
correctPin = 123
pin = int(input("Enter 4 digit PIN"))
try:
    if pin == correctPin :
       print("Account Unblocked")
  
except PinError as msg:
     print("Incorrect pin: ", msg)
     
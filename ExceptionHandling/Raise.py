def checkAge(age):
    if age < 18 :
        raise ValueError("Age must be greater than 18")

try:
    checkAge(12)
except ValueError as msg:
    print("Error Messege", msg)    
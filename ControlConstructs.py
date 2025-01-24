'''
1. Conditional: if-else
2. Looping: for, while
3. Jumping: Break, continue, pass

'''

def checkAge(age):
    if(age > 18):
        print("Age is greater tahn 18")
    else:
        print("Age is not greater than 18")    
checkAge(18)        

def checkingAge(age):
    if(age < 18):
        print("Child")
    elif(age > 18 and age < 65):
        print("Adult")
    elif (age > 65) :
        print("Senior Cetizen")
checkingAge(int(input("Enter your age")))        
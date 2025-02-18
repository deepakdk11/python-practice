def display1(a,b):
    try:
        print("Task started")
        print(a,b)
    except:
        print("Some error handled")
    else: 
        print("Task Executed without any exception")  
    finally:
        print("Task Ended")


display1(10,0)
display1(10,5)
display1(30,3)

# try: Used to keep the logic in which we may get some error.
# except: Will be executed when execption occurres in try block logic.
# else: Will be executed when try block logic executed without any error.
# finally: will always executed irrespective of execption occurred ot not.
def disp(a,b):
    try:
      print(a/b)
    except ZeroDivisionError: 
       print("ZeroDivisionError Occurred and Handle")
    except NameError:
       print("Name error occurred and Handle")
    except TypeError:
       print("Type Error Occurred and handle")  
    except:
       print("Some error occurred and handle")       

disp(10,0)
disp(10, "Deepak")

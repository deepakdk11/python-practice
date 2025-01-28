class Demo1:
    def display(self):
        print("Inside display1")

class Demo2(Demo1):
    pass

d2 = Demo2()
d2.display()
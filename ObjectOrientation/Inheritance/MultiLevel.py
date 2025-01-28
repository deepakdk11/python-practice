class Demo1:
    def display1(self):
        print("This is display 1")
class Demo2(Demo1):
    def display2(self):
        print("This is display 2")        
class Demo3(Demo2):
    pass    

d3 = Demo3()
d3.display1()
d3.display2()
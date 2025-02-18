'''
class Demo1:
    def display1(self):
        print("Inside of diplay 1")

class Demo2:
    def display2(self):
        print("Inside of display 2")

class Demo3(Demo1, Demo2):
    pass

d3 = Demo3()
d3.display1()
d3.display2()

'''

class Demo1:
    def __init__(self):
        self.x = 10
class Demo2:
    def __init__(self):
        self.x = 200
class Demo3(Demo1, Demo2):
    def __init__(self):
        self.x= 300       

d3 = Demo3()
print(d3.x)        
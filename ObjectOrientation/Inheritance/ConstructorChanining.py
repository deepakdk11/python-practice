'''
1. Constructor Chaning is the process of calling one constructor from another constuctor
'''

class GrandParent:
    def __init__(self):
        self.x = 100

class Parent(GrandParent):
    def __init__(self):
        self.y = 200
        super().__init__()
class Child(Parent):
    def __init__(self):
        self.z = 300
        super().__init__()

ch = Child()
print(ch.x)     
print(ch.y)
print(ch.z)   
         
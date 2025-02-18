class Student:
    def cook(self):
        print("Student is cooking")
    def play(self):
        print("Playing cricket")

class Employee(Student):
    def work(self):
        print("Employee is working")      
    def cook(self):
        print("Employee is cooking")          


e = Employee()
e.play() 

"""
work(): Specialized  Methods: Only in child class
play(): InheritednUsed as it is in child class
cook(): Overridden Method: Change Implementation in chlid
"""
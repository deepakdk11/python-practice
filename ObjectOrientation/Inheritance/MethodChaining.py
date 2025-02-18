# Method chaining is the process of calling one method from another method

class GrandParent:
    def cook(self):
        print("Grand Parent can cook biriyani")

class Parent(GrandParent):
    def cook(self):
        print("Parent can cook maggie")

class Child(Parent):
    def cook(self):
        print("Child wont cook")
        super().cook()
        super(Parent, self).cook()

ch = Child()
ch.cook()        
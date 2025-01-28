class Demo:
    def display(self):
        print("Inside display with 0 Para")
    def display(self, a):
        print("Inside display with 1 Para")  
    def display(self,a,b):
        print("Inside display with 2 Para")       

d1 = Demo()
d1.display()
d1.display(10)
d1.display(10, 20)        
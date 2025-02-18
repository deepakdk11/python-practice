class Calculator:
    def calculate(self, a, b):
        print("Calculate result of a and b")

class Add(Calculator):
    def calculate(self, a, b):
        print("Addition: ", a + b)        

class Sub(Calculator):
    def calculate(self, a, b):
        print("Subtraction: ", a-b)     

class Mul:
    pass

ref = Add()
ref.calculate(10,20)

ref = Sub()
ref.calculate(20, 10)

def permit(ref, a, b):
    if type(ref).__name__ == "Mul":
        print("Mul Class does Not calculate")
    else:    
       ref.calculate(a,b)

permit(Add(), 10,20)
permit(Sub(), 20,10)   
permit(Mul(), 10, 20) 
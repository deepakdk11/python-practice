# map(function, iterable Object) ---> Iterator Object
def double(x):
    return x*2
list1 = [1,2,3,4]
doubleList = list(map(double,list1))
print(doubleList) #[2, 4, 6, 8]

tup = ("10" , "20", "30")
print(tup) #('10', '20', '30')
inverList = tuple(map(int, tup))
print(inverList) #(10, 20, 30)  

tup1 = ("10" , "20", "30")
print(tup1) #('10', '20', '30')
inverList = tuple(map(float, tup1))
print(inverList) #(10.0, 20.0, 30.0)
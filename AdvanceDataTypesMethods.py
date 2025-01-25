list1 = list("Deepak")
print(list1) #['D', 'e', 'e', 'p', 'a', 'k']

list2 = list((10,30,20))
print(list2) #[10, 30, 20]

list3 = list({100,300,200})
print(list3) #[200, 100, 300]

list4 = list({"Name" : "Deepak", "Age" : 24})
print(list4) #['Name', 'Age']

list5 = list(range(1,5))
print(list5) #[1, 2, 3, 4]

# Tuple Menthos()

tuple1 = tuple("Deepak")
print(tuple1) #('D', 'e', 'e', 'p', 'a', 'k')

tuple2 = tuple((10,30,20))
print(tuple2) #(10, 30, 20)

tuple3 = tuple({100,300,200})
print(tuple3) #(200, 100, 300)

tuple4 = tuple({"Name" : "Deepak", "Age" : 24})
print(tuple4) #('Name', 'Age')

tuple5 = tuple(range(1,5))
print(tuple5) #(1, 2, 3, 4)

# set(iterable object)
set1 = set([10, 10, 20, 20, 30, 40])
print(set1) #{40, 10, 20, 30}

# dict(iterable object key:value)
dict1 = dict([["name" , "Deepak"], ["Age", 24]])
print(dict1) #{'name': 'Deepak', 'Age': 24}
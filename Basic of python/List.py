'''
1. In list we can store Homogeneous as well as Heterogeneous Data.
2. In list we can store duplicate values.
3. List is an ordered collection of data: Order of insertion will remain as it is in the output.
4. list are mutable: Once we declare the list we can modify it.


'''

list1 = [10, 20, 30.45, True, "Deepak", 2000]
print(list1) #[10, 20, 30.45, True, 'Deepak', 2000]

#append() : Will add element at the end of the list
list1.append(4000)
print(list1) #[10, 20, 30.45, True, 'Deepak', 2000, 4000]

#insert(index, element):
list1.insert(0, 1)
print(list1) #[1, 10, 20, 30.45, True, 'Deepak', 2000, 4000]

#remove(ele): Removes the first occurrence of the specified ele.
list1.remove(20)
print(list1) #[1, 10, 30.45, True, 'Deepak', 2000, 4000]

# in and not in Operator: 
print(2000 in list1) 

#pop(): Without argument will delete and return last element from list
removed_element = list1.pop()
print(removed_element) #4000
print(list1) #[1, 10, 30.45, True, 'Deepak', 2000]

# pop(index): With argument will delete the element at specified index
removed_element = list1.pop(4)
print(removed_element) #Deepak
print(list1) #[1, 10, 30.45, True, 2000]

# del keyword
del list1[1]
print(list1) #[1, 30.45, True, 2000]

del list1
# print(list1)  'list1' is not defined.
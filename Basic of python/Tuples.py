'''
1. In Tuple we can Homogeneous as well Heterogeneous Data.
2. In Tuples we can store duplicates.
3. Tuples are ordered collection of data.
4. Tuples are immutable: Once we declare the tuples we cannot modify it.

'''

tup1 = (10, 20, 33.09, "Deepak", True, 20000)
print(tup1) #(10, 20, 33.09, 'Deepak', True, 20000)

# tup1.append(4000) 'tuple' object has no attribute 'append'
# tup1.remove() 'tuple' object has no attribute 'remove'

# Create a singleton Tuple:
tup2 = (10,)
print(tup2, type(tup2)) #(10,) <class 'tuple'>

# U packing od Tuple:
ele1, ele2, ele3, ele4, ele5, ele6 = tup1
print(ele1)
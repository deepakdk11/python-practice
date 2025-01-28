'''
1. In Set we can store Homogeneous as well as Hetergeneous data.
2. Set is an Unordered collection of data.
3. Set does not support indexing of data.
4. In set we cannot store duplicates.
5. Sets are mutable.

'''

set1 = {10, True, "Deepak", 10, 20, 55.44}
print(set1, type(set1)) #{True, 20, 55.44, 10, 'Deepak'} <class 'set'>
# print(set1[0]) Error

# add(): Used to add an element in the set.
set1.add(500)
print(set1) #{True, 20, 500, 55.44, 'Deepak', 10}

set1.remove(500)
print(set1) #{True, 'Deepak', 20, 55.44, 10}

#pop() : Without index will delete and return one ele.
set1.pop()
print(set1) #{True, 20, 55.44, 10}
list1 = [1,2,3,4,5,6,7,8,9]

duplicateList = [i for i in list1]
print(duplicateList) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

sqList = [i**2 for i in list1]
print(sqList) #[1, 4, 9, 16, 25, 36, 49, 64, 81]

#When we have only if part then write it after for lopp.
evenList = [i for i in list1 if i % 2 == 0]
print(evenList) #[2, 4, 6, 8]

#When we have if_else both write it before for loop
even_odd = ["Even" if i%2 == 0 else "Odd" for i in list1]
print(even_odd) #['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']


list2 = [[10,20],[30,40],[50,60]]

new_list2 = [j for i in list2 for j in i]
print(new_list2)
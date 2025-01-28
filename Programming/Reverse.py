# object.reverse() will reverse the original object.
li = [10, 5, 20, 7, 40]
li.reverse()
print(li) # [40, 7, 20, 5, 10]

#revered(object)
li2 = [23, 34, 54, 675]
print(list(reversed(li2))) #[675, 54, 34, 23]


li3 = [1,2,3,4,5,6,7,8,9]
newReverseList = list(reversed(li3)) #----> Creating new reverse list
newReverseList.reverse() #-----> Reversing Orginal List
#listName[start:end:steps]

list1 = [10, 20, 30, 40, 50, 60]
sub_list1 = list1[1:4:1]
print(sub_list1) #[20, 30, 40]

sub_list2 = list1[1::]
print(sub_list2) #[20, 30, 40, 50, 60]


sub_list3 = list1[::2]
print(sub_list3) #[10, 30, 50]

reverse_list = list1[::-1]
print(reverse_list) #[60, 50, 40, 30, 20, 10]

print(list1[-1::]) #[60]

'''
Q: What is list Slicing?
Is Used to create sublist from main list.
Syntax: List_name[start:end:steps]
'''
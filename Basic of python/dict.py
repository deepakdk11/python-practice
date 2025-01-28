'''
1. In dict we cannot store duplicate keys
2. In dict we can store duplicate values
3. Dict is mutable
'''

d1 = {
    "Name" : "Deepak",
    "Age" : 24,
    "Phone" : 12345678
}
print(d1, type(d1)) #{'Name': 'Deepak', 'Age': 24, 'Phone': 12345678} <class 'dict'>

d1["Name"] = "Sandhiya"
print(d1) #'Name': 'Sandhiya', 'Age': 24, 'Phone': 12345678}

for i in d1.values():
    print(i)

for i in d1.keys():
    print(i)

for i in d1.items():
    print(i)

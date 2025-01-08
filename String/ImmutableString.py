# Strings are immutable: 
# 1.Once we declare the string we cannot modify it, if we try to modify the string it will create new string.
# 2.if new string does not have any reference variable then it will bew removed
s1 = "Deepak"
s2 = "kumar"
s1 = s1.upper()
print(s1)

#How to check memory addrees
print(id(s1))



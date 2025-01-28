# Strings are immutable: 
# 1.Once we declare the string we cannot modify it, if we try to modify the string it will create new string.
# 2.if new string does not have any reference variable then it will bew removed.
# 3.Python Internally uses String Interning.
# 4.String Interning is the process of checking string Inter pool before creating any new object.

# Whenever we want to create new object, python first will check string intern pool, weather that object already exist or not.

#When Object already exist in the string intern Records then address of existing object will be reused.

s1 = "Deepak"
s2 = "kumar"
print(s1)

#How to check memory addrees
print(s1[4],id(s1[4]))
print(s1[4],id(s2[3]))
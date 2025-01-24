# If string is holding integer then it can be converted into int.
a = "30"
b = int(a);
print(a, type(a))
print(b, type(b))

#string to integer conversion is not allowed.
x = "Deepak"
# y = int(x)
# print(y, type(y))

p = float(input("Enter Float type data"))
print(p, type(p))

#bool()
q = 12
print(q, type(q))
q = bool(q)
print(q, type(q))
'''
1. While converting int to bool for all non zero values we will get True.
2. While converting int to bool for 0 and empty string we will get false.

'''


# li = list(map(int, input("Enter space seperated Element").split()))
# print(li) #[12, 34, 56, 78, 890]

# tup = tuple(map(int, input("Enter space seperated Element").split()))
# print(tup) #(23, 45, 67, 89)

li = list(map(int, input("Enter space seperated Element").split()))
li = [i for i in li if i%2 ==0]
print(li)
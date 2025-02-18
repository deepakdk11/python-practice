n = int(input("Enter the number"))
width = len(bin(n)) - 2
for i in range(1, n+1):
    dec = str(i).rjust(width)
    ot = oct(i)[2:].rjust(width)
    hx = hex(i)[2:].rjust(width)
    binary = bin(i)[2:].rjust(width)
    print(f'{dec} {ot} {hx} {binary}')
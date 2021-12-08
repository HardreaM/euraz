a = 0b100001111

mask1 = 0b100
x = a & mask1
x>>=2
print(bin(x))
mask2 = 0b10000
y = a & mask2
y>>=3
c = x|y
print(bin(y))
print(bin(c))
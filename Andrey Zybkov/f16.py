def fact (n, out=1):
    if n == 0:
        return out
    else:
        return fact(n-1, out*n)

print(fact(6))
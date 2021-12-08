def binary (n):
    out = ''
    
    while n > 0:
        out = str(n%2) + out
        n //= 2

    return out

print(binary(255))
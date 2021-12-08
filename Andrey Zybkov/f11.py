def to_decimal (n):
    
    n = n[::-1]
    out = 0
    for i in range(len(n)):
        out += int(n[i]) * 2**i

    return out

print(to_decimal('11111111'))
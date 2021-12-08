def f ():

    n = int(input())

    if n<0:
        raise ValueError()
    
    count = 0

    while n%2 == 0:
        n //= 2
        count += 1

    print(2**count)
    return

while True:
    f()
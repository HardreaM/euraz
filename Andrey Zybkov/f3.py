import math

def f ():

    c = int(input())

    if c == 0:
        raise ValueError()

    if c > 0:
        print('None')
        return
    
    print('x>' + str(max(math.sqrt(abs(c)), (-c+1)/2)))
    return

while True:
    f()
import math

def f():

    c = int(input())

    if c == 0:
        raise ValueError()

    if c>0:
        print('All X')
        return

    print('x<' + str(math.sqrt(abs(c))) + ' and ' + 'x>' + str(math.sqrt(abs(c))))
    return

while True:
    f()
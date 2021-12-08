import math

def f ():

    x, y = map(float, input().split())

    if y > 1-x and y < math.sin(x):
        print('True')
        return
    print('False')
    return

while True:
    f()
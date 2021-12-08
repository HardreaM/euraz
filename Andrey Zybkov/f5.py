import math

def f ():
    
    n = int(input())

    if n < 0:
        raise ValueError()

    answ = math.log(n,4)

    if answ % int(answ) == 0.0:
        print(int(answ))
    else:
        print('None')

    return

while True:
    f()
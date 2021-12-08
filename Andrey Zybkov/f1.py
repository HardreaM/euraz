def f ():
    a,b = map(int, input())
    print(a)
    print(b)
    if a == 0 or b == 0:
        raise ValueError()

    x1 = a

    print('x<' + str(min(x1,0)) + ' and ' + 'x>' + str(max(x1,0)))

while True:
    f()